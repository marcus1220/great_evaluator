import csv

#opening the csv file
with open("data.csv","r") as file:

    # creat a csv reader
    reader = csv.reader(file)

    # init a dictionary to keep the great for each assignment
    grades = {}

    # iterating over eash row in the csv file
    for row in reader:

        # excting the student Id assignment name and grade
        student_id, assignment_name, grade = row

        # printing data and file
        print(student_id, assignment_name, grade)
        
        # if this assignment have't been added to the grade dictionary, then add it into.
        if assignment_name not in grade:
            grades[assignment_name] = []

        # add grade to the list of grade for this assignment
        grades[assignment_name].append(grade) #we may need (int(grade))