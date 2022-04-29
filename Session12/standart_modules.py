# lets assume we need to execute script even if input fie is deleted while wcript is running
# for this we need an additional module which is not in builtin_modules
# for this we need to import os
# first lets see what is in it
# dir(os) -> 'path'
# so now we can add a check if file exists or not
import time
import os

while True:
    if os.path.exists("Session11/vegetables.txt"): # checks if file exists of not
        with open("Session11/vegetables.txt", "r") as file:
            print(file.read())
    else:
        print("File does not exists")        
    time.sleep(10) # should be out of if function