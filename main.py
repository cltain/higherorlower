from art import logo, vs
from game_data import data
import random
from replit import clear

count = 0
def format_data(account):
  acc_name = account["name"]
  acc_description = account["description"]
  acc_country = account["country"]
  return f"{acc_name}, {acc_description}, from {acc_country}."
  
def compare(acc1, acc2):
  guess = input("Who has more followers? Type 'A' or 'B': ")
  count1 = acc1["follower_count"]
  count2 = acc2["follower_count"]
  if count1 > count2 and guess == 'A':
    return True
  elif count1 < count2 and guess == 'B':
    return True
  else:
    return False
print(logo)
account2 = random.choice(data)
cont = True
while cont:
  account1 = account2
  account2 = random.choice(data)
  if account1 == account2:
    account2 = random.choice(data)
  
  print(f"Compare A: {format_data(account1)}")
  print(vs)
  print(f"Against B: {format_data(account2)}")
  
     
  iscorrect = compare(account1, account2)
  if iscorrect:
    clear()
    print(logo)
    count += 1
    print(f"You're right! Current score: {count}")    
  else:
    cont = False
    print(f"Sorry, that's wrong. Final score: {count}")
