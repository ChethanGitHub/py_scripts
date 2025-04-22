class Point:

    "The __del__() destructor prints the class name of an instance that is about to be"

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __del__(self):
        className  = self.__class__.__name__
        print(f"{className} Deleted")

pt1 = Point(10,20)
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print (id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3
