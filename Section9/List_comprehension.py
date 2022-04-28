temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)    

# but to make it more simple we can use a list comprehension - means do it with one line of code

new_temps = [temp / 10 for temp in temps]

print(new_temps)

# if condition

temps = [221, 234, 340, -9999, 230]

new_temps = [temp /10 for temp in temps if temp != -9999]

print(new_temps)

def foo(values):
    new_values = [value for value in values if type(value) != str]
    return new_values

print(foo([99, 'no data', 95, 94, 'no data']))

# OR

def foo(lst):
    return [i for i in lst if isinstance(i, int)]

print(foo([99, 'no data', 95, 94, 'no data']))

def foo(lst):
    return [i for i in lst if i > 0]

print(foo([-5, 3, -1, 101]))

# else in list comprehension

temps = [221, 234, 340, -9999, 230]

new_temps = [temp /10 if temp != -9999 else 0 for temp in temps] # ELSE GOES FIRST!!!!

print(new_temps)
  
def foo(lst):
    return [i if isinstance(i, int) else 0 for i in lst]

print(foo([99, 'no data', 95, 94, 'no data']))

# OR

def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]

print(foo([99, 'no data', 95, 94, 'no data']))   

def foo(lst):
    return sum([float(i) for i in lst])

print(foo(['1.2', '2.6', '3.3']))    