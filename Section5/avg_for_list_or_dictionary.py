def avg(value):
    if isinstance(value, dict):
        the_avg = sum(value.values()) / len(value)
    else:
        the_avg = sum(value) / len(value)

    return the_avg

student_grades_list = [9.1, 8.8, 10.5]   
student_grades_dict = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

print(avg(student_grades_list))
print(avg(student_grades_dict))