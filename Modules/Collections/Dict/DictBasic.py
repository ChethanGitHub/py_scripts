person_dict = {
    "name":"chethan",
    "age":33,
    "worth":1000000,
    "name":"swathi",
    "age":32
}

# If the same key is peresent then it will take the laters key only
#Accessing value
name = person_dict["name"]
print("add", end=",")
print(f"name: {name}") # Output: swathi

# Using .get() to access values (avoids KeyError)
print(person_dict.get("course"))  # Output: None
print(person_dict.get("grade", "Not available"))  # Output: Not available

# update 
age = person_dict["age"] = 34
print("update", end=",")
print(f"age: {age}") #Output: 34

# delete
worth = person_dict.pop("worth")
print("delete", end=",")
print(f"worth: {worth}")

del person_dict["age"]

# Using clear() method
person_dict2 = person_dict
person_dict2.clear() #Output: {}

# Using popitem()
# used to remove and return the last key-value pair from a dictionary
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}

r = numbers.popitem()
print("popItem - ",r) #Output: (40, 'Forty')

for i in person_dict:
    print("items in dict")
    print(i)

# itererating
# Using a for Loop
# Using dict.items() method
# Using dict.keys() method
# Using dict.values() method
print("iteration")
for key in person_dict:
    print(f" key: {key}, value: {person_dict[key]}")

student = {
    "name": "Alice",
    "age": 25,
    "course": "Mathematics"
}

print("# Iterating over keys")
for key in student.keys():
    print("Key:", key)

print("# Iterating over values")
for value in student.values():
    print("Value:", value)

print("# Iterating over key-value pairs")
for key, value in student.items():
    print(f"{key}: {value}")

print("# Check if a key exists")
print("name" in student)  # Output: True
print("course" in student)  # Output: False

# Create a dictionary with squares of numbers
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
sqr = {x:x**2 for x in range(5)}
print(sqr)

# Filter a dictionary with comprehension
# Output: {3: 9, 4: 16}
filtered_sqr = {k:v for k,v in sqr.items() if v > 4}
print(filtered_sqr)
