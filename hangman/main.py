import random
from hangman_art import logo
from hangman_words import word_list

word = random.choice(word_list)

print(logo)
wrong_letters = str()
display_word = []
for places in word:
  display_word.append("_")
user_letters = []
attempts = 6
while attempts > 0:
  print("____________________________________________________________")
  print(f"\nWrong letters: {wrong_letters} you have {attempts} remaining")
  user_letter = input("\nGuess a letter: ")
  if user_letter in user_letters:
    print("\nYou already used this, try again \n")
  if user_letter in word:
    for x in range(0, len(display_word)):
      if user_letter == word[x]:
        display_word[x] = user_letter
        user_letters.append(display_word[x]) 
    print("\n" +"  ".join(display_word))
    if "".join(display_word) == word:
      print("You win!")
      break 
  else:
    if user_letter not in wrong_letters:
      wrong_letters += user_letter + ', '
      attempts -= 1
    else:
      print("\nYou already used this, try again \n")
    if attempts == 0:
      print(f"Nice try, the awsner is {word}")