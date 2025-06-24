def greet_user(name):
 print(f"Hello, {name}! Have a great day!")
greet_user("Dakshi")

def power_numbers(number):
 square = number * number
 cubic = number * number * number
 return square , cubic
number = 3
square, cubic = power_numbers(number)
print("Square : ", square)
print("Cubic : ", cubic)

def check_even_odd(number):
 if number % 2 ==0:
  return "Even"
 else:
  return "odd"
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")

for i in range(1, 6):
 print(f"{i} is {check_even_odd(i)}")


def welcome(name, role= "Learner"):
 print(f"Welcome, {name}! Your role is {role}.") 
welcome("Dakshinesh", "Admin")
welcome("Dakshinesh")

def add_numbers(*args):
 total = 0 
 for num in args:
  total += num
 return total
print(add_numbers(5 ,10))
print(add_numbers(1, 2, 3, 4, 5))