from tkinter import *
from PIL import ImageTk
from tkcalendar import *
from tkinter import messagebox
from helpers import pick_date, clear
from database import save
from validators import validate_fields

# Initialize main window
windows = Tk()
windows.title("Student Registration Form")
windows.geometry('700x750+200+10')
windows.resizable(0, 0)

# Load background image
backgroundimage = ImageTk.PhotoImage(file='assets/p1.jpg')
bglabel = Label(windows, image=backgroundimage)
bglabel.place(x=0, y=0)

# Define Variables
enrollment = StringVar()
rollno = StringVar()
firstname = StringVar()
middlename = StringVar()
lastname = StringVar()
dob = StringVar()
age = IntVar()
gender = StringVar()
contact = StringVar()
email = StringVar()
course = StringVar()
OM = StringVar()

course_options = [
    'MBA-MS(5 Yrs.)', 'MBA-TA(5 Yrs.)', 'MCA(5 Yrs.)', 'MTECH(5 Yrs)',
    'BCOM(Hons.)(3 Yrs.)', 'MBA-APR(2 Yrs.)', 'MBA-ESHIP(2 Yrs)',
    'MBA-MS(2 Yrs.)', 'MBA-TA(2 Yrs.)'
]
OM.set('Select Course')

# GUI Setup
frame = Frame(windows, width=500, height=600, bd=8, bg='#eaeafa')
frame.place(x=100, y=100)

heading = Label(windows, text='Student Registration Form', font=('Calibre', 20, 'bold', 'underline'), bg='#eaeafa')
heading.place(x=170, y=10)

# Form Fields
form_fields = [
    ('Enrollment No.:', enrollment, 10),
    ('Roll No.:', rollno, 50),
    ('First Name:', firstname, 90),
    ('Middle Name:', middlename, 130),
    ('Last Name:', lastname, 170),
    ('Date of Birth:', dob, 210, pick_date),
    ('Age:', age, 250),
    ('Contact:', contact, 390),
    ('Email:', email, 430),
]

for label, variable, y_pos, *callback in form_fields:
    Label(frame, text=label, font=('Calibre', 15, 'bold'), bg='#eaeafa').place(x=10, y=y_pos)
    entry = Entry(frame, width=40, borderwidth=2, textvariable=variable)
    entry.place(x=200, y=y_pos)
    if callback:
        entry.bind("<1>", callback[0])

# Gender Selection
Label(frame, text='Gender:', font=('Calibre', 15, 'bold'), bg='#eaeafa').place(x=10, y=290)
gender.set(0)
gender_options = ['Male', 'Female', 'Other']
for idx, option in enumerate(gender_options, start=1):
    Radiobutton(frame, text=option, variable=gender, value=option, font='Tahoma 13 bold', bg='#eaeafa').place(x=200, y=290 + 30 * (idx - 1))

# Course Dropdown
Label(frame, text='Course:', font=('Calibre', 15, 'bold'), bg='#eaeafa').place(x=10, y=470)
OptionMenu(frame, OM, *course_options).place(x=200, y=470)

# Buttons
Button(frame, text='Save', width=8, borderwidth=5, height=1, font=('calibre', 13, 'bold'), cursor='hand2', command=lambda: save(enrollment, rollno, firstname, lastname, dob, age, gender, contact, email, OM)).place(x=100, y=545)
Button(frame, text='Clear', width=8, borderwidth=5, height=1, font=('calibre', 13, 'bold'), cursor='hand2', command=clear).place(x=250, y=545)

windows.mainloop()
