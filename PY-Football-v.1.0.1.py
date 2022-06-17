import random

# Emojis: ⚽️ ✋ 🤚 👊 💥 ⭐️
print("Welcome to 'PY-Penalties' v.1.0.1\n")

row1 = ["🔳","🔳","🔳"]
row2 = ["🔳","🔳","🔳"]
row3 = ["🔳","🔳","🔳"]

gate = [row1, row2, row3]

# Team Names
ai_team_name = "PY-Keeper"
pl_team_name = ""

# Team Score
ai_score = 0
pl_score = 0

# Rounds Counter
round_number = 1

# Wrap Game Gates visualizing into function
def gates_view():
  print("     1     2     3")
  print(f"1  {row1}\n2  {row2}\n3  {row3}")

# GAME Starts
gates_view()

print("\nYou are going to do penalties versus Computer! \nAim the ball using coordinates: 'Y' for columns and 'X' for rows. \n(f.e. '11' - You hit top-left corner. '32' - middle bottom) \nIf you score you get point, if computer stops the ball then it gets point. \nGame continues up to 10 Goals.")

pl_team_name = input("\nPlease name your team to begin: ")

# Game process looped till 10 goals 
while (ai_score < 10) and (pl_score < 10):
  
  print(f'''
⦿-------------------------------⦿
              
  MATCH: "{ai_team_name}" VS. "{pl_team_name}"
  ROUND: {round_number}
  SCORE: {ai_score} : {pl_score}
        ''')
  
  # PLAYER Set Coordinates:
  player_aim = input("  Aim the ball: ")
  
  pl_y = int(player_aim[0]) - 1
  pl_x = int(player_aim[1]) - 1
  
  # COMPUTERS Set Coordinates:
  # First — Generate separate 'X' and 'Y' coordinate generator to be able to use it for both Left(x) and Right(x+1) hands
  ai_y_coordinate = int(random.randint(0, 2))
  ai_x_coordinate = int(random.randint(0, 1)) # It's (0, 1) Cuz we need to leave space for Right hand, right?
  
  # Then — Use random pre-generated coordinates:
  ai_left_hand_y = ai_y_coordinate
  ai_left_hand_x = ai_x_coordinate
  
  ai_right_hand_y = ai_left_hand_y
  ai_right_hand_x = ai_left_hand_x + 1
  
  # Comparison goes here::
  # IF Keeper Saves:
  if (pl_y == ai_left_hand_y and pl_x == ai_left_hand_x) or (pl_y == ai_left_hand_y and pl_x == ai_right_hand_x):
    ai_score += 1
    gate[ai_left_hand_y][ai_left_hand_x] = "✋"
    gate[ai_right_hand_y][ai_right_hand_x] = "🤚"
    gate[pl_y][pl_x] = "👊"
    gates_view()
    print('''
💥💥💥 Saved by the Keeper! 💥💥💥''')
  # IF Player Scores:
  else:
    pl_score += 1
    gate[ai_left_hand_y][ai_left_hand_x] = "✋"
    gate[ai_right_hand_y][ai_right_hand_x] = "🤚"
    gate[pl_y][pl_x] = "⚽️"
    gates_view()
    print('''
⭐️⭐️⭐️ NICE SHOT! ⭐️⭐️⭐️''')
  # Updating score:
  round_number += 1
  # Restoring gates before next round:
  gate[ai_left_hand_y][ai_left_hand_x] = "🔳"
  gate[ai_right_hand_y][ai_right_hand_x] = "🔳"
  gate[pl_y][pl_x] = "🔳"
  
# After game ends (after someone scores 10 goals):
if pl_score > ai_score:
  game_winner = pl_team_name
else:
  game_winner = ai_team_name
print(f"\nAfter {round_number} rounds, with a score of {ai_score} : {pl_score} the winner is '{game_winner}'")

