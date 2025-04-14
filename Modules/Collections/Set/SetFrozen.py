# Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4, 5])

# Attempting to modify the frozenset (will raise an error)
# frozen_set.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'

# Frozen sets support set operations but cannot be modified
another_set = {3, 4, 5, 6, 7}
print("Intersection with frozenset:", frozen_set.intersection(another_set))  # Output: {3, 4, 5}