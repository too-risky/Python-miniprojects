#Rock Paper Scissors

import random 

options = ("rock", "paper", "scissors")
comp = random.choice(options)
player = None

while player not in options :
    player = input("Choose (rock/paper/scissor) : ")


print(f"user : {player}")
print(f"computer : {comp}")

if player == comp :
    print("TIE")
elif player == "rock" and comp == "scissors" :
    print("YOU WIN")
elif player == "rock" and comp == "paper" :
    print("COMPUTER WIN")
elif player == "paper" and comp == "rock" :
    print("YOU WIN")
elif player == "paper" and comp == "scissors" :
    print("COMPUTER WIN")
elif player == "scissors" and comp == "paper" :
    print("YOU WIN")
elif player == "scissors" and comp == "rock" : 
    print("COMPUTER WIN")
