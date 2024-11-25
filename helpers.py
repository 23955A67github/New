from tkinter import Toplevel, Button, Entry, END
from tkcalendar import Calendar

def pick_date(event):
    global cal, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Choose your Date of Birth")
    date_window.geometry('250x220+590+370')
    cal = Calendar(date_window, selectmode="day", date_pattern="y/mm/dd")
    cal.place(x=0, y=0)
    Button(date_window, text="Submit", command=lambda: grab_date(event.widget)).place(x=80, y=190)

def grab_date(entry):
    entry.delete(0, END)
    entry.insert(0, cal.get_date())
    date_window.destroy()

def clear(entries):
    for entry in entries:
        entry.delete(0, END)
