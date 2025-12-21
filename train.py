from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import cv2
import os
import numpy as np
import sys


class Train:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')  # Full screen
        self.root.title("Face Recognition System")

        img = Image.open(r"images\_bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_image, text="MODEL TRAINING", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
        title_lbl.place(x=0, y=0, width=1540, height=55)

        # Logout Button (left side)
        logout_img = Image.open(r"images\log-out.png")
        logout_img = logout_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.logout_photo = ImageTk.PhotoImage(logout_img)
        
        logout_btn = Button(bg_image, image=self.logout_photo, cursor="hand2", command=self.exit_app, bd=0, bg="lavender", activebackground="lavender")
        logout_btn.place(x=10, y=7, width=40, height=40)

        # Home Button (right side)
        home_img = Image.open(r"images\home-button.png")
        home_img = home_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.home_photo = ImageTk.PhotoImage(home_img)
        
        home_btn = Button(bg_image, image=self.home_photo, cursor="hand2", command=self.go_home, bd=0, bg="lavender", activebackground="lavender")
        home_btn.place(x=1490, y=7, width=40, height=40)

        # Create a frame to center the button
        button_frame = Frame(bg_image, bg="white", bd=3, relief=RIDGE)
        button_frame.place(x=565, y=300, width=400, height=200)

        # Inner frame for gradient effect
        inner_frame = Frame(button_frame, bg="#1a1a2e")
        inner_frame.place(x=5, y=5, width=388, height=188)

        # Title inside the button frame
        frame_title = Label(inner_frame, text="Click to Train Model", font=("Helvetica", 14), bg="#1a1a2e", fg="#eee")
        frame_title.place(x=0, y=20, width=388)

        # Attractive TRAIN MODEL button
        train_btn = Button(
            inner_frame,
            text="TRAIN MODEL",
            command=self.train_classifier,
            font=("Helvetica", 20, "bold"),
            bg="#e94560",
            fg="white",
            activebackground="#ff6b6b",
            activeforeground="white",
            cursor="hand2",
            bd=0,
            relief=FLAT,
            padx=30,
            pady=15
        )
        train_btn.place(x=80, y=70, width=230, height=60)

        # Hover effects
        def on_enter(e):
            train_btn['bg'] = '#ff6b6b'
            train_btn['font'] = ("Helvetica", 21, "bold")

        def on_leave(e):
            train_btn['bg'] = '#e94560'
            train_btn['font'] = ("Helvetica", 20, "bold")

        train_btn.bind("<Enter>", on_enter)
        train_btn.bind("<Leave>", on_leave)

        # Info label
        info_label = Label(inner_frame, text="Train your face recognition model", font=("Helvetica", 10), bg="#1a1a2e", fg="#888")
        info_label.place(x=0, y=145, width=388)

    def train_classifier(self):        
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        classifier_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classifier.xml")
        
        # Check if data directory exists and has files
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory not found!\n{data_dir}", parent=self.root)
            return
        
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png', '.jpeg'))]
        
        if len(path) == 0:
            messagebox.showerror("Error", "No training images found in data folder!", parent=self.root)
            return
            
        faces = []
        ids = []
        
        for image in path:
            try:
                img = Image.open(image).convert('L')  # grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                
                cv2.imshow("Training", imageNp)
                # Wait for 1ms and allow window to update
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except Exception as e:
                print(f"Error processing {image}: {e}")
                continue
                
        ids = np.array(ids)

        # Close OpenCV window before training
        cv2.destroyAllWindows()
        cv2.waitKey(1)  # Required for window to actually close on Windows

        if len(faces) == 0:
            messagebox.showerror("Error", "No valid faces found for training!", parent=self.root)
            return

        try:
            # Train the classifier and save
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write(classifier_path)
            
            # Verify file was created
            if os.path.exists(classifier_path):
                messagebox.showinfo("Success", f"Model trained successfully!\n\nTotal images: {len(faces)}\nUnique IDs: {len(set(ids))}\n\nSaved to: {classifier_path}", parent=self.root)
            else:
                messagebox.showerror("Error", "Failed to save classifier.xml!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {str(e)}", parent=self.root)
        
        messagebox.showinfo("Success", f"Model trained successfully!\n\nTotal images: {len(faces)}\nUnique IDs: {len(set(ids))}", parent=self.root)

    # Go to Home (close current window)
    def go_home(self):
        self.root.destroy()

    # Exit entire application
    def exit_app(self):
        sys.exit()


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()