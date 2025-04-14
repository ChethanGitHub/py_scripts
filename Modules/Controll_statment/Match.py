# print the type of given value

def print_type(n):
    match n:
        case int(): print("Itiger type")
        case float(): print("float type")
        case str(): print("String type")
        case _: print("Due wtf")

def custom_msg(stmt):
    match stmt :
        case "greeting": print("Hello  Welcome")
        case  "farewell":print("Good Bye")

def even_odd(n):
    match n:
        case n if n % 2 == 0 : print("Even number")
        case _: print("Odd Number")


print_type(10)
custom_msg("greeting")
even_odd(10)