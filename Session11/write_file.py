with open ("Session11/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")

# copy first 90 chars from one file to another

with open("Session11/bear.txt", "r") as readfile:
    content = readfile.read()
    
with open("Session11/first.txt", "w") as writefile:
    writefile.write(content[:90])  

# append

with open ("Session11/vegetables.txt", "a") as myfile:
    myfile.write("\nPotato")

# append then move cursor at the beginning then read results  

with open("Session11/vegetables.txt", "a+") as myfile: # + means file is opened for updates
    myfile.write("\nOkra")
    myfile.seek(0) # move curson on 0 position
    content = myfile.read()

print(content) 

# copy file context and append it twice

with open("Session11/data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content) 