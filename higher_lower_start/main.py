from art import logo, vs
from game_data import data
import random

print(logo)

score = 0

def data_clean(instagram):
  """This takes in data and choose a random choice then extract the dictionary"""
  data_choice = random.choice(instagram)
  name = data_choice['name']
  description = data_choice['description']
  country = data_choice['country']
  follower_count = data_choice['follower_count']
  return [name,description,country, follower_count]

game_on = True

while game_on:
  compare_a = data_clean(data)
  print(f'Compare A: {compare_a[0]}, {compare_a[1]}, from {compare_a[2]}')
  compare_a_count = compare_a[3]
  
  print(vs)
  
  compare_b = data_clean(data)
  print(f'Against B: {compare_b[0]}, {compare_b[1]}, from {compare_b[2]}')
  compare_b_count = compare_b[3]
  
  response = input("Who has more followers? Type 'A' or 'B': ").lower()

  if (response == 'a') and (compare_a_count > compare_b_count):
    score += 1
    print(f"You're right! Current score: {score}.")
  elif (response == 'b') and (compare_b_count > compare_a_count):
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_on = False