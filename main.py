import random

words_lists = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(words_lists)

print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_Over = False
while not game_Over:
    Guessed_letters = input("Guess a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == Guessed_letters:
            display[position] = Guessed_letters

    if Guessed_letters not in chosen_word:
        lives -= 1
        if lives == 0:
            game_Over = True
            print("You lose")

    if '_' not in display:
        game_Over = True
        print("You win")
