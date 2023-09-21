# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:50:30 2023

@author: Ahsan
"""


student_records = {}

def add_student():
    reg_number = input("Enter Registration Number: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    gender = input("Enter Gender: ")
    
   
    student_data = {
        "Name": name,
        "Email": email,
        "Gender": gender
    }
    

    student_records[reg_number] = student_data
    print("Student added successfully!")

def view_student(reg_number):
    student_data = student_records.get(reg_number)
    if student_data:
        print("Registration Number:", reg_number)
        print("Name:", student_data["Name"])
        print("Email:", student_data["Email"])
        print("Gender:", student_data["Gender"])
    else:
        print("Student not found!")

def update_student(reg_number):
    if reg_number in student_records:
        print("Enter Registration Number to Update:", reg_number)
        name = input("Enter New Name : ")
        email = input("Enter New Email : ")
        gender = input("Enter New Gender : ")
        
        student_data = student_records[reg_number]
        
        if name:
            student_data["Name"] = name
        if email:
            student_data["Email"] = email
        if gender:
            student_data["Gender"] = gender
        
        print("Student information updated successfully!")
    else:
        print("Student not found!")

def delete_student(reg_number):
    if reg_number in student_records:
        del student_records[reg_number]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            reg_number = input("Enter Registration Number to view: ")
            view_student(reg_number)
        elif choice == "3":
            reg_number = input("Enter Registration Number to update: ")
            update_student(reg_number)
        elif choice == "4":
            reg_number = input("Enter Registration Number to delete: ")
            delete_student(reg_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
