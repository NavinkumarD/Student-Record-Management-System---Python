import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('student_record_system.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY, name TEXT, roll_no INTEGER, email TEXT, phone TEXT, address TEXT)''')
conn.commit()

class StudentRecordSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record System")
      
        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
      
        # Create labels and entry fields
        tk.Label(self.frame1, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.grid(row=0, column=1)
        tk.Label(self.frame1, text="Roll No:").grid(row=1, column=0)
        self.roll_no_entry = tk.Entry(self.frame1)
        self.roll_no_entry.grid(row=1, column=1)
        tk.Label(self.frame1, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.frame1)
        self.email_entry.grid(row=2, column=1)
        tk.Label(self.frame1, text="Phone:").grid(row=3, column=0)
        self.phone_entry = tk.Entry(self.frame1)
        self.phone_entry.grid(row=3, column=1)
        tk.Label(self.frame1, text="Address:").grid(row=4, column=0)
        self.address_entry = tk.Entry(self.frame1)
        self.address_entry.grid(row=4, column=1)

        # Create buttons
        tk.Button(self.frame2, text="Add Student", command=self.add_student).grid(row=0, column=0)
        tk.Button(self.frame2, text="Update Student", command=self.update_student).grid(row=0, column=1)
        tk.Button(self.frame2, text="Delete Student", command=self.delete_student).grid(row=0, column=2)
        tk.Button(self.frame2, text="View Students", command=self.view_students).grid(row=0, column=3)

    def add_student(self):
        # Get values from entry fields
        name = self.name_entry.get()
        roll_no = self.roll_no_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        # Insert into database
        cursor.execute("INSERT INTO students (name, roll_no, email, phone, address) VALUES (?,?,?,?,?)",
                       (name, roll_no, email, phone, address))
        conn.commit()

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.roll_no_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
      
        messagebox.showinfo("Success", "Student added successfully!")

    def update_student(self):
        # Get values from entry fields
        name = self.name_entry.get()
        roll_no = self.roll_no_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        # Update in database
        cursor.execute("UPDATE students SET name=?, email=?, phone=?, address=? WHERE roll_no=?",
                       (name, email, phone, address, roll_no))
        conn.commit()

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.roll_no_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Student updated successfully!")

    def delete_student(self):
        # Get roll no from entry field
        roll_no = self.roll_no_entry.get()

        # Delete from database
        cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
        conn.commit()

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.roll_no_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Student deleted successfully!")

    def view_students(self):
        # Create a new window to display students
        view_window = tk.Toplevel(self.root)
        view_window.title("View Students")

        # Create a treeview to display students
        treeview = tk.ttk.Treeview(view_window)
        treeview.pack()

        # Define columns
        treeview["columns"] = ("name", "roll_no", "email", "phone", "address")

        # Format columns
        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.column("name", anchor=tk.W, width=100)
        treeview.column("roll_no", anchor=tk.W, width=100)
        treeview.column("email", anchor=tk.W, width=150)
        treeview.column("phone", anchor=tk.W, width=100)
        treeview.column("address", anchor=tk.W, width=200)

        # Create headings
        treeview.heading("#0", text="", anchor=tk.W)
        treeview.heading("name", text="Name", anchor=tk.W)
        treeview.heading("roll_no", text="Roll No", anchor=tk.W)
        treeview.heading("email", text="Email", anchor=tk.W)
        treeview.heading("phone", text="Phone", anchor=tk.W)
        treeview.heading("address", text="Address", anchor=tk.W)

        # Fetch students from database
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        # Insert students into treeview
        for student in students:
            treeview.insert("", tk.END, values=student[1:])

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordSystem(root)
    root.mainloop()
