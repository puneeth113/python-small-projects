# -*- coding: utf-8 -*-
"""
Creating a chatbot that can handle student attendance.
"""
import random 
import pandas as pd


student_name = []
student_attendance = []

def greeting():
    greet = ["hello", "hey", "hai", "hi"]
    print(random.choice(greet))

def get_student_names():
    print("Clai: Enter how many students are there in the class.")
    count = int(input("You: "))
    
    for i in range(count):
        print(f"Clai: Name of student with roll number {i+1}:\n ")
        name = input("You: ")
        student_name.append(name)
    
    return student_name


def record_attendance():
    for student in student_name:
        print(f"Clai: Type 'p' if {student} is present, else type 'a'.\n")
        pa = input("You: ").lower()
        pa = 'p' if pa == 'p' or pa == 'yes' else 'a'
        student_attendance.append(pa)
    
    return student_attendance


# Collecting the student name 

list_student_name = get_student_names()

# Record attendance attenadance 

list_student_attendance = record_attendance()

# Combine the lists into a dictionary

student_attendance_detail = {
    "name": list_student_name,
    "attendance": list_student_attendance
}

#convarting to data_frame 

df =pd.DataFrame(student_attendance_detail)


