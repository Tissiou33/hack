import random
from num2words import num2words

print(str(random.randint(1,500)))

mot_passe = input("Entré un mot de passe d'au plus 4 lettre ")
def mot (mot_passe):
    if len(mot_passe) > 4:
        le_mot = ""
        n = 1
        for i in mot_passe :
            n += 1 
            le_mot = le_mot + i
            if n ==5 : break
        return(le_mot)
    else : 
        le_mot = mot_passe 
        return le_mot
    
liste = []
for i in range(5):
    chiffre = random.randint(1,2500)
    chiffre = num2words(chiffre , lang='fr')
    liste.append(chiffre)
    for i in range(5):
        ch = random.randint(1,2500)
        ch = num2words(ch , lang='fr')
        chiffre = chiffre + ch 
        liste.append(chiffre)
        for i in range(5):
            ch = random.randint(1,2500)
            ch = num2words(ch , lang='fr')
            chiffre = chiffre + ch 
            liste.append(chiffre)
            for i in range(5):
                ch = random.randint(1,2500)
                ch = num2words(ch , lang='fr')
                chiffre = chiffre + ch 
                liste.append(chiffre)

mot_passe = mot(mot_passe)     
print(f" le mot de passe entré est {mot_passe}")     
for el in liste:
    print(el)
    if(el == mot_passe):
        print(f" le programme a trouvé le mot de passe ({el})")
else:
    print("Dommage ")
    