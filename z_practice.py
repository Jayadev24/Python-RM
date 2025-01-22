# num = int(input("Enter the number:"))

# if(num%7==0):
#     print(num,"is multiple of 7")
# else:
#     print(num,"is not a multiple of 7")

num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))
num3 = int(input("Enter the 3rd number:"))

if(num1>num2 and num1>num3):
    print(num1)

elif(num2>num3):
    print(num2)

else:
    print(num3)