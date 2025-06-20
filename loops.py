secret_password = "python123"

for attempt in range(1 , 4):
 print(f"Attempt {attempt} of 3")
 
 guess = " "
 while guess == " ":
   guess = input("Enter your password (cannot be empty): ")
 
 if guess == secret_password:
    print("✅ Access granted!")
    break
 else:
    print("❌ Incorrect password.\n")

else:
   print("🚫 Access denied. Too many failed attempts.")