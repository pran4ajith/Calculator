def add(x,y):
  return x+y #add two numbers

def subtract(x,y):
  return x-y #subtract two numbers
def multiply(x,y):
  return x*y #multiply two numbers
def divide(x,y):
  return x//y #divide two numbers

print("select operation")
print("'1':ADD")
print("'2': SUBTRACT")
print("'3':MULTIPLY")
print("'4':DIVIDE")

user_choice= input ("enter the operation index")
num_1= int(input("enter the first number"))
num_2= int(input("enter the second number"))

if user_choice== '1':
  print(num_1, '+', num_2,"=", add(num_1, num_2))
elif user_choice== '2':
  print(num_1, '-', num_2,"=",subtract(num_1, num_2))
elif user_choice== '3':
  print(num_1, '*', num_2,"=", multiply(num_1, num_2))
elif user_choice== '4':
  print(num_1, '/', num_2,"=", divide(num_1, num_2))
else:
  print("Invalid operation")
