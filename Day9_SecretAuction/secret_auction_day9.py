import os
from turtle import clear

bid ={}
biding_finished= False


def find(bidding_record):
  highest=0
  winner=""
  for bidder in bidding_record:
    bid_amt=bidding_record[bidder]
    if (bid_amt>highest):
      highest=bid_amt
      winner=bidder
  print(f"The winner is {winner} with a highest bid of ${highest}")

while not biding_finished:
  user= input("What is your name?:\n ")
  price= int(input("What is your bid?:\n $"))
  bid[user]= price
  other=input("Are there any other bidder? Type 'yes'or 'no:\n ").lower()
  if other=="no":
    biding_finished= True
    find(bid)
  elif other=="yes":
    clear()    

