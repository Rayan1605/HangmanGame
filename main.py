import random

words_lists = ["apple", "beautiful", "potato"]
chosen_word = random.choice(words_lists)

print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)


