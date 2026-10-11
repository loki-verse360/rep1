import random
def play():
user=input("Enter 'r' for rock 'p' for paper and 's' for scissors")
computer=random.choice(['r','p','s'])
if user==computer:
  return'Tie'
  elif ((user=='r' and computer=='s') or (user=='s' and computer=='p') or (user='p' and computer='r')):
    return 'YOU WIN'
else:
    return'YOU LOST'

print(play())
    
