from tkinter import *
from tkinter import ttk
import pymysql  # pip install pymsql
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("Calibri", 40, "bold"),
                      bg="yellow", fg="blue")
        title.pack(side=TOP, fill=X)

        # **********All_Variables*********
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # **************************Manage_Frame***********************
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="green")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="Manage Students", bg="green", fg="white", font=("Calibri", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("Calibri", 15, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.name_var, font=("Calibri", 15, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("Calibri", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("Calibri", 13, "bold"),
                                    state='readonly')
        combo_Gender['values'] = ("male", "female", "other")
        combo_Gender.grid(row=4, column=1, pady=10, padx=20)

        lbl_Contact = Label(Manage_Frame, text="Contact No.", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("Calibri", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="Date of Birth", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable=self.dob_var, font=("Calibri", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=30, height=4, font=("Calibri", 10, "bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # *****Button_Frame******
        Btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="green")
        Btn_Frame.place(x=10, y=530, width=430)

        AddBtn = Button(Btn_Frame, text="Add", width=10, command=self.add_students).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        UpdateBtn = Button(Btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=10)
        DeleteBtn = Button(Btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                              pady=10)
        ClearBtn = Button(Btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # **************************Detail_Frame************************

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="green")
        Detail_Frame.place(x=500, y=100, width=800, height=600)

        lbl_search = Label(Detail_Frame, text="Search By", bg="green", fg="white", font=("Calibri", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("Calibri", 13, "bold"),
                                    state='readonly')
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, font=("Calibri", 15, "bold"), bd=5,
                           relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        SearchBtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,
                                                                                                         column=3,
                                                                                                         padx=10,
                                                                                                         pady=10)
        ShowAllBtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0,
                                                                                                           column=4,
                                                                                                           padx=10,
                                                                                                           pady=10)

        # ************Table_Frame*****************

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="green")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame, columns=(
        "Roll No", "Name", "Email", "Gender", "Contact No.", "DOB", "Address"), yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll No", text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact No.", text="Contact No.")
        self.Student_table.heading("DOB", text="DOB")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("Roll No", width=70)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Email", width=150)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact No.", width=100)
        self.Student_table.column("DOB", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)

        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # For adding the details in the table
    # And database connectivity with phpMyAdmin
    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or self.gender_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "":
            messagebox.showerror("Error", "All fields are required !!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_Address.get('1.0', END)
                                                                              ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted successfully!!")

    # For fetching the all record from the table
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    # Making a function for clear the records
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    # Making a function for updating the records
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_Address.get('1.0', END),
            self.Roll_No_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    # Making a function for deleting the records
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    # Making a function for search any record
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE  '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()  # main loop closed