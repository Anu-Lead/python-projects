# Student Grade Calculation Algorithm
"""Step 1: Instruct the student to enter grade of each subject one after the other
Step 2: Store the grades in a collections of grades
Step 3: Loop through the collections of grades and assign/store each (grade index) to a subject variable
Step 4: print each subject grade
Step 5: Find the maximum of all grade score and divide by number of subject to determine the average
Step 6: Assign the average to a letter grade A/B/C anyone it falls to
Step 7: Print all grades including the average
"""

user_input_score_grades = []
for user_input_score_grades in range(1):
    (input(
        "WELCOME TO YOUR GRADUATE SCHOOL GRADE CHECKER!\n==================================================\nEnter the Financial Management Score:\n"))
    input("Enter the Professional Communication Score:\n")
    input("Enter the Technology Score:\n")
    input("Enter the Digital Leadership Score:\n")
    input("Enter the Operation and Management Score:\n")
    input("Enter the Ethics, Law and Regulations Score:\n")
    input("Enter the Information Technology Score:\n")
    input("Enter the Artificial Intelligence and Data Analytics Score:\n")
    input("Enter the Financial Technology Score:\n")
    input("Enter the Business Ethics Score:\n")
    input("Enter the International Policy Score:\n")

user_input_score_grades = {Maths: Score for Maths, Score in user_input_score_grades}

for stu_grades in user_input_score_grades:
    user_input_score_grades.values()


def calculate_grade(each_grade):
    global user_input_score_grades
    if each_grade > user_input_score_grades:
        return each_grade
    else:
        max(user_input_score_grades)


print(user_input_score_grades)
