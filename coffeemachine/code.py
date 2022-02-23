import data 

profit=0
resources= {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
 is_enough= True
 for item in order_ingredients:
    if order_ingredients[item]>= resources[item]:
      print(f"Sorry there is not enough {item}")
      is_enough=False
 return is_enough

def process_coins():
   print("Please insert coins.")
   total= float(input("How many quarters?: "))* 0.25
   total += float(input("How many dimes?: "))* 0.1
   total += float(input("How many nickles?: "))* 0.05
   total += float(input("How many pennies?: "))* 0.01
   return total

def is_transaction_succesful(money_received, drink_cost):
   if money_received>=drink_cost:
      change =round(money_received-drink_cost, 2)
      print(f"Here is {change} in change.")
      global profit
      profit += drink_cost
      return True
   else:
      print("Sorry there's no enough money")
      return False

def make_coffee(drink_name, order_ingre):
   for item in order_ingre:
      resources[item] -= order_ingre[item]
   print(f"Here is your {drink_name}. Enjoy!")

is_on=True

while is_on:
   choice= input("What would you like? (espresso/latte/cappuccino): ")
   if choice=="off":
      is_on=False
   elif choice=="report":
      print(f"Water: {resources['water']}ml ")
      print(f"Milk: {resources['milk']}ml ")
      print(f"Coffee: {resources['coffee']}g ")
      print(f"Money: ${profit}")
   else:
      drink= data.MENU [choice]
      if is_resource_sufficient(drink["ingredients"]):
         payment= process_coins()
         if is_transaction_succesful(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])