#!/usr/bin/env python3
#coding utf8

import damier
import cercle_croix
import turtle
import argparse
import curses


parser = argparse.ArgumentParser(description= "Jeu_de_tic_tac_toe")
parser.add_argument("--choice", "-c", dest= "choice", help=" \nPerso, je vous avoue que c'est pas joli :( ", required= False)
parser.add_argument("--help", "-h", help="Affiche la page d'aide :) \nPar défaut, si aucun argument n'est pris, alors le jeu sera joué dans le turtle de python\n")

args = parser.parse_args()

#n = 'y'
#while n == 'y':

print("Le Player1 a les croix et le Player2 a les cercles.\n Lorsque c'est le tour d'un joueur, il entre successivement les coordonnées (x, y) de son déplacement.")
print("Les cases sont numérotés du haut vers le bas (1, 2, 3) et de la gauche vers la droite (a, b, c)")
input("Appuyer sur ENTREE pour commencer le jeu.")
    

if args.choice == "-t" or  args.choice == "--turtle":
    coordonnees = { 'a' : -200, 'b' : 0, 'c' : 200, '1' : 200, '2' : 0, '3' : -200 }
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
#n = input("******************Le jeu est terminée*******************************\n Voulez-vous recommencer (y/n) : ")
print("********************LA PARTIE EST TERMINÉE************************************\n")

if args.choice == "-T" or args.choice == "--Terminal":

    moves = {'a' : 5, 'b' : 11, 'c' : 17, '1' : 5, '2' : 20, '3' : 35 }
    curses.initscr()
    win = curses.newwin(75, 75, 0, 0)
    #Dessiner la grille
    damier.dessiner_grille(win)        
    #Que le jeu commence !
    for i in range(0, 9):
        #La valeur qu'il va entrer sera directement traitée en correspondance dans le dictionnaire
        if i % 2 != 0:
            x = input("PLAYER1 : \n x = ")
            x = coordonnees[x]
            y = input(" y = ")
            y = coordonnees[y]
            cercle_croix.dessiner_rectangle(win, y, x)
        
        else:
            x = input("PLAYER2 : \n x = ")
            x = coordonnees[x]
            y = input(" y = ")
            y = coordonnees[y]
            cercle_croix.dessiner_croix(win, y, x)
        
        curses.window.refresh(win)

    curses.window.getch(win)
    curses.endwin()
    print("****************************LA PARTIE EST TERMINÉE*******************************\n")
    




        