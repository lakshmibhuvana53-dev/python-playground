# # Number generator
# import random
# HARD = 5
# EASY = 10
# def choose_difficulty(user_choice):
#     difficulty = user_choice.lower()
#     if difficulty == "easy":
#         print(f"You have {EASY} attempts remaining to guess the number.")
#         return EASY
#     elif difficulty == "hard":
#         print(f"You have {HARD} attempts remaining to guess the number.")
#         return HARD
#     else:
#         print("Invalid input. Please choose 'easy' or 'hard'.")
#         user_choice = input("Choose again : ")
#         return choose_difficulty(user_choice)

# def random_number():
#     return random.randint(1, 100)

# def generator():
#     print("Welcome to the number generator!")
#     print("This program will generate a random number between 1 and 100.")
#     print("You must Guess the number to win !!")
#     number = random_number()
#     user_choice = input("Choose a difficulty level. Type 'easy' or 'hard': ")
#     attempts = choose_difficulty(user_choice)

#     while attempts > 0:
#         guess = int(input("Make a guess: "))
#         if guess < number:
#             print("Too low.")
#             print("Guess again.")
#             print(f"You have {attempts-1} attempts remaining to guess the number.")
#             attempts -= 1
#         elif guess > number:
#             print("Too high.")
#             print("Guess again.")
#             print(f"You have {attempts-1} attempts remaining to guess the number.")
#             attempts -= 1
#         else:
#             print(f"You got it ! The number was {number}. \nyou won !!")
#             break

    
#     if attempts == 0:
#         print(f"You have run out of attempts. The number was {number}.")
#     if guess == number or attempts == 0:
#         print("Hope you enjoyed the game. Thank you for playing!") 

# generator()

