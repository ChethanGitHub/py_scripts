# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = set([3, 4, 5, 6, 7])

my_set = {1,2,4,5,6,8}
print(my_set)

my_set.add(9)
my_set.remove(1)# or
my_set.discard(1) 
my_set.update([4,6,7]) # add multiple element
my_set.pop(1)
my_set.clear()

if 2 in my_set:
    print("here it is")

squared_set = {x**2 for x in range(1, 6)}
print(squared_set)

even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)

nested_set = {(x, y) for x in range(1, 3) for y in range(1, 3)}
print(nested_set)
# output: {(1, 1), (1, 2), (2, 1), (2, 2)}

# Work around to get the index number
# converting set in to a list
my_set = {1, 2, 3, 4, 5}
set_list = list(my_set)

# Iterating through the list 
for index, item in enumerate(set_list):
   print("Index:", index, "Item:", item)