# List comprehension to create a new list with squared values
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering a list to keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]


lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print (num, end = ' ')

# iterate over index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
   print(index, fruit)

#  iterate over index 
lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])

list1=[x for x in range(1,21) if x%2==0]
print (list1)

ovel_str = [char for char in "Hello worlrd" if char in "aeiou"]
print(ovel_str)

sqrt = [x **2 for x in range(1,10)]
print(sqrt)