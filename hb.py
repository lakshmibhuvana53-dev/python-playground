import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["python", "java", "ruby", "javascript", "csharp", "golang", "swift", "kotlin", "php", "typescript"]
chosen_word = random.choice(word_list)
print(chosen_word)
place_holders = " "
word_length = len(chosen_word)
for length in range(word_length):
    place_holders += "_"
print(place_holders)
lives = 6
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
    display =" "
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
                
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")
    print(stages[lives])


  




