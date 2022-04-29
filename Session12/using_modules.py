# the most modules are available in Python and we can view it by using dir(str) or dir(__builtins)
# but there are also modules which require additional import
# import sys
# sys.builtin_module_names - allows to view some available modules
# to access some of them we need to import it first
# e.g. 'time'
# import time
# now we can see what functions are under this module
# dir(time)
# for example we want to add some delay inside our script
# help(time.sleep) - shows how to use it
# now lets use it in our script
import time

while True:
    with open("Session11/vegetables.txt", "r") as file:
        print(file.read())
        time.sleep(10) # this is delay 10 sec by using time.sleep function
