tuile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1er 0 est un dépotoire en cas de saisie invalid
exc = [" ", "x", "o"]                   # sxc veut dire : espace, x et cercle
tour = 0
joueur = 1                              # joueur 1 = x ; joueur 2 = o (ça pointe directement à la liste «exc»)
while 1 == 1:            # ceci loop le jeu jusqu'à ce qu'il reçoit la command «break»
  print("""


  """)
  print("                  Exemple")
  print(f"{exc[tuile [7]]} ║ {exc[tuile [8]]} ║ {exc[tuile [9]]}        7 ║ 8 ║ 9")
  print("══╬═══╬══        ══╬═══╬══")
  print(f"{exc[tuile [4]]} ║ {exc[tuile [5]]} ║ {exc[tuile [6]]}        4 ║ 5 ║ 6")
  print("══╬═══╬══        ══╬═══╬══")
  print(f"{exc[tuile [1]]} ║ {exc[tuile [2]]} ║ {exc[tuile [3]]}        1 ║ 2 ║ 3")
  print("")

  for x in "y":                             # permet au jeu de montrer la grille du gagnant avant de terminer
    if (tuile[1] == tuile[2] and tuile[1] == tuile[3]) and tuile[1] != 0:
      print(f" {exc[tuile[1]]} GAGNE")      # le code en haut compare trois valeurs sur la grille et répète 7 fois
      tour = 10                                 # ceci évite le message «MATCH NUL» à la fin
      break                                     # j'ai inclue cet command en cas de gagnant double 
    """
      ║   ║  
    ══╬═══╬══
      ║   ║  
    ══╬═══╬══
    1 ║ 2 ║ 3
    """
    if (tuile[4] == tuile[5] and tuile[4] == tuile[6]) and tuile[4] != 0:
      print(f" {exc[tuile[4]]} GAGNE")
      tour = 10
      break
    """
      ║   ║  
    ══╬═══╬══
    4 ║ 5 ║ 6
    ══╬═══╬══
      ║   ║  
    """
    if (tuile[7] == tuile[8] and tuile[7] == tuile[9]) and tuile[7] != 0:
      print(f" {exc[tuile[7]]} GAGNE")
      tour = 10
      break
    """
    7 ║ 8 ║ 9
    ══╬═══╬══
      ║   ║  
    ══╬═══╬══
      ║   ║  
    """
    if (tuile[1] == tuile[4] and tuile[1] == tuile[7]) and tuile[1] != 0:
      print(f" {exc[tuile[1]]} GAGNE")
      tour = 10
      break
    """
    7 ║   ║  
    ══╬═══╬══
    4 ║   ║  
    ══╬═══╬══
    1 ║   ║  
    """
    if (tuile[2] == tuile[5] and tuile[2] == tuile[8]) and tuile[2] != 0:
      print(f" {exc[tuile[2]]} GAGNE")
      tour = 10
      break
    """
      ║ 8 ║  
    ══╬═══╬══
      ║ 5 ║  
    ══╬═══╬══
      ║ 2 ║  
    """
    if (tuile[3] == tuile[6] and tuile[3] == tuile[9]) and tuile[3] != 0:
      print(f" {exc[tuile[3]]} GAGNE")
      tour = 10
      break
    """
      ║   ║ 9
    ══╬═══╬══
      ║   ║ 6
    ══╬═══╬══
      ║   ║ 3
    """
    if (tuile[1] == tuile[5] and tuile[1] == tuile[9]) and tuile[1] != 0:
      print(f" {exc[tuile[1]]} GAGNE")
      tour = 10
      break
    """
      ║   ║ 9
    ══╬═══╬══
      ║ 5 ║  
    ══╬═══╬══
    1 ║   ║  
    """
    if (tuile[3] == tuile[5] and tuile[3] == tuile[7]) and tuile[3] != 0:
      print(f" {exc[tuile[3]]} GAGNE")
      tour = 10
      break
    """
    7 ║   ║  
    ══╬═══╬══
      ║ 5 ║  
    ══╬═══╬══
      ║   ║ 3
    """

  if tour == 9:               # termine le jeu quand la grille est remplie (après 9 tours)
    print("MATCH NUL")
    break
  if tour == 10:              # termine le jeu sans le message «MATCH NUL» (si quelqu'un gagne)
    break
  print("Joueur " + exc[joueur])
  try:
    player_tile = int(input("Choisissez votre cadre: "))
  except ValueError:                                                    # verifie pour des saisies non-entier
    player_tile = 0
  if player_tile < 1 or player_tile > 9 or tuile [player_tile] > 0:     # verifie pour des entiers hors la liste
    player_tile = 0
    print("")
    print("VALEUR INVALID!")
    valeur_inutile = input("Appuyez sur Entrée pour continuer: ")
  else:
    tuile [player_tile] += joueur     # change la tuile correspondante en x ou o
    tour += 1                         # augmente la valeur du tour
    joueur = tour % 2 + 1             # change le joueur basé sur le tour


"""
quelques échantillons pour copiés/collés :
│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌
  ║   ║  
══╬═══╬══
  ║   ║  
══╬═══╬══
  ║   ║  
"""