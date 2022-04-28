monday_temperatures = [9.1, 8.8, 7.5]

for temperature in monday_temperatures:
    print(round(temperature))

for letter in 'hello':
    print(letter.title())    

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for every_color in colors:
    if type(every_color) == int and every_color > 50:
        print(every_color)   

def celsius_to_kelvin(cels):
    return cels + 273.15
 
for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))   

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}    

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)    

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}") 

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for number in phone_numbers.values():
    print(str.replace(number, '+', '00'))       

