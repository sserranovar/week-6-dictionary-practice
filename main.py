# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
#print(len(students))
#print(students[0]["Combo,Name"])
#print(students[1]["Combo,Name"])
#print(students[0]['Email'][0])
#print(students[1]['Email'][0])
#print(students[0]["CPSID"])
#print(students[1]["FName"])
#print(students[1]["MName"])
#print(students[1]["LName"])
#print(students[1]['Email'])
#'for loops' allow us to go through data and perform a function
for students in students :
  print(students["Combo,Name"])
  print(students["CPSID"])
  print(students['Email'][0])
  print(students['Email'][1])
  print("_"*25)