from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import sqlite3
from database import get_connection
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import sys
import time


class FaceRecognition:
    def __init__(self, parent):
        self.root = parent
        self.root.title("Face Recognition System")
        self.root.geometry("1540x800")
        img = Image.open(r"images\face_recognition_bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_label = Label(self.root, image=self.photoimg)
        bg_label.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_label, text="FACE RECOGNITION", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
        title_lbl.place(x=0, y=0, width=1540, height=55)

        # Logout Button (left side)
        logout_img = Image.open(r"images\log-out.png")
        logout_img = logout_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.logout_photo = ImageTk.PhotoImage(logout_img)
        logout_btn = Button(bg_label, image=self.logout_photo, cursor="hand2", command=self.exit_app, bd=0, bg="lavender", activebackground="lavender")
        logout_btn.place(x=10, y=7, width=40, height=40)

        # Home Button (right side)
        home_img = Image.open(r"images\home-button.png")
        home_img = home_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.home_photo = ImageTk.PhotoImage(home_img)
        home_btn = Button(bg_label, image=self.home_photo, cursor="hand2", command=self.go_home, bd=0, bg="lavender", activebackground="lavender")
        home_btn.place(x=1490, y=7, width=40, height=40)

        #button to start face recognition
        recognize_btn = Button(bg_label, text="Detect Face", command=self.face_recognize, font=("Helvetica", 14, "bold"), bg="red", fg="white", cursor="hand2")
        recognize_btn.place(x=1040, y=653, width=200, height=35)


    #=========attendance function=========
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            now = datetime.now()
            today_date = now.strftime("%d-%m-%Y")
            

            for line in myDataList:
                entry = line.strip().split(",")
                if len(entry) >= 5:
                    student_id = str(entry[0])
                    attendance_date = entry[4].split()[0] if " " in entry[4] else entry[4]
                    if str(i) == student_id and attendance_date == today_date:
                        return  

            dtString = now.strftime("%d-%m-%Y,%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtString},Present")



    #=========face recognition function=========
    def face_recognize(self):
        try:
            conn = get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Student_id, Name, Roll, Dept FROM student")
            students = my_cursor.fetchall()
            conn.close()
            
            
            student_data = {}
            for student in students:
                try:
                    student_id = int(student[0])  
                except:
                    student_id = student[0]
                student_data[student_id] = {
                    "name": student[1],
                    "roll": student[2],
                    "dept": student[3]
                }
            
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not connect to database: {e}")
            return
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                
                # Set default values
                i = id
                n, r, d = "Unknown", "N/A", "N/A"
                
                if id in student_data:
                    n = student_data[id]["name"]
                    r = student_data[id]["roll"]
                    d = student_data[id]["dept"]
 
                if confidence > 77 and id in student_data:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Department:{d}", (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)

                coord.append((x, y, w, h))

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
        # Check if classifier file exists
        classifier_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classifier.xml")
        if not os.path.exists(classifier_path):
            messagebox.showerror("Error", "Classifier not found! Please train the model first.", parent=self.root)
            return
            
        clf = cv2.face.LBPHFaceRecognizer_create()
        try:
            clf.read(classifier_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load classifier: {e}", parent=self.root)
            return

        # Open camera with DSHOW backend (best for Windows)
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        # Give camera time to initialize
        time.sleep(0.3)
        
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open camera!", parent=self.root)
            return
        
        # Set camera properties for better performance
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        cv2.namedWindow("Face Recognition - Press Q to Exit", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Face Recognition - Press Q to Exit", 800, 600)
        while True:
            ret, img = video_cap.read()
            if not ret or img is None:
                continue
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition - Press Q to Exit", img)
            key = cv2.waitKey(1) & 0xFF
            if key == 13 or key == ord('q') or key == 27:
                break
            try:
                if cv2.getWindowProperty("Face Recognition - Press Q to Exit", cv2.WND_PROP_VISIBLE) < 1:
                    break
            except:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    # Go to Home (close current window)
    def go_home(self):
        self.root.destroy()

    # Exit entire application
    def exit_app(self):
        sys.exit()













if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()