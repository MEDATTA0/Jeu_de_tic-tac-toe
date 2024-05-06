import turtle
import math

def dessiner_cercle(x, y): #elle reçoit en x et y comme 
    rayon = 75
    turtle.speed(5)
    turtle.goto(x, y-rayon) # Il se déplacera à (x, y-75) pour effectuer un cercle complet
    turtle.pendown()
    turtle.circle(rayon)
    turtle.penup()

def dessiner_croix(x, y):
    cote = 150
    turtle.speed(5)
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