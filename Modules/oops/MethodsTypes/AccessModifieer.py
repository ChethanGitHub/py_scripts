class Employee:
    """Tprivate, prefix it with double underscore (such as "__age").
    To protected, prefix it with single underscore (such as "_salary").
    
    Public members − A class member is said to be public if it can be accessed from anywhere in the program.

    Protected members − They are accessible from within the class as well as by classes derived from that class.

    Private members − They can be accessed from within the class only.

    You can still access the private members by Python's name mangling technique
    """

    def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
    
    def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
print (e1.__age)

#Mangling 
e1._Employee__age
# obj._class__privatevar

"""
Bhavana
10000
Traceback (most recent call last):
 File "C:\Users\user\example.py", line 14, in <module>
  print (e1.__age)
        ^^^^^^^^
AttributeError: 'Employee' object has no attribute '__age'
"""

