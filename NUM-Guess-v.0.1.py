import random

print("NMBR Guesser 3000\n")
print("Welocme! Let's play a game! With a winning chance of 1:10 \nIf you can guess the number computer thought of then you are pretty cool!")

pl_guess = input("Your number is:\n")
ai_guess = random.randint(1, 10)

if pl_guess == ai_guess:
  print(f"OMG! YOU DID IT! CORRECT! Indeed it was {ai_guess}!")
elif pl_guess == ai_guess - 1 or pl_guess == ai_guess + 1:
  print(f"That was pretty close! The number was {ai_guess}")
else:
  print(f"Naah... Actually it was {ai_guess}")