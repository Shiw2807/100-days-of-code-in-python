import random

number=random.randint(1,100)
print("Welcome to the Number Guessing Game.\n I am thinking of a number between 1 and 100.")
choice=input("Choose your difficulty. Type 'easy' or 'hard': ")

if choice=="easy":
  n=10
elif choice=="hard":
  n=5

while n>0:
  print(f"You have {n} attempts remaining to guess the number")
  guess= int(input("Make a guess: "))
  if(guess<number):
    print("Too low")
    if n>1:
      print("Guess Again")
  elif(guess>number):
    print("Too High")
    if n>1:
      print("Guess Again")
  else:
    print(f"You win! The answer is {number} ")
    n=0
  n+=-1
  if(n==0):
    print("Oops, no more attempts left!")