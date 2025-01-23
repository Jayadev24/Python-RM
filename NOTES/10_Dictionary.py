# Dictionary in Python : Dictionaries are used to store data values in " key:value " pairs

info = {
    "name" : "Jayadev",                     # Stores String
    "subjects" : ["DL","ANN", "Python"],    # Stores List
    "topics" : ("dictionary", "sets"),      # Stores Tuples
    "age" : 20,                             # Stores Integers
    "is_adult" : True                       # Stores Boolean values
}

# They are unordered, mutable(changeable) & don’t allow "duplicate keys"

print(info["name"])
print(info["age"])
print(info["is_adult"])
print(info["subjects"])

# They are mutable and can be changed

info["name"] = "Jayadev L"   # we can change(over write) value stored in the key
info["iD"] = "300356"        # we can add a new key:value pair

print(info)

null_disct = {}   # it used when we are about to add details timely in the process

# Nested Dictionary

student = {
    "Name": "Abhiram",
    "score" : {
        "math" : 95,
        "phy"  : 80,
        "che"  : 87
    }
}

print(student)

print(student["score"]["math"]) # by add a new "[]" we can search deep into the dictionary

# Dictionary Methods

"""
myDict.keys()             #returns all keys

myDict.values()           #returns all values

myDict.items()            #returns all (key, val) pairs as tuples

myDict.get(“key“)         #returns the key according to value

myDict.update(newDict)    #inserts the specified items to the dictionary
"""