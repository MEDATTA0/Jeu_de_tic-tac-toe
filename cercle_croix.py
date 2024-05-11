import turtle
import curses
import math

# Croix et cercle du turtle's graphics
def dessiner_cercle(x, y): #elle reçoit en x et y comme 
    rayon = 75
    turtle.speed(2)
    turtle.goto(x - 50, y - 50) # Il se déplacera à (x, y-75) pour effectuer un cercle complet
    turtle.pendown()
    turtle.circle(rayon)
    turtle.penup()

def dessiner_croix(x, y):
    cote = 150
    turtle.speed(0)
    turtle.goto(x-(cote/2), y-(cote/2)) #On va placer la tortue dans le coin (gauche, bas) de la case choisi
    turtle.setheading(0)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(cote*(math.sqrt(2)))
    turtle.penup()
    turtle.goto(x-(cote/2), y+(cote/2))
    turtle.right(90)
    turtle.pendown()
    turtle.forward(cote*(math.sqrt(2))) #Une croix est la représentation des 2 diagonales d'un carré dont la valeur = côté * sqrt(2) 
    turtle.penup()


#Rectangle et croix, houuuuuu; c'était chaud... :_(

def dessiner_rectangle(win, y, x):
    
    #lignes
    curses.window.addstr(win, y + 1, x + 2, '-' * 11)
    curses.window.addstr(win, y + 5, x + 2, '-' * 11)
    
    #colonne
    for i in range(2, 5):
        curses.window.addstr(win, y + i, x + 1, '|')
    for i in range(2, 5):
        curses.window.addstr(win, y + i, x + 13, '|')
    
def dessiner_crois(win, y, x):
    for i in range(1, 6):
        curses.window.addstr(win, y - i, (x + 2) + i, '  /')
    for i in range(1, 6):
        curses.window.addstr(win, (y - 6) + i, (x + 2) + i, '  \\')
