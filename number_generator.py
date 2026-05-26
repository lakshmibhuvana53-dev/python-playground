import random
logo = """  ________                               ___________.__               _______               ___.                 
 /  _____/ __ __   ____   ______ ______  \__    ___/|  |__   ____     \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/    |    |   |  |  \_/ __ \    /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \     |    |   |   Y  \  ___/   /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >    |____|   |___|  /\___  >  \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                   \/     \/           \/            \/    \/     \/       """
 
print(logo)
print("Welcome To The Number Guessing Game! ")
print("I am thinking a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()
if user_choice == "easy":
    attempts = 10
elif user_choice == "hard":
    attempts = 5
else:
    print("Invalid Choice! The game will start with easy mode by default.")
    attempts = 10
random_number = random.randint(1, 100)
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print(f"Congratulations! You guessed the number {random_number} correctly!")
        break
    elif guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    
    attempts -= 1

        
    if attempts == 0:



        print(f"Sorry, you've run out of attempts. The number was {random_number}.")
        
        