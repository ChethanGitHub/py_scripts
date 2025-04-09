set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)  # Output: True

# Check if set2 is a superset of set1
is_superset = set2.issuperset(set1)
print("Is set2 a superset of set1?", is_superset)  # Output: True