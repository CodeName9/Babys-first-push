areas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1st 0 is a garbage dump in case of invalid inputs
sxc = [" ", "x", "o"]                   # sxc stands for: space, x and circle
turn = 0
player = 1                              # player 1 = x ; player 2 = o
tile_1 = 1
tile_2 = 2
tile_3 = 3
x = 3
y = 3
z = 3
timer = 0
while 1 == 1:            # this lets the game keep going until the break command
  print("""


  """)
  print("                  Exemple")
  print(f"{sxc[areas [7]]} ║ {sxc[areas [8]]} ║ {sxc[areas [9]]}        7 ║ 8 ║ 9") # 1st row
  print("══╬═══╬══        ══╬═══╬══")
  print(f"{sxc[areas [4]]} ║ {sxc[areas [5]]} ║ {sxc[areas [6]]}        4 ║ 5 ║ 6") # 3rd row
  print("══╬═══╬══        ══╬═══╬══")
  print(f"{sxc[areas [1]]} ║ {sxc[areas [2]]} ║ {sxc[areas [3]]}        1 ║ 2 ║ 3") # 5th row
  print("")

  while timer < 7:
    if (areas[tile_1] == areas[tile_2] and areas[tile_1] == areas[tile_3]) and areas[tile_1] != 0:
      print(f" {sxc[areas[tile_1]]} GAGNE")     # the code above compares three values on the board and repeats 7 times
      turn = 10                                 # this changes the ending message
      break                                     # this stops the check, i don't think its necessary but ikd
    else:
      tile_1 += x                               # changes the tiles to check (horizontal)
      tile_2 += y
      tile_3 += z
      timer += 1
      if timer == 2:                            # after checking 3 rows, it switchs to columns
        x = 1
        y = 1
        z = 1
        tile_3 = 7
        tile_2 = 4
        tile_1 = 1
      elif timer == 5:                          # after cheking 3 columns, it switchs to diagonal
        tile_3 = 9                              # PS. the code for diagonal is very improvised and dumb
        tile_2 = 5
        tile_1 = 1
        x = 2
        y = 0
        z = -2
  timer = 0             # resets the values of all checking tools so the process can repeat each turn
  tile_1 = 1
  tile_2 = 2
  tile_3 = 3
  x = 3
  y = 3
  z = 3

  if turn >= 9:               # ends the game when the grid is filled (after 9 turns)
    if turn == 10:            # ends the game without the MATCH NUL message (if someone wins)
      break
    print("MATCH NUL")
    break
  print("Joueur " + sxc[player])
  try:
    player_tile = int(input("Choisissez votre cadre: "))
  except ValueError:                                                    # checks for non-integer values
    player_tile = 0
  if player_tile < 1 or player_tile > 9 or areas [player_tile] > 0:     # checks for invalid integer values
    player_tile = 0
    print("")
    print("VALEUR INVALID!")
    dummy_value = input("Appuyez sur Entrée pour continuer: ")
  else:
    areas [player_tile] += player     # turns the corresponding area into x or o
    turn += 1                         # increments the turn value
    player = turn % 2 + 1             # changes players based on the turn



"""
a few copy/paste samples:
│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌
  ║   ║  
══╬═══╬══
  ║   ║  
══╬═══╬══
  ║   ║  
"""