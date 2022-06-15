import random

print('''
|***********************************|
|                                   |
|         NMBR Guesser 3000         |
|                                   |
|***********************************|
''')
print("Welocme! Let's play a game! \nGuess the number computer keeps in mind!")
while True:
  attempts = 0
  while True:
    pl_guess = input("\nYour number is: ") 
    # Check is needed
    pl_guess = int(pl_guess)
    ai_guess = random.randint(1, 10)
      
    attempts += 1
  
    if pl_guess == ai_guess:
  
      # Chance is 1:10
      # Attempts is N
      # Accuracy(%) = 100% / Attempts
      
      accuracy = (100 // attempts)
      score = 1000 - attempts * 50
      print(f'''
          
  |*****************************************
  |          
  |  YOU WON! GAME OVER! CONGRATULATIONS!
  |         
  |*****************************************
  |          
  |  It took you {attempts} attemps!
  |  
  |  YOUR SCORE: {score} / 1 000
  |
  |***************************************** 
      ''')
      break
      
    elif pl_guess < 0:
      print(f"Did you see 'minus' symbol in condition?")
      continue
      
    elif pl_guess == 0:
      null_guess_statements = ["Is it becasue you love donuts you wrote '0'?", "Cool number though but you gotta pick between 1 and 10.", "0 number is cool, but please stick to the rules: From 1 to 10"]
      print(null_guess_statements[random.randint(0,2)])
      continue
      
    elif (pl_guess == ai_guess - 1) or (pl_guess == ai_guess + 1):
      print (f"So close! So close! It was {ai_guess}")
      continue
      
    elif pl_guess > 10:
      print(f"Sorry, your computer can't count after 10 :(")
      continue
      
    elif pl_guess != ai_guess:
      wrong_guess_statements = [f"Nah, better luck next time! Computer chose {ai_guess}.", f"Cool number, but was {ai_guess} it.", f"Nah, it was {ai_guess}.", f"Computer chose {ai_guess}.", f"It was {ai_guess} this time."]
      print(wrong_guess_statements[random.randint(0,4)])
      continue
      
    else:
      print("ERROR")
  
  replay = input("Want to play again? Y or N\n")
  replay = replay.lower()
  if replay == "y":
    print("\n\nGAME CONTINUES\n\nWhat's your next number?\n")
    continue
  elif replay == "n":
    exit("Good Bye!")
  else:
    print("\nInvalid input but I'll take it as 'Yes'\n")
    continue
