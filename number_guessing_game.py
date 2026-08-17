import random

print("Welcome to the number guessing game! Guess a number from 1 to 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True: 

    user_guess = int(input("Enter a number: "))
    attempts += 1

    if user_guess > secret_number:
         print("Too high")      
    elif user_guess < secret_number:
         print("Too low")
    else:
         print("Correct!")
         break

print("Attempts: ", attempts)



         
    

    







