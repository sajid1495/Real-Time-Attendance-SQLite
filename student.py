from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import sqlite3
from database import get_connection, init_database
import cv2
import sys


class Student:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')  # Full screen
        self.root.title("Face Recognition System")

        #=======variables========
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search = StringVar()



        # Background Image
        img = Image.open(r"images\_bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_image, text="STUDENTS DETAILS", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
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

        #frame
        main_frame = Frame(bg_image, bd=2, bg="white")
        main_frame.place(x=15, y=80, width=1500, height=680) 


        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=660)

        img_left = Image.open(r"images\student_details_banner.png")  
        img_left = img_left.resize((730, 150), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        lbl_img_left = Label(Left_frame, image=self.photoimg_left)
        lbl_img_left.place(x=5, y=0, width=720, height=150)

        #current course frame
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("Calibri", 12, "bold"))
        current_course_frame.place(x=5, y=160, width=720, height=120)


        #department combo box
        dept_label = Label(current_course_frame, text="Department:", font=("Calibri", 12, "bold"), bg="white")
        dept_label.grid(row=0, column=0, padx=5, sticky=W)

        dept_combo = ttk.Combobox(current_course_frame,  textvariable=self.var_dept, font=("Calibri", 12, "bold"), state="readonly", width=20)
        dept_combo["values"] = ("Select Department", "CSE", "EEE", "Civil", "Mechanical", "Chemical")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #course combo box
        course_label = Label(current_course_frame, text="Course:", font=("Calibri", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=5, sticky=W)       

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("Calibri", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "B.Sc", "M.Sc", "PhD")
        course_combo.current(0) 
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        #year combo box
        year_label = Label(current_course_frame, text="Year:", font=("Calibri", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=5, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Calibri", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27", "2027-28")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        #semester combo box
        sem_label = Label(current_course_frame, text="Semester:", font=("Calibri", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=5, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("Calibri", 12, "bold"), state="readonly", width=20)
        sem_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        #student information
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("Calibri", 12, "bold"))
        student_frame.place(x=5, y=290, width=720, height=340)

        #student id
        studentID_label = Label(student_frame, text="Student ID:", font=("Calibri", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentID_entry = ttk.Entry(student_frame, textvariable=self.var_std_id, width=20, font=("Calibri", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #student name
        studentName_label = Label(student_frame, text="Student Name:", font=("Calibri", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        studentName_entry = ttk.Entry(student_frame, textvariable=self.var_std_name, width=20, font=("Calibri", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        #Section
        class_div_label = Label(student_frame, text="Section:", font=("Calibri", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(student_frame, textvariable=self.var_div, font=("Calibri", 12, "bold"), state="readonly", width=18)
        class_div_combo["values"] = ("Select Section", "A", "B", "C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #roll no
        roll_no_label = Label(student_frame, text="Roll No:", font=("Calibri", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(student_frame, textvariable=self.var_roll, width=20, font=("Calibri", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        #gender
        gender_label = Label(student_frame, text="Gender:", font=("Calibri", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(student_frame, textvariable=self.var_gender, font=("Calibri", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        #dob
        dob_label = Label(student_frame, text="DOB:", font=("Calibri", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        dob_entry = ttk.Entry(student_frame, textvariable=self.var_dob, width=20, font=("Calibri", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        #email
        email_label = Label(student_frame, text="Email:", font=("Calibri", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        email_entry = ttk.Entry(student_frame, textvariable=self.var_email, width=20, font=("Calibri", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #phone no
        phone_label = Label(student_frame, text="Phone No:", font=("Calibri", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        phone_entry = ttk.Entry(student_frame, textvariable=self.var_phone, width=20, font=("Calibri", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        #address
        address_label = Label(student_frame, text="Address:", font=("Calibri", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        address_entry = ttk.Entry(student_frame, textvariable=self.var_address, width=20, font=("Calibri", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        #teacher name
        teacher_label = Label(student_frame, text="Teacher Name:", font=("Calibri", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        teacher_entry = ttk.Entry(student_frame, textvariable=self.var_teacher, width=20, font=("Calibri", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        #radio buttons
        self.var_radio1 = StringVar()
        self.var_radio1.set("Yes")
        radiobtn1 = Radiobutton(student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes", font=("Calibri", 12, "bold"), bg="white")
        radiobtn1.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        radiobtn2 = Radiobutton(student_frame, variable=self.var_radio1, text="No Photo Sample", value="No", font=("Calibri", 12, "bold"), bg="white")
        radiobtn2.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        #buttons frame
        btn_frame = Frame(student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=710, height=68)

        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Take Photo Sample", width=43, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0, columnspan=2, padx=0, pady=1, sticky=W)
        update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=43, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=2, columnspan=2, padx=0, pady=1, sticky=E)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=21, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        save_btn.grid(row=1, column=0, padx=0, pady=1)
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=21, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        update_btn.grid(row=1, column=1, padx=0, pady=1)
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=21, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=1, column=2, padx=0, pady=1)
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=21, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=1, column=3, padx=0, pady=1)









        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=660)

        img_right = Image.open(r"images\student_details_banner.png")
        img_right = img_right.resize((730, 150), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        lbl_img_right = Label(Right_frame, image=self.photoimg_right)
        lbl_img_right.place(x=5, y=0, width=720, height=150)


        #search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Calibri", 12, "bold"))
        search_frame.place(x=5, y=160, width=720, height=70)

        search_label = Label(search_frame, text="Search By:", font=("Calibri", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search, font=("Calibri", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("Calibri", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4, pady=5)

        showAll_btn = Button(search_frame, text="Show All", width=12, font=("Calibri", 11, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4, pady=5)   


        #table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=240, width=720, height=390)

        # Style for thicker scrollbar
        style = ttk.Style()
        style.configure("Horizontal.TScrollbar", arrowsize=15)
        style.configure("Vertical.TScrollbar", arrowsize=15)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL, width=15)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL, width=15)

        self.student_table = ttk.Treeview(table_frame, columns=("id", "roll", "name", "div", "dept", "course", "year", "sem", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings" 

        self.student_table.column("id", width=100, anchor=CENTER)
        self.student_table.column("roll", width=100, anchor=CENTER)
        self.student_table.column("name", width=100, anchor=CENTER)
        self.student_table.column("div", width=100, anchor=CENTER)
        self.student_table.column("dept", width=100, anchor=CENTER)
        self.student_table.column("course", width=100, anchor=CENTER)
        self.student_table.column("year", width=100,anchor=CENTER)
        self.student_table.column("sem", width=100, anchor=CENTER)
        self.student_table.column("gender", width=100, anchor=CENTER)
        self.student_table.column("dob", width=100, anchor=CENTER)
        self.student_table.column("email", width=150, anchor=CENTER)
        self.student_table.column("phone", width=100, anchor=CENTER)
        self.student_table.column("address", width=150, anchor=CENTER)
        self.student_table.column("teacher", width=100, anchor=CENTER)
        self.student_table.column("photo", width=150, anchor=CENTER)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #=======add functions=======
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return
        conn = None
        my_cursor = None
        try:
            conn = get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO student VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
            ))
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
        finally:
            if my_cursor is not None:
                try:
                    my_cursor.close()
                except:
                    pass
            if conn is not None:
                try:
                    conn.close()
                except:
                    pass

    #=========fetch data=========
    def fetch_data(self):
        try:
            conn = get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            self.student_table.delete(*self.student_table.get_children())
            if len(data) != 0:
                for i in data:
                    # Always use the string as-is to preserve leading zeros
                    id_str = str(i[4])
                    roll_str = str(i[7])
                    reordered = (
                        id_str,  # id (preserve leading zeros)
                        roll_str,  # roll
                        i[5],  # name
                        i[6],  # div
                        i[0],  # dept
                        i[1],  # course
                        i[2],  # year
                        i[3],  # sem
                        i[8],  # gender
                        i[9],  # dob
                        i[10], # email
                        i[11], # phone
                        i[12], # address
                        i[13], # teacher
                        i[14], # photo
                    )
                    self.student_table.insert("", END, values=reordered)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    #=====get cursor=====
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if not data:
            return
        # data order: id, roll, name, div, dept, course, year, sem, gender, dob, email, phone, address, teacher, photo
        # Always set as string to preserve original formatting (including leading zeros if present)
        self.var_std_id.set(str(data[0]))
        self.var_roll.set(str(data[1]))
        self.var_std_name.set(data[2])
        self.var_div.set(data[3])
        self.var_dept.set(data[4])
        self.var_course.set(data[5])
        self.var_year.set(data[6])
        self.var_semester.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])



    #========update function========
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    conn = get_connection()
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET Dept=?, Course=?, Year=?, Semester=?, Name=?, Division=?, Roll=?, Gender=?, Dob=?, Email=?, Phone=?, Address=?, Teacher=?, PhotoSample=? WHERE Student_id=?", (
                                                                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll.get(),    
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                                ))
                    conn.commit()
                    my_cursor.close()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    if not Update:
                        return  
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

        

    #=======delete function=======
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
            return
        try:
            delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
            if not delete:
                return
            conn = get_connection()
            my_cursor = conn.cursor()
            sql = "DELETE FROM student WHERE Student_id=?"
            val = (self.var_std_id.get(),)  # Always use string, preserves leading zeros
            my_cursor.execute(sql, val)
            deleted_count = my_cursor.rowcount
            conn.commit()
            my_cursor.close()
            conn.close()
            self.fetch_data()
            if deleted_count == 0:
                messagebox.showwarning("Delete", "No student found with this ID. It may be due to leading zeros mismatch.", parent=self.root)
            else:
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #========reset function========
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("Yes")


    #========generate data set or take photo sample=======
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = get_connection()
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE student SET Dept=?, Course=?, Year=?, Semester=?, Name=?, Division=?, Roll=?, Gender=?, Dob=?, Email=?, Phone=?, Address=?, Teacher=?, PhotoSample=? WHERE Student_id=?", (
                                                                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll.get(),        
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                                ))
                conn.commit()
                my_cursor.close()
                conn.close()
                self.fetch_data()
                
                # Save student ID before resetting
                student_id = self.var_std_id.get()
                
                #========load predefined data on face frontals from opencv========
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor = 1.3
                    #minimum neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(student_id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                # Only reset the photo sample radio button, not all fields
                self.var_radio1.set("Yes")
                messagebox.showinfo("Result", "Generating data set completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # Go to Home (close current window)
    def go_home(self):
        self.root.destroy()

    # Exit entire application
    def exit_app(self):
        sys.exit()
            












if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()