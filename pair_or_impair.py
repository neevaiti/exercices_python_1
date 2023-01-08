ask_user = input("Veuillez saisir un nombre : ")

# Faire une division entière
pair_or_impair = int(ask_user) % 2

# Si il y à un reste c'est un nombre impair
if pair_or_impair == 1:
    print(f"{ask_user} est un nombre impair")

# Sinon c'est un nombre pair
else :
    print(f"{ask_user} est un nombre pair")