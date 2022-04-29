myfile = open("Session11/fruits.txt", "r") # r-read, w-write, x-create new file, a-append to the end

print(myfile.read())
print(myfile.read())
# read method can move cursor through the file only once, so there is no way to execute read method twice!
# but we can save it into variable

myfile = open("Session11/fruits.txt", "r")

my_text = myfile.read()

print(my_text)
print(my_text)
print(my_text)
print(my_text)

# good practice is to close file after reading to clean up a mamory
myfile = open("Session11/fruits.txt", "r")

my_text = myfile.read()
myfile.close()

print(my_text)

# the better way is to use context manager "with"

with open("Session11/fruits.txt", "r") as myfile:
    content = myfile.read()

print(content)

# show first 90 chars from file

with open("Session11/bear.txt", "r") as myfile:
    content = myfile.read()

print(content[:90])

# find how much 'a' occured in file

def foo(character, filepath="Session11/bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

print(foo('a'))    

