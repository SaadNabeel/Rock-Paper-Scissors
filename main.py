import random
choice = random.choice(["Rock", "Paper", "Scissor"])
user = input("Select either Rock, Paper, or Scissor: ")
print("Computer:", choice)
print("User:", user)

if choice == user:
    print("ITS A TIE")
elif user == "paper":
    print("COMPUTER WINS")
else:
    print("USER WINS")
    
if choice == "scissor":
    print("COMPUTER WINS")
else:
    print("USER WINS")

