
def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={ 
  "+": add, 
  "-": substract, 
  "*": multiply, 
  "/": divide
}

def calculator ():
  for symbol in operations:
    print(symbol)
  num1=float(input("What's the first number?: "))
  not_finished= True

  while not_finished:
    
    num2=float(input("What's the next number?: "))
    operation_symbol= input("Pick an operation: ")
    calculation_func= operations[operation_symbol]
    answer= calculation_func(num1,num2)
    print(f"{num1} {operation_symbol} {num2}= {answer}")
    choice=input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation: ")
    if choice=="n":
      not_finished= False
      print(" The calculation has ended 😊")
    elif choice=="y":
      num1=answer
      calculator()

calculator()



