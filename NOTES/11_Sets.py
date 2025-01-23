# Sets : Set is the collection of the unordered items.
#        Each element in the set must be unique & immutable.

nums = { 1, 2, 3, 4 }
print(nums)

set2 = { 1, 2, 2, 2 }
print(set2)            #repeated elements stored only once, so it resolved to {1, 2}

null_set = set() #empty set syntax

# Set methods
"""
set.add(el) #adds an element

set.remove(el) #removes the elem an

set.clear() #empties the set

set.pop() #removes a random value

set.union( set2 ) #combines both set values & returns new

set.intersection( set2 ) #combines common values & returns new
"""