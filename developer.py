from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import sys 

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')  # Full screen
        self.root.title("Face Recognition System")

        # Background Image
        img = Image.open(r"images\_bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_image, text="DEVELOPER INFORMATION", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
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

        # Main Frame for Developer Info
        main_frame = Frame(bg_image, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=200, y=100, width=1130, height=620)

        # Left Frame for Photo
        left_frame = Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        left_frame.place(x=20, y=20, width=350, height=580)

        # Developer Photo
        try:
            dev_img = Image.open(r"images\developer_info.png")
        except:
            # Create a placeholder if image not found
            dev_img = Image.new('RGB', (400, 400), color='lightgray')
        
        dev_img = dev_img.resize((400, 400), Image.Resampling.LANCZOS)
        self.dev_photo = ImageTk.PhotoImage(dev_img)

        photo_lbl = Label(left_frame, image=self.dev_photo, bg="white")
        photo_lbl.place(x=10, y=10, width=330, height=400)

        # Developer Name below photo
        name_below_photo = Label(left_frame, text="Sajid", font=("Calibri", 22, "bold"), bg="white", fg="#2c3e50")
        name_below_photo.place(x=10, y=420, width=330)

        role_lbl = Label(left_frame, text="Undergrad Student", font=("Calibri", 14), bg="white", fg="#7f8c8d")
        role_lbl.place(x=10, y=455, width=330)

        dept_lbl = Label(left_frame, text="Department of CSE", font=("Calibri", 12), bg="white", fg="#7f8c8d")
        dept_lbl.place(x=10, y=480, width=330)

        institute_lbl = Label(left_frame, text="RUET", font=("Calibri", 12, "bold"), bg="white", fg="#e74c3c")
        institute_lbl.place(x=10, y=505, width=330)

        # Right Frame for Details
        right_frame = Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        right_frame.place(x=390, y=20, width=720, height=580)

        # Title in right frame
        info_title = Label(right_frame, text="Contact Information", font=("Calibri", 24, "bold"), bg="white", fg="#e74c3c")
        info_title.place(x=20, y=20)

        # Separator line
        separator = Frame(right_frame, bg="#e74c3c", height=3)
        separator.place(x=20, y=65, width=680)

        # Info Labels and Values
        info_y = 90
        info_gap = 50

        # Name
        Label(right_frame, text="Full Name:", font=("Calibri", 14, "bold"), bg="white", fg="#34495e").place(x=30, y=info_y)
        Label(right_frame, text="Sajedul Islam", font=("Calibri", 16, "bold"), bg="white", fg="#2c3e50").place(x=200, y=info_y)

        # Email
        info_y += info_gap
        Label(right_frame, text="Email:", font=("Calibri", 14, "bold"), bg="white", fg="#34495e").place(x=30, y=info_y)
        email_lbl = Label(right_frame, text="m.sajid1495@gmail.com", font=("Calibri", 14, "underline"), bg="white", fg="#3498db", cursor="hand2")
        email_lbl.place(x=200, y=info_y)
        email_lbl.bind("<Button-1>", lambda e: webbrowser.open("mailto:m.sajid1495@gmail.com"))

        # Phone
        info_y += info_gap
        Label(right_frame, text="WhatsApp:", font=("Calibri", 14, "bold"), bg="white", fg="#34495e").place(x=30, y=info_y)
        whatsapp_lbl = Label(right_frame, text="+880 1738 977967", font=("Calibri", 14, "underline"), bg="white", fg="#25D366", cursor="hand2")
        whatsapp_lbl.place(x=200, y=info_y)
        whatsapp_lbl.bind("<Button-1>", lambda e: webbrowser.open("https://wa.me/8801738977967"))

        # LinkedIn
        info_y += info_gap
        Label(right_frame, text="LinkedIn:", font=("Calibri", 14, "bold"), bg="white", fg="#34495e").place(x=30, y=info_y)
        linkedin_lbl = Label(right_frame, text="@sajidruetcse21", font=("Calibri", 14, "underline"), bg="white", fg="#0077b5", cursor="hand2")
        linkedin_lbl.place(x=200, y=info_y)
        linkedin_lbl.bind("<Button-1>", lambda e: webbrowser.open("https://www.linkedin.com/in/sajidruetcse21/"))

        # GitHub
        info_y += info_gap
        Label(right_frame, text="GitHub:", font=("Calibri", 14, "bold"), bg="white", fg="#34495e").place(x=30, y=info_y)
        github_lbl = Label(right_frame, text="@sajid1495", font=("Calibri", 14, "underline"), bg="white", fg="#333", cursor="hand2")
        github_lbl.place(x=200, y=info_y)
        github_lbl.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/sajid1495"))

        # Portfolio
        info_y += info_gap
        Label(right_frame, text="Portfolio:", font=("Calibri", 14, "bold"), bg="white", fg="#34495e").place(x=30, y=info_y)
        portfolio_lbl = Label(right_frame, text="https://portfolioofsajid.netlify.app/", font=("Calibri", 14, "underline"), bg="white", fg="#9b59b6", cursor="hand2")
        portfolio_lbl.place(x=200, y=info_y)
        portfolio_lbl.bind("<Button-1>", lambda e: webbrowser.open("https://portfolioofsajid.netlify.app/"))

        # About Section
        info_y += info_gap + 20
        Label(right_frame, text="About Me", font=("Calibri", 18, "bold"), bg="white", fg="#e74c3c").place(x=30, y=info_y)
        
        separator2 = Frame(right_frame, bg="#e74c3c", height=2)
        separator2.place(x=30, y=info_y + 35, width=660)

        info_y += 50
        about_text = """I am a passionate CS undergraduate student with expertise in Python, Machine Learning, and Computer Vision. I love building innovative solutions that make a difference. This Face Recognition Attendance System is one of my projects that combines my interest in AI and practical application development."""
        
        about_lbl = Label(right_frame, text=about_text, font=("Calibri", 12), bg="white", fg="#7f8c8d", justify=LEFT, wraplength=660, anchor="w")
        about_lbl.place(x=30, y=info_y, width=660)

    # Go to Home (close current window)
    def go_home(self):
        self.root.destroy()

    # Exit entire application
    def exit_app(self):
        sys.exit()


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()