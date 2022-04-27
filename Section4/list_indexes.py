some_list = [1, 4, 6, 3, 10]
print(some_list.index(6))
# and reverso
print(some_list.__getitem__(2))
# or better
print(some_list[2])

something = [15, 1001]

some_list.append(something[1])
print(some_list)
some_list.remove(something[1])
print(some_list)

print(some_list[1:3]) # returns only specific slice of list

# if you want to get slice started from 0 index it can look

print(some_list[:3])
# or to the end
print(some_list[3:])

# we can also use - index for lists

print(some_list[-1])
print(some_list[-4:-1])
print(some_list[-3:])