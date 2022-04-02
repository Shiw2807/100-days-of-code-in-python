
from games import names
import random
import logo 
from turtle import clear

game_should_continue=True

score=0
print(logo.logo)
acc_b = random.choice(names)

while game_should_continue:
  acc_a = acc_b
  acc_b = random.choice(names)
  if acc_a == acc_b:
      acc_b = random.choice(names)
  
  print(f"Compare A: {acc_a['name']}, a {acc_a['description']} from {acc_a['country']}")
  
  print(logo.vs)
  
  print(f"Against B: {acc_b['name']}, a {acc_b['description']} from {acc_b['country']}")
  
  guess= input("Who has more followers? Type 'A' or 'B': ").lower()
  
  
  afoll= acc_a["follower_count"]
  bfoll= acc_b["follower_count"]
  
  def check(guess,afoll,bfoll):
    if afoll>bfoll:
      return guess=="a"
    else:
      return guess=="b"

  clear()
  answer= check(guess,afoll,bfoll)

  if answer:
    score+=1
    print(f"You're right! Current score is {score}")
  else:
    game_should_continue=False
    print(f"Sorry that's wrong! Final score is {score}")