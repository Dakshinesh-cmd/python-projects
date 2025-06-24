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

def print_info(**kwargs):
 for key, value in kwargs.items():
  print(f"{key}: {value}")
print_info(name="Dakshi", age=22, role="learner")

add = lambda a, b: a + b
output = add(1, 6)
print(output)

number = [2 , 4 , 6 , 8]
squared = list(map(lambda x: x*x, number))
print(squared)

name = ["Alice", "Bob", "Ankit", "John", "Arya"]
a = list(filter(lambda name : name.startswith("A"), name))
print(a)

people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
arrange = sorted(people, key=lambda person: person[1])
print(arrange)

name = ["Alice", "Bob", "Charlie"]
age = [25, 30, 18]
combined= list(zip(name, age))
print(combined)

for name, age in zip(name , age):
 print(f"{name} is {age} years old")