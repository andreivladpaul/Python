from math import floor


print("Welcome to Copmputer Quiz")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("ok let's play")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " right answers")
print("You got " + str(floor(score / 2 * 100)) + "%")
