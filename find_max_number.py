number_1 = input("Veuillez saisir un premier nombre : ")
number_2 = input("Veuillez saisir un deuxième nombre : ")
number_3 = input("Veuillez saisir un troisième nombre : ")

if int(number_1) > int(number_2) and int(number_3):
    print(f"{number_1} est plus grand que {number_2} et {number_3}")

elif int(number_2) > int(number_1) and int(number_3):
    print(f"{number_2} est plus grand que {number_1} et {number_3}")

elif int(number_3) > int(number_1) and int(number_2):
    print(f"{number_3} est plus grand que {number_1} et {number_2}")

else :
    print("Oui oui baguette.")