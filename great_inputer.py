import csv

# prompt the user the enter the student information
student_id = input("what is student ID?")
student_name = input("what is student name?")
student_major = input("what is student major?")

# creater a dictionary to keep the student information
student = {"ID":student_id,"Name":student_name,"Major":student_major}

# writing the information to the csv file
with open("student.csv", "a",newline = "")as file:
    writer = csv.DictWriter(file,fieldnames=["ID", "Name", "Major"])
    writer.writerow(student)

print("student information have been saved into csv file")