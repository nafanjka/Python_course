student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
#list(dict) has method values and keys

print(student_grades.values())
print(student_grades.keys())

student_sum = sum(student_grades.values())
print(student_sum)

list_length = len(student_grades.values())
student_avg = student_sum / list_length
print(student_avg)

