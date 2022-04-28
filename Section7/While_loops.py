username = ''
while username != "pypy":
    username = input("Enter username: ")

# more accurate is to use break and continue statements

while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue    

a = 0
while a < 5:
    a = a + 1
    print(a)     