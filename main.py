print("python calculator")


num1= int(input("Enter a number here:"))
num2= int(input("Enter another number here:"))

print('''
press 1 for addition
press 2 for substraction
press 3 for multiplication
press 4 for division
''')

selection = (int(input("enter a number between 1-4:")))
if selection == 1:
    sum = num1 + num2
    print ("The addition of the given two numbers is", sum)
elif selection == 2:
    print("The substraction of the given two numbers is", num1-num2) 
elif selection == 3:
    print("The multiplication of the given two numbers is", num1*num2) 
elif selection == 4:
    print("The division of the given two numbers is", num1/num2) 
else:
    print("Invalid Input from the user")             
