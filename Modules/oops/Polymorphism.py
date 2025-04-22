"""
1.Duck Typing
2.Operator Overloading
3.Method Overriding
4.Method Overloading
"""

"""1.ßDuck Typing
you can call any method on an object without checking its type, as long as the method exists
IT allows objects of different types to be used interchangeably as long as they have the required methods or attributes"""
class Duck:
   def sound(self):
      return "Quack, quack!"

class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"

def makeSound(obj):
   print(obj.sound())

# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)   
makeSound(anotherBird) 

"""
 2.method overriding, a method defined inside a subclass has the same name as a method in its superclass but implements a different functionality.
 """
from abc import ABC, abstractmethod
class shape(ABC):
   @abstractmethod
   def draw(self):
      "Abstract method"
      return

class circle(shape):
   def draw(self):
      super().draw()
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      super().draw()
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()

"""
3. Mehthod overloading 
When a class contains two or more methods with the same name but d
"""
def add(*nums):
   return sum(nums)

# Call the function with different number of parameters
result1 = add(10, 25)
result2 = add(10, 25, 35)

print(result1)  
print(result2) 