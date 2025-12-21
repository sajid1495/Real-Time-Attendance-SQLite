from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys


class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')  # Full screen
        self.root.title("Help Desk - Face Recognition System")

        # Background Image
        img = Image.open(r"images\_bg.png")
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_image, text="HELP DESK", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
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

        # Main Frame
        main_frame = Frame(bg_image, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=15, y=80, width=1500, height=680)

        # ============ LEFT FRAME - FEATURES ============
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="System Features", font=("Calibri", 16, "bold"), fg="#e74c3c")
        left_frame.place(x=10, y=10, width=730, height=655)

        # Features Title
        features_title = Label(left_frame, text="Key Features of the System", font=("Calibri", 18, "bold"), bg="white", fg="#2c3e50")
        features_title.place(x=20, y=10)

        separator1 = Frame(left_frame, bg="#e74c3c", height=2)
        separator1.place(x=20, y=45, width=690)

        # Features List
        features = [
            ("👤 Student Management", "Add, update, delete, and search student records with complete details including personal information and course details."),
            ("📸 Face Detection", "Capture and store facial data of students using advanced OpenCV face detection algorithms for accurate recognition."),
            ("🎯 Model Training", "Train the face recognition model using collected facial data to improve recognition accuracy."),
            ("✅ Face Recognition", "Real-time face recognition system that identifies students and marks their attendance automatically."),
            ("📊 Attendance Tracking", "View, export, and manage attendance records with date and time stamps in CSV format."),
            ("🖼️ Photo Gallery", "Access and manage all captured student photos organized by student ID."),
            ("👨‍💻 Developer Info", "View information about the system developer and contact details."),
            ("❓ Help Desk", "Comprehensive help and user manual for system navigation and troubleshooting.")
        ]

        y_pos = 60
        for title, desc in features:
            # Feature Title
            feat_title = Label(left_frame, text=title, font=("Calibri", 13, "bold"), bg="white", fg="#3498db", anchor="w")
            feat_title.place(x=30, y=y_pos, width=680)
            
            # Feature Description
            feat_desc = Label(left_frame, text=desc, font=("Calibri", 11), bg="white", fg="#7f8c8d", anchor="w", wraplength=660, justify=LEFT)
            feat_desc.place(x=30, y=y_pos + 22, width=680)
            
            y_pos += 70

        # ============ RIGHT FRAME - USER MANUAL ============
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="User Manual", font=("Calibri", 16, "bold"), fg="#e74c3c")
        right_frame.place(x=750, y=10, width=740, height=655)

        # Create a canvas with scrollbar for user manual
        canvas_frame = Frame(right_frame, bg="white")
        canvas_frame.place(x=5, y=5, width=725, height=620)

        canvas = Canvas(canvas_frame, bg="white", highlightthickness=0)
        scrollbar = Scrollbar(canvas_frame, orient=VERTICAL, command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # User Manual Content
        manual_title = Label(scrollable_frame, text="How to Use This System", font=("Calibri", 18, "bold"), bg="white", fg="#2c3e50")
        manual_title.pack(anchor="w", padx=20, pady=(10, 5))

        separator2 = Frame(scrollable_frame, bg="#e74c3c", height=2)
        separator2.pack(fill=X, padx=20, pady=5)

        # Manual Sections
        manual_sections = [
            ("Step 1: Add Student Details", 
             """1. Click on "Students Details" from the main menu.
2. Fill in all required fields:
   • Select Department, Course, Year, and Semester
   • Enter Student ID, Name, Roll No, and other details
3. Choose "Take Photo Sample" option.
4. Click "Save" to store the student information.
5. Click "Take Photo Sample" button to capture facial data."""),
            
            ("Step 2: Capture Face Samples",
             """1. After clicking "Take Photo Sample", camera will open.
2. Position your face clearly in front of the camera.
3. The system will automatically capture 100 face samples.
4. Keep your face steady and well-lit for best results.
5. Press Enter to stop early if needed.
6. Wait for "Generating data set completed!" message."""),
            
            ("Step 3: Train the Model",
             """1. Click on "Train Model" from the main menu.
2. Click "Train Classifier" button.
3. Wait for the training process to complete.
4. Training uses all captured face samples.
5. A success message will appear when done.
6. The classifier.xml file will be updated."""),
            
            ("Step 4: Face Recognition & Attendance",
             """1. Click on "Face Detector" from the main menu.
2. Click "Face Recognition" button to start camera.
3. The system will detect and recognize faces in real-time.
4. Recognized students will have attendance marked automatically.
5. Attendance is saved with timestamp to attendance.csv.
6. Press Enter to stop recognition."""),
            
            ("Step 5: View Attendance Records",
             """1. Click on "Attendance" from the main menu.
2. View all attendance records in the table.
3. Use "Import CSV" to load attendance data.
4. Use "Export CSV" to save attendance records.
5. Search for specific records using filters.
6. Click on a record to view/edit details."""),
            
            ("Step 6: Managing Photos",
             """1. Click on "Photoes" from the main menu.
2. This opens the data folder containing all face samples.
3. Photos are named as: user.[StudentID].[PhotoNumber].jpg
4. You can view or delete photos as needed.
5. Deleting photos will require retraining the model."""),
            
            ("Troubleshooting Tips",
             """• Camera not working: Check camera permissions and connections.
• Face not detected: Ensure proper lighting and face positioning.
• Recognition errors: Retrain the model with more samples.
• Database errors: Check if attendance.db file exists in the project folder.
• Slow performance: Close other applications using the camera.
• Cannot save data: Ensure the project folder is not read-only."""),
            
            ("Contact Support",
             """For technical support or queries:
• Check Developer section for contact information.
• Email your queries with screenshots if possible.
• Include error messages for faster resolution.""")
        ]

        for section_title, section_content in manual_sections:
            # Section Title
            sec_title = Label(scrollable_frame, text=section_title, font=("Calibri", 14, "bold"), bg="white", fg="#3498db")
            sec_title.pack(anchor="w", padx=20, pady=(15, 5))
            
            # Section Content
            sec_content = Label(scrollable_frame, text=section_content, font=("Calibri", 11), bg="white", fg="#7f8c8d", justify=LEFT, anchor="w")
            sec_content.pack(anchor="w", padx=30, pady=(0, 10))

        # Add some padding at the bottom
        bottom_padding = Label(scrollable_frame, text="", bg="white", height=2)
        bottom_padding.pack()

    # Go to Home (close current window)
    def go_home(self):
        self.root.destroy()

    # Exit entire application
    def exit_app(self):
        sys.exit()


if __name__ == "__main__":
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()
