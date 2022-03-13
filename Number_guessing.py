import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 5:
        print('Please type a number at least equal to 5')
        quit()
else:
    print('Please type a number next time.')
    quit()

# calcolo numero random
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    # --------------------gestisce il dato inserito ----------------------
    user_guess = input("Make a guess: ")
    # verifica che sia un numero
    if user_guess.isdigit():
        # lo trasforma in un int perchè input da una string
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    # --------------------gestisce il dato inserito ----------------------

    # --------------------fa il controllo con il numero rand ----------------------
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
    # --------------------fa il controllo con il numero rand ----------------------

print("You got it in", guesses, "guesses")
