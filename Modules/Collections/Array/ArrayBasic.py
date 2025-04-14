import array as arr
"""
Unlike other programming languages like C++ or Java, Python does not have built-in support for arrays.
 
Syntax:
obj = array_name.array(typecode[, initializer])
typecode	Python data type	Byte size
'b'	        signed integer	        1
'B'	        unsigned integer    	1
'u'	        Unicode character	    2
'h'	        signed integer	        2
'H'	        unsigned integer	    2
'i'	        signed integer	        2
'I'	        unsigned integer	    2
'l'	        signed integer	        4
'L'	        unsigned integer	    4
'q'	        signed integer	        8
'Q'	        unsigned integer	    8
'f'	        floating point	        4
'd'	        floating point	        8

Traverse − Print all the array elements one by one.
Insertion − Adds an element at the given index.
Deletion − Deletes an element at the given index.
Search − Searches an element using the given index or by the value.
Update − Updates an element at the given index.
"""

#creating array
arr1 = arr.array('i',[1,2,3,4,5,6])

#Accessing element
print(arr1[0]) # 1
print(arr1[1]) # 2

#Adding element
arr1.append(9) # 1 2 3 4 5 6 9
arr1.insert(2,20) # 1 2 20 3 4 5 6 9
arr1.extend([10,20,30])

#Removing element
arr1.remove(1) # 2 20 3 4 5 6 9 10 20 30

last_element = arr1.pop() #removing last element
print("last element",last_element) #30

arr1.index(2) # 0
arr1[0]= 1 # 1 20 3 4 5 6 9 0 20

for item in arr1:
    print(item,end=" ")

#Sorted array
sorted_arr = sorted(arr1)
sorted_arr_rev = arr1.reverse()
print("sorted_arr",sorted_arr)  # Output: array('i', [1, 2, 5, 7, 9])
print("reversed array",arr1) # Output : array('i', [20, 10, 9, 6, 5, 4, 3, 20, 1])

arr2 = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])

# Slicing the array
print(arr2[2:5])  # Output: array('i', [3, 4, 5])
print(arr2[:4])   # Output: array('i', [1, 2, 3, 4])
print(arr2[4:])   # Output: array('i', [5, 6, 7, 8])
print(arr2[-3:])  # Output: array('i', [6, 7, 8])

# Array operation
arr3 = arr.array('i', [10, 20, 30, 40, 50])

# Length of the array
print(len(arr3))  # Output: 5

# Sum of all elements
print(sum(arr3))  # Output: 150 

# Minimum and maximum elements
print(min(arr3))  # Output: 10
print(max(arr3))  # Output: 50


arr4 = arr.array('i', [1, 2, 3, 4, 5])

# Convert array to list
arr_list = arr4.tolist()
print(arr_list)  # Output: [1, 2, 3, 4, 5]

# Convert list to array
new_arr = arr.array('i', arr_list)
print(new_arr)  # Output: array('i', [1, 2, 3, 4, 5])