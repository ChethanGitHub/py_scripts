# Using the setdefault() Method
#The setdefault() method in Python is used to get the value of a specified key in a dictionary. 
# If the key does not exist, it inserts the key with a specified default value.

# Initial dictionary
student = {"name": "Alice", "age": 21}
# Adding a new key-value pair
major = student.setdefault("major", "Computer Science")
print(student) #Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}

# set default values for keys that not been set 
from collections import defaultdict
d= defaultdict(int)

d["a"] = 1
d["b"] = 2
d["c"] #Output: {'c': 0 }}

print(d)

# custom funciton for defalt values 
def default_value():
    return "N/A"

new_d = defaultdict(default_value)
new_d["a"] #Output: {'a': 'N/A' })

print(new_d)
