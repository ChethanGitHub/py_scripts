list1 = ["Chetan", "Swathi",13,14,20]
print(list1[2])

# Add
list1.append("added newly")
print(list1)

# Delete
del list1[0]
print(list1)

#concatination
list_concat=[1,3,5] + ["Hi","Hello"]
print(f"{list_concat} concatination")

# multiple
multiple = [1,2,3] * 3
print(f"{multiple} multiple")

print('\n\n')
print('original-',list1)
print('index-',list1[-2])
print('start after first element-',list1[1:])
print('Negetive count from last-',list1[:-1])
print('reverse order-',list1[::-1])

# list common operation
list2=["Hi"]
list2.append("new data")
list2.insert(1,"some data")
list2.remove("some data")
list2.pop(1) #pop with index

list2.sort()
list2.sort(reverse =True)

del list2[0]
list2.clear()

# Zipping two lists together
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(zipped)  # Output: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

list1.extend(list2)

# sort vs soreted
list1.sort()
sorted(list1,reverse=True)