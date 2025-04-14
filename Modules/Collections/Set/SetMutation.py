set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Update set1 with the union of set1 and set2
set1.update(set2)
print("After update:", set1)  # Output: {1, 2, 3, 4, 5}

# Update set1 with the intersection of set1 and set2
set1.intersection_update(set2)
print("After intersection_update:", set1)  # Output: {3, 4, 5}

# Update set1 with the difference of set1 and set2
set1.difference_update({4})
print("After difference_update:", set1)  # Output: {3, 5}

# Update set1 with the symmetric difference of set1 and another set
set1.symmetric_difference_update({5, 6})
print("After symmetric_difference_update:", set1)  # Output: {3, 6}