import mysql.connector
from tkinter import messagebox

def save(enrollment, rollno, firstname, lastname, dob, age, gender, contact, email, course):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="password", database="Student_form")
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                Enrollment_no VARCHAR(20) PRIMARY KEY NOT NULL,
                Roll_no VARCHAR(10) NOT NULL UNIQUE,
                First_name CHAR(50) NOT NULL,
                Middle_name CHAR(50),
                Last_name CHAR(50) NOT NULL,
                Birthdate DATE NOT NULL,
                Age INT NOT NULL,
                Gender CHAR(10) NOT NULL,
                Contact INT NOT NULL UNIQUE,
                Email VARCHAR(50) NOT NULL UNIQUE,
                Course VARCHAR(30) NOT NULL
            )
        """)
        query = """
            INSERT INTO Student (Enrollment_no, Roll_no, First_name, Middle_name, Last_name, Birthdate, Age, Gender, Contact, Email, Course)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (enrollment.get(), rollno.get(), firstname.get(), "", lastname.get(), dob.get(), age.get(), gender.get(), contact.get(), email.get(), course.get())
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data saved successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    finally:
        if db:
            db.close()
