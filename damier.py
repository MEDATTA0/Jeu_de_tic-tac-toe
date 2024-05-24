import curses
import turtle
# Quelque soit le déplacement fait, la tortue garde toujours la même direction qu'on lui donne. Donc il faut la faire tourner
# dans le bon sens

#Fonction pour le damier dans turtle
def afficher_damier():
    turtle.setup(700, 700)
    turtle.penup()
    dessiner_verticalement()
    dessiner_horizontalement()

def dessiner_verticalement():
    turtle.speed(5)
    turtle.goto(-100, 300) #Il se place pour le 1re droite
    turtle.right(90) #Il tourne en direction du bas
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(100, 300) # 2e droite
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()

    
def dessiner_horizontalement():
    turtle.speed(5)
    turtle.goto(-300, 100) # 1re droite
    turtle.left(90)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-300, -100) # 2e droite
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()


#Fonctions pour le jeu de tic tac toe sur terminal
x_moves = [5, 9, 13, 17]
y_moves = [5, 7, 9, 11]



def dessiner_grille(win):
    win.clear()
    
    #On va afficher les coordonnées, a, b, c et 1, 2, 3
    c = ord('a')
    k = 0
    for i in x_moves:
        for j in range (5, 11):
            if j == 5 and k < 3 : 
    #On crée une condition pour insérer le répère en même temps qu'on construit le damier
    #k < 3 pour arrêter après avoir écrit a, b et c
                curses.window.addstr(win, 4, i + 2, chr(c + k))
                k += 1 
            curses.window.addstr(win, j, i, '|')
        
    c = ord('1')
    k = 0 
    for j in y_moves:
        if k < 3 :
            curses.window.addstr(win, j + 1, 3, chr(c + k))
            k += 1
        curses.window.addstr(win, j, 5, '-' * 12)

"""    #curses.window.move(win, 5, 20)
    for i in range(5, 10):
        if i != 7 or i != 9:
            curses.window.addstr(win, i, 8, '|')
    
    #curses.window.move(win, 5, 35)
    for i in range(5, 10):
        if i != 7 or i != 9:
            curses.window.addstr(win, i, 11, '|')

    #curses.window.move(win, 11, 5)
        curses.window.addstr(win, 6, 5, '-' * 17)
    
    #curses.window.move(win, 17, 5)
        curses.window.addstr(win, 8, 5, '-' * 17)
"""

#afficher_damier()
#turtle.done()
