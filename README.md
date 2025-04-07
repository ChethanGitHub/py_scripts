# py_scripts
usefull utility
keyword-only arguments are arguments that can only be specified using their name, not as positional arguments. 

def print_details(name, age, *, city, country):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Country: {country}")

# Correct usage with keyword-only arguments
print_details("Alice", 30, city="New York", country="USA")


Function Annotation
def fn(a:Int,b:Int)

Funcirton Annotation with expression
def marks(x:'Marks in Maths', y:'Marks in Science')