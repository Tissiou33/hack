from random import *
import os
import time

mot_passe = input("Entrer le mot de passe: ")
pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
       'o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,
       4,5,6,7,8,9,0,'A','B','C','D','E','F','G','H','i','J','K','L',
       'M','N','o','P','Q','R','S','T','U','W','X','Y','Z','@','_','']

password = ""
debut = time.time()

while password != mot_passe:
    password = ''
    i = 0
    for letter in range(len(mot_passe)):
        suivt = pwd[randint(0,63)]
        password = str(suivt) + str(password)
        i +=1 
        print(password)
        print("hacking du mot de passe ---- grrrrr")
        os.system("cls")
        
fin = time.time()
duré = (fin - debut) /60
print(f"Your pass mot is : {password}  apres {i} tentatives et {duré} minutes" )
