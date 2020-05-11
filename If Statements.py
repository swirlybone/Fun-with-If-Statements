#Name:Trevon Harris
#Course:CPSC1301
#Purpose:If Statements Worksheet
import math
import random
#5
print("Number 5")
by = int(input("Enter your birth year:"))
if by > 2003:
    print("Not old enough")
else:
    print("Approve")
print()
print()
print()
print("Number 6")
#6
random = random.randint(0,100)
print(random)
if (random % 2) == 0:
   print("Number is even")
else:
   print("Number is odd")
print()
print()
print()
#8
print("Number 8")
num1 = int(input("Enter the first number:"))
num2 = int(input("Ebter the second number"))
num3 = int(input("Enter the last number:"))
if (num1 > num2) and (num1> num3):
    largest_num = num1
    print("The largest number is:", largest_num)
elif (num2 > num1) and (num2 > num3):
    largest_num = num2
    print("The largest number is:", largest_num)
else:
    largest_num = num3
    print("The largest number is:", largest_num)
print()
print()
print()
#9
code = int(input("Enter ASCII codes:"))
if code >= 91:
    print("Not capital letter.")
elif code <= 64:
    print("Not capital letter.")
else:
    decode = chr(code)
    print(decode)
print()
print()
print()
#10
code2 = int(input("Enter ASCII codes:"))
if code2 >= 123:
    print("Not a letter.")
elif code2 == 91:
    print("Not a letter.")
elif code2 == 92:
    print("Not a letter.")
elif code2 == 93:
    print("Not a letter.")
elif code2 == 94:
    print("Not a letter.")
elif code2 == 95:
    print("Not a letter.")
elif code2 == 96:
    print("Not a letter.")
elif code2 <= 64:
    print("Not a letter.")
else:
    decode2 = chr(code2)
    print(decode2)

