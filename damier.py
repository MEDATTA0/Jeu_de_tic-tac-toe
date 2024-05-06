import turtle
# Quelque soit le déplacement fait, la tortue garde toujours la même direction qu'on lui donne. Donc il faut la faire tourner
# dans le bon sens
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

#afficher_damier()
#turtle.done()
