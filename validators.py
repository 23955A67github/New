from tkinter import messagebox

def validate_fields(field, field_type):
    if field_type == 'alpha' and not field.isalpha():
        messagebox.showwarning("Invalid Input", "Only letters are allowed")
        return False
    elif field_type == 'numeric' and not field.isdigit():
        messagebox.showwarning("Invalid Input", "Only numbers are allowed")
        return False
    elif field_type == 'alphanumeric' and not field.isalnum():
        messagebox.showwarning("Invalid Input", "Only alphanumeric values are allowed")
        return False
    return True
