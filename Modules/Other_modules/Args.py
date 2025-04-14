def print_args(*args):
    for arg in args:
        print(f"Args:{arg}")

print_args(1,2,3,4)

# keyword-only arguments are arguments that can only be specified using their name, not as positional arguments. 

def print_details(name, age, *, city, country):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Country: {country}")

# Correct usage with keyword-only arguments
print_details("Alice", 30, city="New York", country="USA")
