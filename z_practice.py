# num = int(input("Enter the number:"))

# if(num%7==0):
#     print(num,"is multiple of 7")
# else:
#     print(num,"is not a multiple of 7")

# num1 = int(input("Enter the 1st number:"))
# num2 = int(input("Enter the 2nd number:"))
# num3 = int(input("Enter the 3rd number:"))

# if(num1>num2 and num1>num3):
#     print(num1)

# elif(num2>num3):
#     print(num2)

# else:
#     print(num3)

# print("Enter your fav 3 movies")

# movies = []

# fav1 = input("Enter your 1st fav:")

# fav2 = input("Enter your 2nd fav:")

# fav3 = input("Enter your 3rd fav:")

# movies.append(fav1)
# movies.append(fav2)
# movies.append(fav3)

# print(list)

# tuple = ("C", "D", "A", "A","B", "B", "A")

# copy = list.copy()

# copy.reverse()

# if(list == copy):
#     print("palandrome")

# else:
#     print("Not Palindrome")

# print(tuple.count("A"), " STUDENTS GOT 'A'- GRADE")

# list = ["C", "D", "A", "A","B", "B", "A"]

# list.sort()

# print(list)

marks = {}

print("Enter your marks for following Subjects")

math = int(input("Maths:"))
marks.update({"Maths" : math})

phy = int(input("Phy:"))
marks.update({"Physics" : phy})

che = int(input("Che:"))
marks.update({"Chemistry" : che})

print(marks)