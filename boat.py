import turtle

# Je veux que ma tortue dessine un bateau

turtle.pendown() # La tortue va dessiner
turtle.forward(200) # Avance de 200px

turtle.left(120) # Tourne à gauche à un angle de 120 degré
turtle.forward(200) # Avance de 200px

turtle.right(210) # Tourne à droite à un angle de 210 degré
turtle.forward(175) # Avance de 180px

turtle.penup() # Relève le stylo qui va arrêter le dessin de la tortue

turtle.right(90) # Tortue tourne à 90 degré à droite
turtle.forward(100) # Tortue avance de 100px

turtle.pendown() # La tortue va dessiner
turtle.right(120) # prend en angle vers la droite de 90degré
turtle.forward(200) # Avance de 200px


################---- ETAPE 2 ----################

# Maintenant nous voulons dessiner le trapèze
turtle.penup() # La tortue arrête de dessiner

turtle.right(150) # tortue prend un angle de 90 degré à droite
turtle.forward(180) # Avance de 190px

turtle.right(90) # tortue part à droite en angle de 90 degré
turtle.forward(100) # Avance de 100px

turtle.right(180) # Ma tortue fait demi-tour
turtle.pendown() # La tortue va dessiner

turtle.forward(200) # Avance de 200px

turtle.right(125) # Prend un angle de 125 degré à droite
turtle.forward(75) # Avance de 75px

turtle.right(55) # Prend un angle de 75 degré
turtle.forward(125) # Avance de 125px

turtle.right(62.5) # Prend un angle de 62.5 degré
turtle.forward(75) # Avance de 75px

turtle.done() # Affiche le dessin