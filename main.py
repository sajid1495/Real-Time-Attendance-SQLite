import signal, sys
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
import os
from student import Student
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from developer import Developer
from helpdesk import HelpDesk

class Face_Recognition_System: 
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed') 
        self.root.title("Face Recognition System")

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Background Image
        img = Image.open(r"images\_bg.png")  
        img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=screen_width, height=screen_height)

        title_lbl = Label(bg_image, text="REAL TIME ATTENDANCE SYSTEM SOFTWARE", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
        title_lbl.place(x=0, y=0, width=screen_width, height=55)


        #students button
        student = Image.open(r"images\students.png")  
        student = student.resize((180, 180), Image.Resampling.LANCZOS)
        self.photostudent = ImageTk.PhotoImage(student)

        btn1 = Button(bg_image, image=self.photostudent, command=self.student_details , cursor="hand2") 
        btn1.place(x=255, y=130, width=180, height=180)

        btn1_text = Button(bg_image, text="Students Details", command=self.student_details , cursor="hand2", font=("Calibri", 14, "bold"))
        btn1_text.place(x=255, y=310, width=180, height=40)


        #detect face button
        detect_face = Image.open(r"images\detect_faces.png")  
        detect_face = detect_face.resize((180, 180), Image.Resampling.LANCZOS)
        self.photodetect_face = ImageTk.PhotoImage(detect_face)

        btn2 = Button(bg_image, image=self.photodetect_face, cursor="hand2", command=self.face_recognition)
        btn2.place(x=535, y=130, width=180, height=180)

        btn2_text = Button(bg_image, text="Face Detector", cursor="hand2", command=self.face_recognition, font=("Calibri", 14, "bold"))
        btn2_text.place(x=535, y=310, width=180, height=40)

        #attendance button
        attendance = Image.open(r"images\attendance.png")  
        attendance = attendance.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoattendance = ImageTk.PhotoImage(attendance)

        btn3 = Button(bg_image, image=self.photoattendance, cursor="hand2", command=self.attendance)
        btn3.place(x=815, y=130, width=180, height=180)

        btn3_text = Button(bg_image, text="Attendance", cursor="hand2", command=self.attendance, font=("Calibri", 14, "bold"))
        btn3_text.place(x=815, y=310, width=180, height=40)

        #model training
        traindata = Image.open(r"images\train_data.png")  
        traindata = traindata.resize((180, 180), Image.Resampling.LANCZOS)
        self.phototraindata = ImageTk.PhotoImage(traindata)

        btn4 = Button(bg_image, image=self.phototraindata, cursor="hand2", command=self.train_classifier)
        btn4.place(x=1095, y=130, width=180, height=180)

        btn4_text = Button(bg_image, text="Train Model", cursor="hand2", command=self.train_classifier, font=("Calibri", 14, "bold"))
        btn4_text.place(x=1095, y=310, width=180, height=40)

        #photos button
        photos = Image.open(r"images\photos.png")  
        photos = photos.resize((180, 180), Image.Resampling.LANCZOS)
        self.photophotos = ImageTk.PhotoImage(photos)

        btn5 = Button(bg_image, image=self.photophotos, cursor="hand2", command=self.open_img)
        btn5.place(x=255, y=420, width=180, height=180)

        btn5_text = Button(bg_image, text="Photoes", cursor="hand2", command=self.open_img, font=("Calibri", 14, "bold"))
        btn5_text.place(x=255, y=600, width=180, height=40)

        #help desk button
        helpdesk = Image.open(r"images\help_desk.png")   
        helpdesk = helpdesk.resize((180, 180), Image.Resampling.LANCZOS)
        self.photohelpdesk = ImageTk.PhotoImage(helpdesk)

        btn6 = Button(bg_image, image=self.photohelpdesk, cursor="hand2", command=self.help_desk)
        btn6.place(x=535, y=420, width=180, height=180)

        btn6_text = Button(bg_image, text="Help Desk", cursor="hand2", command=self.help_desk, font=("Calibri", 14, "bold"))
        btn6_text.place(x=535, y=600, width=180, height=40)

        #developer button
        developer = Image.open(r"images\developer.png")   
        developer = developer.resize((180, 180), Image.Resampling.LANCZOS)
        self.photodeveloper = ImageTk.PhotoImage(developer)

        btn7 = Button(bg_image, image=self.photodeveloper, cursor="hand2", command=self.developer)
        btn7.place(x=815, y=420, width=180, height=180)

        btn7_text = Button(bg_image, text="Developer", cursor="hand2", command=self.developer, font=("Calibri", 14, "bold"))
        btn7_text.place(x=815, y=600, width=180, height=40)

        #exit button
        exitbtn = Image.open(r"images\exit.png")   
        exitbtn = exitbtn.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoexit = ImageTk.PhotoImage(exitbtn)

        btn8 = Button(bg_image, image=self.photoexit, cursor="hand2", command=self.exit_app)
        btn8.place(x=1095, y=420, width=180, height=180)

        btn8_text = Button(bg_image, text="Exit", cursor="hand2", command=self.exit_app, font=("Calibri", 14, "bold"))
        btn8_text.place(x=1095, y=600, width=180, height=40)



    #student button function
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    #train button function
    def train_classifier(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    #face recognition function
    def face_recognition(self):
        self.face_window = Toplevel(self.root)
        self.face_window.state('zoomed')
        self.app = FaceRecognition(self.face_window)

    #attendance function
    def attendance(self):
        # Check if attendance window already exists and is open
        if hasattr(self, 'attendance_window') and self.attendance_window.winfo_exists():
            self.attendance_window.lift()
            self.attendance_window.focus_force()
            return
        self.attendance_window = Toplevel(self.root)
        self.app = Attendance(self.attendance_window)

    #open images function
    def open_img(self):
        os.startfile("data")

    #developer function
    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    #help desk function
    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = HelpDesk(self.new_window)

    #exit function
    def exit_app(self):
        self.root.quit()
        self.root.destroy()













if __name__ == "__main__":
    root = Tk()

    def _graceful_exit(signum=None, frame=None):
        try:
            root.quit()
            root.destroy()
        except:
            pass
        sys.exit(0)

    signal.signal(signal.SIGINT, _graceful_exit)
    signal.signal(signal.SIGTERM, _graceful_exit)

    obj = Face_Recognition_System(root)

    def on_close():
        try:
            if hasattr(obj, "cap") and obj.cap:
                obj.cap.release()
        except:
            pass
        _graceful_exit()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
