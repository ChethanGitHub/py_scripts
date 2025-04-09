set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union: Combines all unique elements from both sets "|"
union_set = set1.union(set2)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

union_set = set1 | set2 # union can ber performed by "|" or "union" 

# Intersection: Finds common elements between sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Output: {3, 4, 5}

# intersection update÷ also can use operator "&"
intersec_update_set = set1.intersection_update(set2)
print(intersec_update_set) # Output update the intersection result in set1

# Difference: Finds elements in set1 but not in set2, also using operator "-"
difference_set = set1.difference(set2)
print("Difference:", difference_set)  # Output: {1, 2}

# Symmetric Difference: Finds elements not common in both sets, also using operator "^"
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 6, 7}