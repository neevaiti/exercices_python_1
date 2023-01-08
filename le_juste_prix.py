import random

random_number = random.randint(0, 99999) #On définit une range pour un nombre aléatoire
user_number = 0 # On définit à l'avance la valeur de user_number en integer

while user_number != random_number: # Ici on fait appel à une boucle while car on ne sait pas combien de fois environ nous allons devoir faire appel à cette boucle
    user_number = int(input("Quel est le Juste prix : ")) # On redéfinit user_number sous forme d'input pour faire intéragir l'utilisateur tout en convertissant l'input en integer
    if user_number < random_number: # Une condition dans le while, si user_number est plus petit que le nombre aléatoire alors "c'est plus"
        print("C'est plus.")
    elif user_number > random_number: # Sinon si user_number est plus grand que le nombre aléatoire alors "c'est moins"
        print("C'est moins.")

print(f"{user_number} EST le JUSTE PRIX !") # Si on trouve le nombre aléatoire on sort directement de la boucle donc pas besoin d'inclure ce print dans la boucle.