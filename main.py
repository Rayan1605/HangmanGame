import random

words_lists = ["apple", "beautiful", "potato"]
chosen_word = random.choice(words_lists)

print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
Guessed_letters = input("Guess a letter: ")

for letter in chosen_word:
    if letter == Guessed_letters:
        print("Match")
    else:
        print("No match")




