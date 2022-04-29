from operator import concat


def area(a, b):
    return a * b

print(area(4, 5))

def foo(text1, text2):
    return concat(text1, text2)

print(foo("abc", "efg"))

def area(a=5, b=7): # default args
    return a * b

print(area(a=10, b=9)) # it replaces the default args   

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 5, 7)) 

def foo(*text):
    the_text = [text.upper() for text in text]
    return sorted(the_text)

print(foo('snow', 'rain', 'ice'))    

def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3, b=3, c=3))

def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))

