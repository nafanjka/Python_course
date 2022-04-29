# lets imagine we have input csv file with some temperatures from two stations and we need to calculate the average of the temperature
# the is no standart modules to do it and we need to use third party packages
# e.g. pandas
# first we need to install it with - 'pip3.10 install pandas' - pip depends on Python version we use
# now we can import it
import time
import os
import pandas

while True:
    if os.path.exists("Session12/temps_today.csv"):
        data = pandas.read_csv("Session12/temps_today.csv")
        print(data.mean())
    else:
        print("File does nor exist.")
    time.sleep(10)        