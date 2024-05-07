from turtle import*
import math

def dessiner_cercle(x, y): #elle reçoit en x et y comme 
    rayon = 75
    speed(2)
    goto(x - 50, y - 50) # Il se déplacera à (x, y-75) pour effectuer un cercle complet
    pendown()
    circle(rayon)
    penup()

def dessiner_croix(x, y):
    cote = 150
    speed(0)
    goto(x-(cote/2), y-(cote/2)) #On va placer la tortue dans le coin (gauche, bas) de la case choisi
    setheading(0)
    left(45)
    pendown()
    forward(cote*(math.sqrt(2)))
    penup()
    goto(x-(cote/2), y+(cote/2))
    right(90)
    pendown()
    forward(cote*(math.sqrt(2))) #Une croix est la représentation des 2 diagonales d'un carré dont la valeur = côté * sqrt(2) 
    penup()