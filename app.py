import random

options = ('piedra','papel','tijera') 

user = input( 'piedra, papel, tijera ')
user = user.lower()
computer = random.choice(options)

if not user in options:
  print('opcion invalida')
  
print('user = >',user)
print('computer => ',computer)

if user == computer:
  print('empate !')
elif user == 'piedra':
  if computer == 'tijera':
    print('piedra gana a tijera')
    print('user win')
  else:
    print('papel gana a  piedra ')
    print( 'computer win ')
elif user == 'papel':
  if computer == 'piedra':
    print('papel gana a piedra')
    print('user win')
  else:
    print('tijera gana a  papel ')
    print( 'computer win ')
elif user == 'tijera':
  if computer == 'papel':
    print('tijera gana a papel')
    print('user win')
  else:
    print('piedra gana a tijera ')
    print( 'computer win ')