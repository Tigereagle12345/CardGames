import random

cards = ["2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "ts", "js", "qs", "ks", "as", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "tc", "jc", "qc", "kc", "ac", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "td", "jd", "qd", "kd", "ad", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "th", "jh", "qh", "kh", "ah"]

player_hand = []
ai_hand = []

def deal():
  for i in range(10):
    card = random.choice
    player_hand.append(card)
    cards.remove(card)
    card = random.choice
    ai_hand.append(card)
    cards.remove(card)
 
def turn1():
  card = random.choice
  cards.remove(card)
  print("Face-Up Card")
  print(card)
  if len(cards) == 0:
    turn2()
    
def turn2():
  print("card")
  
    
  
