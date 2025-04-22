class Employee:
    """ Create class employee, parameter name and salary
    1. create counter, when new object is created count should be increased
    2. Method to show displayCount
    3. Method to show displayEmployee name and salary 
    """

    empCount = 0

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def showCount(self):
        print(f"Total employee {Employee.empCount}")

    def showEmployee(self):
        print(f"Name {self.name}, Salary {self.salary}")

    # This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)

emp1.showEmployee()
emp1.showCount()

#You can add, remove, or modify attributes of classes and objects at any time

# Add an 'age' attribute
emp1.age = 7  
# Modify 'age' attribute
emp1.age = 8  
# Delete 'age' attribute
# del emp1.age  

# Returns true if 'age' attribute exists
print(hasattr(emp1, 'age'))
# Returns value of 'age' attribute
print(getattr(emp1, 'age')    )
# Set attribute 'age' at 8
print(setattr(emp1, 'age', 8) )
# Delete attribute 'age'
print(delattr(emp1, 'age')  )

""" Built-In Class Attributes in Python
SNo.	Attributes & Description
1	__dict__
Dictionary containing the class's namespace.

2	__doc__
Class documentation string or none, if undefined.

3	__name__
Class name

4	__module__
Module name in which the class is defined. This attribute is "__main__" in interactive mode.

5	__bases__
A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

"""