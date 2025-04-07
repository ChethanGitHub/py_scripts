# any changes within the function create a new object.
def callByValue_immutable(x):
    x = x+1
    print("Inside Function", x)

x = 10
callByValue_immutable(x)
print("value of x:",x)



# changes within the function affect the original object.
def callByRef_mutable(lst):
    lst.append(4)
    print("Inside function ",lst)

lst = [1,2,3]
callByRef_mutable(lst)
print("value of lst:",lst)