import random

digit = random.sample('0123456789',3)
match_number = ''.join(digit)
match_number = str(match_number)
guess_limit = 10
Turns = 0
will_continue= True
game_hint ="""I am thinking of a 3-digit number. Try to guess what it is.Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct."""
print(game_hint)
print(match_number)

clues = []

while will_continue:
    print("It's turn",Turns)
    print("You have",guess_limit-Turns,"left")
    guessed_number = str((input("Guess: \n")))
    if guessed_number == match_number:
        print("You have won")
        break
    Turns +=1
    for i in range(len(match_number)):
        if guessed_number[i] in match_number:
            if guessed_number[i] == match_number[i]:
                clues.append("Fermi")
            else:
                clues.append("Pico")
    if len(clues) == 0:
        clues.append("Bagels")
    print(','.join(clues))
    clues = []
    if Turns == guess_limit:
        will_continue = False
        
