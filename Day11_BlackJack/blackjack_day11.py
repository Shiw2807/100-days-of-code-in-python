import random
from turtle import clear

def pick_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, dealer_score):
  
  if dealer_score > 21 and user_score > 21:
    return "You lose miserably. You went over 21.😣😥"
  if user_score == dealer_score:
    return "It is a draw. Better luck next time.😣"
  elif dealer_score == 0:
    return "You lose. The dealer has a Blackjack 😕"
  elif user_score == 0:
    return "Congratulations. Blackjack, you win!😊"
  elif user_score > 21:
    return "Oh man. You went over. You lost. 😣"
  elif dealer_score > 21:
    return 'Congrats. You have won!!! Dealer went over 21.😊'
  elif user_score > dealer_score:
    return 'You win😘👌!'
  else: 
    return "You lose😓!"


def play_game():
  user=[]
  comp=[]
  for i in range(2):
    user.append(pick_card())
    comp.append(pick_card())

  is_game_over= False

  while not is_game_over:
    uscore= calculate_score(user)
    cscore= calculate_score(comp)

    print(f"Your cards: {user} current score: {uscore}")
    print(f"Computer's first card: {comp[0]}")

    if uscore==0 or cscore==0 or uscore>21:
      is_game_over= True
    else: 
      choice=input("\n Type 'y' to get another card, type 'n' to pass: ")
      if choice=='y':
        user.append(pick_card())
      else:
        is_game_over= True

  while cscore!=0 and cscore<17:
    comp.append(pick_card())
    cscore= calculate_score(comp)

  print(f"User current cards: {user} Your current score: {uscore}")
  print(f"Computer's current cards:{comp} pmputer's current score: {cscore}")
  result= compare(uscore,cscore)
  print(result)


while(input("Do you want to play the game of Blackjack? Type 'y' or 'n': "))=="y":
  clear()
  play_game()