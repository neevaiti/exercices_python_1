letter_ask_user = input("Veuillez saisir une lettre : ")

voyelle = ["a", "e", "i", "o", "u", "y"]

if letter_ask_user in voyelle:
    print(f"{letter_ask_user} est une voyelle.")
else :
    print(f"{letter_ask_user} n'est pas une voyelle, c'est une consonne.")