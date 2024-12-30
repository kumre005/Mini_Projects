import random

# List orf word to choose from
word_list = ["apple","beautiful","potato"]
chosen_word = random.choice(word_list)
print(chosen_word)

# Initialize display and lives
display = ['_']
lives = 6

for letter in range(len(chosen_word)): # 0 1 2 3 4 5 
    display += '_'
print(display)
game_over=False

# Game loop
while not game_over:

    guessed_letter = input("Guess a letter: ").lower()
    for position  in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter

    if guessed_letter not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You loose!!!")
    
    if '_' not in display:
        game_over = True
        print("You win!!!")