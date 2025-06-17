name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
score1 = int(input("Enter your score: "))
score2 = int(input("Enter your score: "))

print("Sum of scores:" ,score1 + score2)
print("Difference between scores:" ,score1 - score2)
print("Product of scores:" ,score1 * score2)
print("Division of scores:" ,score1 / score2)
print("Floor division of scores:" ,score1 // score2)
print("Remainder:" ,score1 % score2)
print("Exponential:" ,score1 ** score2)

print("Eligible to vote:" , age >= 18)
print("Tall enough to ride:" , height >= 5.0)
print("score1 > score2:", score1 > score2)

age_height_condition = (age >= 18) and (height >= 5.0)
any_score_above_90 = (score1 > 90) or (score2 > 90)

print(f"Age and height condition met: {age_height_condition}")
print(f"Any score above 90: {any_score_above_90}")
