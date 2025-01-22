# Lists : A built-in data type that stores set of values
#         It can store elements of different types (integer, float, string, etc.)

marks = [94.6, 87.3, 40.3, 64.7, 93.9, 72.8]

print(marks)

print(type(marks))

print(marks[0])      # accessing by locating the index

print(len(marks))

# in Python, Srings are "Immutable" as here the data/elements can only be accessed but can't be changed at the STR[INDEX]
#            but Lists are "Mutable" where the data/elements inside it can be accessed and we can also make changes at the LIST[INDEX]


# 1) LIST SLICING : Similar to String Slicing

    # list_name[ starting_idx : ending_idx ]    "ending [idx] is not included"

marks = [87, 64, 33, 95, 76]

marks[ 1 : 4 ] # is [64, 33, 95]

marks[ : 4 ] # is same as marks[ 0 : 4]

marks[ 1 : ] # is same as marks[ 1 : len(marks) ]

marks[ -3 : -1 ] # is [33, 95]

# 2) LIST Methods : 

list = [2, 1, 3]

list.append(4) #adds one element at the end [2, 1, 3, 4]    "here, we mutated the list"

list.sort( ) #sorts in ascending order [1, 2, 3]

list.sort( reverse=True ) #sorts in descending order [3, 2, 1]

list.reverse( ) #reverses list [3, 1, 2]

list.insert( 2, "Jai" ) #insert element at index

print(list)



list2 = [2, 1, 3, 1]

list2.remove(1)  #removes first occurrence of element

list2.pop(2)     #removes element at idx

print(list2)