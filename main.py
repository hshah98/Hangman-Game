import random, os
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
  display += "_"

lives = 6
should_end = False

print(logo)

while not should_end:
  guess = input("Guess a letter: ").lower()

  os.system("clear")
  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = guess

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
      print(f"You lose. The correct word was {chosen_word}.")
      should_end = True

  print(f"{' '.join(display)}")

  if "_" not in display:
    print("You win!")
    should_end = True

  print(stages[lives])
