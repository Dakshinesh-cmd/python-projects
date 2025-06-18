#simple calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")


if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")

#pass/ fail

mark = int(input("Enter your mark: "))
if mark >= 90: print("Grade A")
elif mark >= 75: print("Grade B")
elif mark >= 60: print("Grade C")
else: print("Grade F")


#find larger number

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3: print("The largest number is: ", num1)
elif num2 >= num1 and num2 >= num3: print("The largest number is: ", num2)
else: print("The largest number is: ", num3)

#odd/even

number = int(input("Enter a number: "))
if number % 2 ==0: print(number, "is even")
else: print(number, "is odd")

#smiple bill splitter

bill = float(input("Enter the total bill amount:"))
people = int(input("Enter the number of people:"))

if people == 0: 
 print("Number of people must be greater than 0.")
else:
 each_person_pays = bill / people
 print(f"Each person should pay: ₹{each_person_pays:.2f}")
