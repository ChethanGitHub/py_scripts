class JustCounter:
    """name attributes with a double underscore prefix, and those attributes then are not be directly visible to outsiders."""
    __secretCount = 0
    
    def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCount) #AttributeError: 'JustCounter' object has no attribute '__secretCount'
