# Strings : a datatype that stores sequence of characters.

# Basic String Operations

str1 = "hello"
str2 = "World!"
str3 = "Hi everyone I'm Jayadev"

print(str1 + " " + str2)   # 1) Concatination

print(len(str3))           # 2) Length of string

# 3) Indexing : str[index] to access the data

# 4) Slicing : accessing the parts of a string   syntax - str[ starting_index : ending_index ]   where ending index is "not included"

   # str[ : index] is same as str[ 0 : index]
   # str[index : ] is same as str[ index : len(str)]

   # slicing supports negative indexing as it counts ending as "-1" and decrements towards left

str4 = "Jayadev Naidu"

print(str4[0:7])

# String Functions
str = "i am learning Python"

    # 1) str.endsWith(“sub-string“) #returns true if string ends with substr

print(str.endswith("hon")) # gives boolean(true/false)

    # 2) str.capitalize( ) #capitalizes 1st char                                 Changes are made only for that instance
print(str.capitalize())

    # 3) str.replace( old, new ) #replaces all occurrences of old with new       Changes are made only for that instance
print(str.replace( "Python", "Java Sript"))

    # 4) str.find( word ) #returns 1st index of 1st occurrence
print(str.find("P"))

    # 5) str.count(“am“) #counts the occurrence of substr in string
print(str.count("n"))