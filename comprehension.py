#list

squares = [x * x for x in range(1, 10)]
print(squares)

#dictionary

number = [1 , 2 , 3 , 4 , 5]
cubic = {num: num**3 for num in number}
print(cubic)

number = [1, 2, 3, 4, 5]
square = {num: num**2 for num in number}
print(square)

number = [1, 2, 3, 4, 5]
even = {num: num**2 for num in number if num %2 ==0}
print(even)

user = {
    "name": "Dakshinesh",
    "email": "dakshineshprabhu@gmail.com",
    "city": "Tirupur"
}

total_length = len(user["name"]) + len(user["email"]) + len(user["city"])
print("The total length of all string values is:", total_length)

#set comprehension

unique = {letter for letter in "Welcome Home"}
print(unique)

sentence= "Python programming is powerful and fun!"
vowels = {letter for letter in sentence.lower() if letter in 'aeiou'}
print(vowels)

sentence= "Python programming is powerful and fun!"
vowels = "aeiou"
vowel_count= {}
for char in sentence.lower():
    if char in vowels:
        if char in vowel_count:
            vowel_count[char] += 1
        else:
            vowel_count[char] = 1
print(vowel_count)

sentence = "Learning python is fun"
vowels = 'aeiou'
vowel_count = {}
for char in sentence.lower():
   if char in vowels:
        if char in vowel_count:
            vowel_count[char] += 1
        else:
            vowel_count[char] = 1
print(vowel_count)

