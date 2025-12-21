import signal, sys
from tkinter import*
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk 
import os
import csv
from student import Student
from train import Train
from face_recognition import FaceRecognition

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')  # Full screen
        self.root.title("Attendance Management System")
        self.root.focus_force()

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_status = StringVar()

        # Background Image
        img = Image.open(r"images\_bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_image, text="ATTENDANCE MANAGEMENT SYSTEM", font=("Calibri", 35, "bold"), bg="lavender", fg="darkgreen")
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

        # Main Frame (covers the whole display below title)
        main_frame = Frame(bg_image, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=50, y=130, width=1430, height=585)

        # Left Frame - Student Information
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", 
                                font=("Calibri", 12, "bold"), bg="white", fg="crimson")
        left_frame.place(x=5, y=5, width=705, height=570)

        # Image inside left frame
        img_left = Image.open(r"images\face_recognition_bg.png")
        img_left = img_left.resize((690, 230), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lbl_left_img = Label(left_frame, image=self.photoimg_left)
        lbl_left_img.place(x=5, y=0, width=690, height=230)

        # Entry Fields Frame
        entry_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        entry_frame.place(x=5, y=235, width=690, height=235)

        # Employee ID
        lbl_atten_id = Label(entry_frame, text="Attendance ID:", font=("Calibri", 13, "bold"), bg="white")
        lbl_atten_id.grid(row=0, column=0, padx=10, pady=12, sticky=W)
        entry_atten_id = Entry(entry_frame, textvariable=self.var_atten_id, font=("Calibri", 13), bd=1, relief=SOLID, width=18)
        entry_atten_id.grid(row=0, column=1, padx=5, pady=12, ipady=3)

        # Roll
        lbl_roll = Label(entry_frame, text="Roll:", font=("Calibri", 13, "bold"), bg="white")
        lbl_roll.grid(row=0, column=2, padx=10, pady=12, sticky=W)
        entry_roll = Entry(entry_frame, textvariable=self.var_atten_roll, font=("Calibri", 13), bd=1, relief=SOLID, width=18)
        entry_roll.grid(row=0, column=3, padx=5, pady=12, ipady=3)

        # Name
        lbl_name = Label(entry_frame, text="Name:", font=("Calibri", 13, "bold"), bg="white")
        lbl_name.grid(row=1, column=0, padx=10, pady=12, sticky=W)
        entry_name = Entry(entry_frame, textvariable=self.var_atten_name, font=("Calibri", 13), bd=1, relief=SOLID, width=18)
        entry_name.grid(row=1, column=1, padx=5, pady=12, ipady=3)

        # Department
        lbl_dep = Label(entry_frame, text="Department:", font=("Calibri", 13, "bold"), bg="white")
        lbl_dep.grid(row=1, column=2, padx=10, pady=12, sticky=W)
        entry_dep = Entry(entry_frame, textvariable=self.var_atten_dep, font=("Calibri", 13), bd=1, relief=SOLID, width=18)
        entry_dep.grid(row=1, column=3, padx=5, pady=12, ipady=3)

        # Time
        lbl_time = Label(entry_frame, text="Time:", font=("Calibri", 13, "bold"), bg="white")
        lbl_time.grid(row=2, column=0, padx=10, pady=12, sticky=W)
        entry_time = Entry(entry_frame, textvariable=self.var_atten_time, font=("Calibri", 13), bd=1, relief=SOLID, width=18)
        entry_time.grid(row=2, column=1, padx=5, pady=12, ipady=3)

        # Date
        lbl_date = Label(entry_frame, text="Date:", font=("Calibri", 13, "bold"), bg="white")
        lbl_date.grid(row=2, column=2, padx=10, pady=12, sticky=W)
        entry_date = Entry(entry_frame, textvariable=self.var_atten_date, font=("Calibri", 13), bd=1, relief=SOLID, width=18)
        entry_date.grid(row=2, column=3, padx=5, pady=12, ipady=3)

        # Attendance Status
        lbl_status = Label(entry_frame, text="Attendance Status:", font=("Calibri", 13, "bold"), bg="white")
        lbl_status.grid(row=3, column=0, padx=10, pady=12, sticky=W)
        
        combo_status = ttk.Combobox(entry_frame, textvariable=self.var_atten_status, font=("Calibri", 13), width=16, state="readonly")
        combo_status["values"] = ("Status", "Present", "Absent")
        combo_status.current(0)
        combo_status.grid(row=3, column=1, padx=5, pady=12)

        # Buttons Frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=480, width=690, height=50)

        # Configure grid columns and rows to expand equally
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)
        btn_frame.grid_columnconfigure(3, weight=1)
        btn_frame.grid_rowconfigure(0, weight=1)

        # Import CSV Button
        import_btn = Button(btn_frame, text="Import csv", command=self.import_csv, font=("Calibri", 12, "bold"), bg="blue", fg="white", cursor="hand2")
        import_btn.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

        # Export CSV Button
        export_btn = Button(btn_frame, text="Export csv", command=self.export_csv, font=("Calibri", 12, "bold"), bg="blue", fg="white", cursor="hand2")
        export_btn.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")

        # Update Button
        update_btn = Button(btn_frame, text="Update", command=self.update_attendance, font=("Calibri", 12, "bold"), bg="blue", fg="white", cursor="hand2")
        update_btn.grid(row=0, column=2, padx=2, pady=2, sticky="nsew")

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_fields, font=("Calibri", 12, "bold"), bg="blue", fg="white", cursor="hand2")
        reset_btn.grid(row=0, column=3, padx=2, pady=2, sticky="nsew")

        # Right Frame - Student Details
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", 
                                 font=("Calibri", 12, "bold"), bg="white", fg="crimson")
        right_frame.place(x=715, y=5, width=705, height=570)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=690, height=530)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Treeview Table
        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Table Headings
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        # Column Widths
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=80)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=80)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

        # Load attendance data
        self.fetch_attendance()

    # ============ Fetch Attendance Data from CSV ============
    def fetch_attendance(self):
        # Clear existing data
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        
        try:
            with open("attendance.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 6:  # Ensure row has enough data
                        # CSV format: id, roll, name, department, date, time, status
                        self.AttendanceReportTable.insert("", END, values=row)
        except FileNotFoundError:
            pass

    # ============ Get Cursor (Select Row) ============
    def get_cursor(self, event):
        cursor_focus = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        data = content["values"]
        
        if data:
            self.var_atten_id.set(data[0])
            self.var_atten_roll.set(data[1])
            self.var_atten_name.set(data[2])
            self.var_atten_dep.set(data[3])
            self.var_atten_time.set(data[4] if len(data) > 4 else "")
            self.var_atten_date.set(data[5] if len(data) > 5 else "")
            self.var_atten_status.set(data[6] if len(data) > 6 else "Status")

    # ============ Import CSV ============
    def import_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")], parent=self.root)
        if file_path:
            try:
                # Read content first
                with open(file_path, "r") as source:
                    content = source.read()
                
                # Then write to destination
                with open("attendance.csv", "w") as dest:
                    dest.write(content)
                    
                messagebox.showinfo("Success", "CSV file imported successfully!", parent=self.root)
                self.fetch_attendance()
            except Exception as e:
                messagebox.showerror("Error", f"Error importing CSV: {e}", parent=self.root)

    # ============ Export CSV ============
    def export_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], parent=self.root)
        if file_path:
            try:
                with open("attendance.csv", "r") as source:
                    with open(file_path, "w") as dest:
                        dest.write(source.read())
                messagebox.showinfo("Success", "CSV file exported successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error exporting CSV: {e}", parent=self.root)

    # ============ Update Attendance ============
    def update_attendance(self):
        if self.var_atten_id.get() == "":
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return
        
        try:
            # Read all data
            rows = []
            with open("attendance.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 1 and str(row[0]) == str(self.var_atten_id.get()):
                        # Update this row
                        rows.append([self.var_atten_id.get(), self.var_atten_roll.get(), self.var_atten_name.get(),
                                     self.var_atten_dep.get(), self.var_atten_time.get(), self.var_atten_date.get(),
                                     self.var_atten_status.get()])
                    else:
                        rows.append(row)
            
            # Write back
            with open("attendance.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            
            messagebox.showinfo("Success", "Attendance updated successfully!", parent=self.root)
            self.fetch_attendance()
        except Exception as e:
            messagebox.showerror("Error", f"Error updating attendance: {e}", parent=self.root)

    # ============ Reset Fields ============
    def reset_fields(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("Status")

    # Go to Home (close current window)
    def go_home(self):
        self.root.destroy()

    # Exit entire application
    def exit_app(self):
        sys.exit()





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()