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
def dessiner_grille(win):
    win.clear()
    
    #curses.window.move(win, 5, 20)
    for i in range(5, 24):
        if i != 11 or i != 17:
            curses.window.addstr(win, i, 20, '|')
    
    #curses.window.move(win, 5, 35)
    for i in range(5, 24):
        if i != 11 or i != 17:
            curses.window.addstr(win, i, 35, '|')

    #curses.window.move(win, 11, 5)
        curses.window.addstr(win, 11, 5, '-' * 45)
    
    #curses.window.move(win, 17, 5)
        curses.window.addstr(win, 17, 5, '-' * 45)


#afficher_damier()
#turtle.done()
