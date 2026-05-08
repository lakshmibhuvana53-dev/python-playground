import random
word_list = ["python", "java", "ruby", "javascript", "csharp", "golang", "swift", "kotlin", "php", "typescript"]
chosen_word = random.choice(word_list)
print(chosen_word)
place_holders = " "
word_length = len(chosen_word)
for length in range(word_length):
    place_holders += "_"
print(place_holders)
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
    correct_letters = []
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

    if "_" not in display:
        game_over = True
        print("You win!")


  




