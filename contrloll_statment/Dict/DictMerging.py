# Merging Dictionaries
dict1 = {"name": "Alice", "age": 25}
dict2 = {"course": "Mathematics", "grade": "A"}

#using update() method 
dict1.update(dict2)
print("dict1 - ",dict1)

# Using dictionary unpacking (Python 3.9+)
dict3 = {**dict1 , **dict2}
print("dict3 - ",dict3)

# Using the Union Operator (|)
dict4 = dict1 | dict2
print("dict4 - ",dict4)

# Using the "|=" Operator
# The |= operator in Python is an in-place union operator for sets and dictionaries. 
# It updates the set or dictionary on the left-hand side with elements from the set or dictionary 
# on the right-hand side.

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks |= marks1
print ("marks dictionary after update: \n", marks)
#Output: {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}



