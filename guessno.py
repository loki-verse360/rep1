import random
def guess(x):
  guess=0
  rn=random.randint(1,x)
  while guess!=rn:
    guess=input(f'Guess a number between 1 and {x}')
    if guess<rn:
      print('sorry guess again.Too low.')
    elif guess>rn:
      printf('sorry guess again.Too high.')

print(f'Hooray!! Your guess is correct.{rn}')

guess(100)
    
