from random import randint
HARD = 5
EASY = 10
def random_number():
    return randint(1, 100)


def choose_level(user_choice):
    if user_choice == "hard":
        print(f"You have {HARD} attempts remaining to guess the number.")
        return HARD
    elif user_choice == "easy":
        print(f"You have {EASY} attempts remaining to guess the number.")
        return EASY
    else:
        print("Invalid Choice! The game will start with easy mode by default.")
        print(f"You have {EASY} attempts remaining to guess the number.")
        return EASY

def game():
    logo = """
      
      ________                               ___________.__               _______               ___.                 
    /  _____/ __ __   ____   ______ ______  \__    ___/|  |__   ____     \      \  __ __  _____\_ |__   ___________ 
    /   \  ___|  |  \_/ __ \ /  ___//  ___/    |    |   |  |  \_/ __ \    /   |   \|  |  \/     \| __ \_/ __ \_  __ \
    \    \_\  \  |  /\  ___/ \___ \ \___ \     |    |   |   Y  \  ___/   /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
    \______  /____/  \___  >____  >____  >    |____|   |___|  /\___  >  \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                   \/     \/           \/            \/    \/     \/       """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    user_choice = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    attempts = choose_level(user_choice)
    number = random_number()

    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"Congratulations! You guessed the number {number} correctly!")
            break
        elif guess < number:
            print("Too Low! \nGuess Again.")
            print(f"You have {attempts-1} attempts remaining to guess the number.")
        elif guess > number:
            print("Too High! \nGuess Again." )
            print(f"You have {attempts-1} attempts remaining to guess the number.")
        
        for i in range(1):
            attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number}.")
game()
