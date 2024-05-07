import damier
import cercle_croix
import turtle

coordonnees = { 'a' : 200, 'b' : 0, 'c' : -200, '1' : 200, '2' : 0, '3' : -200 }

n = 'y'
while n == 'y':
    print("Le Player1 a les croix et le Player2 a les cercles.\n Lorsque c'est le tour d'un joueur, il entre successivement les coordonnées (x, y) de son déplacement.")
    input("Appuyer sur ENTREE pour commencer le jeu.")

    #On affiche le damier
    damier.afficher_damier()

    for i in range(0, 9):
        #La valeur qu'il va entrer sera directement traitée en correspondance dans le dictionnaire
        if i % 2 != 0:
            x = input("PLAYER1 : \n x = ")
            x = coordonnees[x]
            y = input(" y = ")
            y = coordonnees[y]
            cercle_croix.dessiner_cercle(x, y)
        
        else:
            x = input("PLAYER2 : \n x = ")
            x = coordonnees[x]
            y = input(" y = ")
            y = coordonnees[y]
            cercle_croix.dessiner_croix(x, y)

    turtle.done()
    n = input("******************Le jeu est terminée*******************************\n Voulez-vous recommencer (y/n) : ")
