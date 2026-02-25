# Quest 25: The number wizard
# Asks user to guess a number and gives feedback

secret_number = 7  
user_guess = int(input("Guess the number: "))

if user_guess == secret_number:
    print("Your guess is correct!")
elif user_guess < secret_number:
    print("Too low!")
else:
    print("Too high!")
