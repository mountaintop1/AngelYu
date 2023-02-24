from art import logo
import random
print(logo)
# Include an ASCII art logo.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
# print(f"Pssst, the correct answer is {answer}")
difficulty = {
  'easy': 10,
  'hard': 5
}
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
difficulty_choice = difficulty[choice]

print(f'You have {difficulty_choice} attempts remaining to guess the number.')

while difficulty_choice > 0:
  guess = int(input('Make a guess: '))
  if guess == answer:
    print(f'You got it! The answer was {answer}.')
    difficulty_choice = 0
  elif guess < answer:
    print("Too low.")
    difficulty_choice -= 1
    if difficulty_choice == 0:
      print("You've run out of guesses, you lose.")
    else:
      print("Guess again.")
      print(f"You have {difficulty_choice} attempts remaining to guess the number.")
  else:
    print("Too high.")
    difficulty_choice -= 1
    if difficulty_choice == 0:
      print("You've run out of guesses, you lose.")
    else:
      print("Guess again.")
      print(f"You have {difficulty_choice} attempts remaining to guess the number.")
  


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).