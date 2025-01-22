# Conditional Statements : if-elif-else

marks = int(input("Enter your Marks:"))

if(marks>=90 and marks <= 100):
    print("A-Grade")

elif(marks < 90 and marks >= 80):
    print("B-Grade")

elif(marks < 80 and marks >= 70):
    print("C-Grade")

elif(marks < 70 and marks >= 0):
    print("D-Grade")

else:
    print("Invalid Marks")

age = 18

if(age >= 18):
    if(age>=80):
        print("Can't Drive")
    else:
        print("Can Drive")
else:
    print("Can't Drive")