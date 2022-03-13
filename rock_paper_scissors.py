import random

# definiamo variabili vincita utente e vincita PC
user_wins = 0
comp_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("type rock - paper - scissors or q to quit ").lower()
    # se ha scritto q
    if user_input == "q":
        break

    # verifico se ha scritto una delle 3 possibilità, se non lo ha fatto
    if user_input not in options:
        continue

    random_num = random.randint(0, 2)
    # rock = 1, paper = 1, scissors = 2
    computer_pick = options[random_num]
    print("- Computer picked " + computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("- You won")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("- You won")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("- You won")
        user_wins += 1
    elif user_input == computer_pick:
        print("- Draw")

    else:
        print("- you lost")
        comp_wins += 1

print("you won " + str(user_wins) + " times")
print("Computer won " + str(comp_wins) + " times")
