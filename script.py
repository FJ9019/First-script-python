#coding:utf-8

import random

val_min = 1
val_max = 60

mystere = random.randint(val_min, val_max)

essai = 1
score = 100

loop = True

while loop: 
    valeur_utilisateur = input(f"Veuillez Entrez une valeur comprise entre {val_min} et {val_max} !")

    valeur_int = int(valeur_utilisateur)

    if essai <= 10:
       if valeur_int > mystere:
           print("Plus grand que le nombre mystere")
           essai += 1
           score -= 10
       elif valeur_int < mystere:
           print("Plus petit que le nombre mystere")
           essai += 1
           score -= 10
       else:
           print(f"Félicitation vous avez trouvé le nombre mystère, le nombre mystère est {valeur_int}")
           print(f"Nombre d'essais : {essai} \nSCore : {score}")
           loop = False
    else:
        loop = False
        print(f"Désolé vous avez manqué le nombre mystère, c'était {mystere}")       
        print(f"Nombre d;essais : {essai} \nScore : {score}")         