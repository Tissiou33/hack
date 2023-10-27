import random
import string

mot_de_passe = input("Entrez un mot de passe de 4 lettres : ")
caracteres = string.ascii_lowercase
essais = 0

while True:
    essais += 1
    tentative = ''.join(random.choice(caracteres) for i in range(4))
    print(tentative)
    if tentative == mot_de_passe:
        print("Mot de passe trouvé en", essais, "essais.")
        break