def temperature(value):
    if value > 7:
        the_temp = "Warm"
    else:
        the_temp = "Cold"
        
    return the_temp

print(temperature(6))

def foo(value):
    if value > 25:
        return "Hot"
    elif value < 15:
        return "Cold"
    else:
        return "Warm"

print(foo(15))    

def foo(string):
    if len(string) < 8:
        return False
    else:
        return True  

print(foo("mypass"))

def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")