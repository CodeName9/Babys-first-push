print("Bienvenue au fabricateur de triangle isocèle.")
print("© Gabriel Lavallée")
print("")
while 1 == 1: 
    rangée = int(input("Combien de rangée voulez-vous? "))
    rangée2 = 0
    print("")
    if rangée >= 2:
        while rangée >= 2:
            print(rangée * " " + "/" + rangée2 * " " + "\ ")
            rangée -= 1
            rangée2 += 2
        print(rangée * " " + "/" + rangée2 * "_" + "\ ") # La rangée avec underscore
        print("")
        print("Voici votre triangle isocèle!")
        dummy_value = input("Appuyez sur Entrée pour fabriquer un nouveau trianlge. ")
        print("")
        print("")
        print("")
        print("")
        print("")
    else:
        print("Choisissez une valeur plus grande que 1!")
        dummy_value = input("Appuyez sur Entrée pour fabriquer un nouveau trianlge. ")
        print("")
        print("")
        print("")
        print("")