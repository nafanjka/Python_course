from turtle import title


def temperature(value):
    if value > 7:
        the_temp = "Warm"
    else:
        the_temp = "Cold"
        
    return the_temp

user_input = float(input("Enter temperature:"))

print(temperature(user_input))

# 3 ways how to work with string
user_input = input("Enter your Name: ")
message = "Hello " + user_input + "!"
message = "Hello %s!" % user_input
message = f"Hello {user_input}!"
print(message)

# few variables
name = input("Enter your Name: ")
surname = input("Enter you Surname: ")
day = "today"

message = "Hello %s %s! What's up %s?" % (name, surname, day) 
# OR
message = f"Hello {name} {surname}! What's up {day}?"
# OR
message = "Hello {} {}! What's up {}?" .format(name, surname, day)

print(message)

def foo(person):
    the_person = f"Hi {person}"
    return the_person
print(foo("Marry"))

def foo(person):
    the_person = f"Hi {person.title()}"
    return the_person
print(foo("marry"))