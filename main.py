import random
from art import logo
from art import vs
from game_data import data
from replit import clear
end_game= False
final_score=False
score=0
num_A=random.randint(0,len(data)-1)
num_B=random.randint(0,len(data)-1)


if num_A==num_B:
  while num_A==num_B:
    num_B=random.randint(0,len(data)-1)


while not end_game:
  # Functions for difference
  
  def diff_B():
    global num_A
    global num_B
    if num_A==num_B:
      while num_A!=num_B:
        num_B=random.randint(0,len(data)-1)
      return
  def diff_A():
    global num_A
    global num_B
    if num_A==num_B:
      while num_A!=num_B:
        num_A=random.randint(0,len(data)-1) 
      return
  
  # Score
  
  def scr():
    global end_game
    if score>0:
      if final_score==True:
        print(logo)
        print(f"Sorry that's wrong.Final score: {score}")
        end_game=True
      else:
        print(f"You're right.current score: {score}")
    
  
  comp_a=data[num_A]
  comp_b=data[num_B]
  print(logo)
  scr()
  print(f"Compare A: {comp_a['name']}, {comp_a['description']}, {comp_a['country']} {comp_a['follower_count']}")
  print(vs)  
  print(f"Compare B: {comp_b['name']}, {comp_b['description']}, {comp_b['country']} {comp_b['follower_count']}")  
  y_ans=input("Who has more followers? Type 'A' or 'B': ").upper()
  
  
  # check the answer
  
  if y_ans=='A':
    if comp_a['follower_count']>comp_b['follower_count']:
      score+=1
      num_B=random.randint(0,len(data)-1)
      diff_B()
      
    else:
      if score==0:
        print(logo)
        print(f"Sorry that's wrong.Final score: {score}")
        end_game=True
      else:
        final_score=True
        end_game=True
        scr()
      
  elif y_ans=='B':
    if comp_a['follower_count']<comp_b['follower_count']:
      score+=1
      num_A=num_B
      num_B=random.randint(0,len(data)-1)
      diff_B()
      
    else:
      if score==0:
        print(logo)
        print(f"Sorry that's wrong.Final score: {score}")
        end_game=True
      else:
        final_score=True
        end_game=True
        scr()
  clear()
print(logo)
print(f"Sorry that's wrong.Final score: {score}")    

  
  