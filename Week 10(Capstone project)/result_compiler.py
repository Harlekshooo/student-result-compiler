


import os
import csv


students = [] # This stores all the student data

def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


#OPTION 1: ---ADD STUDENTS---
def add_students():
    while True:
        student_name = input("Student name: ")
        if student_name == "": # If the {student_name} is empty, it takes you back to the beginning of the loop to input a valid {student_name}.
            print(f"Please enter a name!!!")
            continue
        break

    while True:
        number_of_subjects = int(input("Number of subjects: "))
        if number_of_subjects <= 0: # If the {number_of_subjects} is < or = 0, it takes you back to the beginning of the loop to input a valid {number_of_subjects}.
            print("Pease enter a valid number of subjects you took!!!")
            continue
        break

    scores = [] # This stores all the student scores.
    
    for i in range(number_of_subjects): # It uses the {number_of_subjects} to know how many score fields it is going to bring out
        while True:
            score = int(input(f"Score {i + 1}: "))
            if score < 0 or score > 100: # If the score is < 0 or > 100, it takes you back to the beginning of the loop to input a valid score.
                print("SCORE MUST BE BETWEEN 0 - 100!!!")
                continue
            scores.append(score)
            break

    average = sum(scores) / len(scores)
    average = round(average, 2) # rounds the average off to 2 decimal places.
    grade = calculate_grade(average) # obtains the grade using the calculate_grade function above and the average as its argument.

    student = {
        "name": student_name,
        "average": average,
        "grade": grade
    }

    # print(f"{student_name}: {number_of_subjects}")
    students.append(student)
    # print(scores)
    # print(average)
    # print(grade)
    # print(students)
    print(f"{student_name} - {average} - {grade}")


#OPTION 2: ---CLASS SUMMARY---
def class_summary():
    student_averages = []
    for student in students:
        # print(student["average"])
        student_averages.append(student["average"])
        # print(student_averages)
    
    highest_average = max(student_averages)
    # print(highest_average)
    lowest_average = min(student_averages)
    # print(lowest_average)
    
    class_average = sum(student_averages)/len(student_averages)
    real_class_average = round(class_average, 2)


    print("---Class Summary---")
    print(f"Class average: {real_class_average}")
    for student in students:
        if highest_average == student["average"]:
            print(f"Highest: {student['name']} ({highest_average})")
        if lowest_average == student["average"]:
            print(f"Lowest: {student['name']} ({lowest_average})")
            



#OPTION 3: ---SAVE RESULTS---
def save_results():
        
    filename = "results.csv"

    if os.path.exists(filename):
        print(f"{filename} already exists!!!")

        choose = input("Overwrite the existing file? (yes/no): ").lower()

        if choose != "yes":
            print("Save cancelled. The existing results are being kept✅.")
    
    headers = ["name", "average", "grade"] # The header of the student data.

    with open("results.csv", "w", newline='') as f:#newline helps prevent blank rows from being created
        writer = csv.DictWriter(f, fieldnames=headers) # This registers the column headers and links the writer to the {filename}
        writer.writeheader() # This writes the top header directly into the file
        writer.writerows(students)# This fills in all the student data into the rows

    with open("results.csv") as f:
        print(f.read()) # Helps you to see or read the changes that have been made to the file

    if students == []:
        print("PLEASE INPUT A RESULT TO SAVE!!!")
        return


# ---MAIN CONTAINER---
def container():
    while True:
        print("===Student Result Processor===")
        print("1. Add Students")
        print("2. Class summary")
        print("3. Save results")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            add_students()
            continue
        elif choice == 2:
            class_summary()
            continue
        elif choice == 3:
            save_results()
            continue
        elif choice == 4:
            print("Alright. Bye for now👋!!!")
            continue
        else:
            print("⚠ ⚠ Such option does not exist!!!")
            continue

        break


container()
