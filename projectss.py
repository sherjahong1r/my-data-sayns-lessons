"""
Created on Mon Nov 10 07:21:59 2025
dice_rolling_game.py
@author: Sherjahongir
"""

print("\n")

# Narda o'yini ikki ishtirokchiga son chiqaradi katta yoki kichik

import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 100)
        die2 = random.randint(1, 100)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
        
        
##################################################
        
print("\n\n")

# Son topish o'yini

import random


number_to_guess = random.randint(1, 100)
while True:
  try:
    guess = int(input('Guess the number between 1 and 100:' ))
    
    if guess < number_to_guess:
      print('Too low!')
    elif guess > number_to_guess:
      print('Too hight!')
    else:
      print('Congratulations! You guessed the number.')
  except ValueError:
    print('Please enter a valid number')
    

###################################################

# rock_paper_scissor
# tosh, qog'oz, qaychi o'yini.

import random

emojis = { 'r': 'tosh', 's': 'qaychi', 'p': 'varaq' }
choices = ('r', 'p', 's')

while True:
  user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
  if user_choice not in choices:
    print('Invalid choice!')
    continue
  computer_choice = random.choice(choices)

  print(f'You chose {emojis[user_choice]}')
  print(f'Computer choise chose {emojis[computer_choice]}')

  if user_choice == computer_choice:
    print('Tie!')
  elif (
    (user_choice == 'r' and computer_choice == 's') or \
    (user_choice == 's' and computer_choice == 'p') or \
    (user_choice == 'p' and computer_choice == 'r')):
    print('You win')
  else:
    print('You lose')


  should_continue = input('Continue? (y/n): ').lower()
  if should_continue == 'n':
      break
  













