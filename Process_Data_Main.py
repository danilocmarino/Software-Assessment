#..............................................
# ........Project : Software Assessment...............
#..........Name : Danilo Cunha Marino...............
#...............08/05/2025....................

import Calculation_Functions
#....This command import a calculation from Calculation_Functions.py.
 
import csv
#....This command import all details from csv to be built.

Students = []
#......This command starts the student list.

try:
    #.....reading csv file.
    with open('Students1.csv', 'r') as file:
            reader = csv.reader(file) #..it craates a csv reader.
            header = next(reader) #... it reads the header.
            for row in reader:#... it makes the names working throught a row.
                name, geography, history, portuguese, english, math = row #... subjects which needs to be calculated.
                average = Calculation_Functions.calculate_average([int(geography), int(history), int(portuguese), int(english), int(math)])#calculates the average of these subjects.
                grade = Calculation_Functions.assign_grade(average) #... knowing the average. it works giving the grade
                Students.append([name, geography, history, portuguese, english, math, average, grade]) #... this command works using each students, average and grade.
     
except FileNotFoundError:
     print(f"Error: Students1.csv not found.") #.... this is in case of the file is not found. 

with open('Student_Result.csv', 'w', newline='') as file: #...this command write everything on the result file.
     writer = csv.writer(file)
     writer.writerow(["Name", "Geography", "History", "Portuguese", "English", "Math", "Average", "Grade"])
     writer.writerows(Students)

print("Results saved to student_results.csv")          
