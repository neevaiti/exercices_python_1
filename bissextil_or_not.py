year_ask_user = input("Veuillez saisir une année : ")

divisible_4_et_400 = (int(year_ask_user) % 4 and int(year_ask_user) % 400 or not int(year_ask_user) % 100)
#On vérifie si l'année est divisible par 4 & 100 mais elle ne doit pas l'être par 400

if int(divisible_4_et_400) == 0:
    # Si elle est bien divisible par 4 & 100 donc avec un reste de 0, elle est bien une année bissextile
    print(f"{year_ask_user} est une année bissextile.")

else :
    # Sinon quand il reste quelque chose autre que 0 ET que l'année peut-être divisble par 400, c'est forcément une année non bisextile
    print(f"{year_ask_user} n'est pas une année bissextile.")

# Cherche mon chiffre