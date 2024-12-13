#coding:utf-8

mystere = 34

loop = True

while loop: 
    valeur_utilisateur = input("Veuillez Entrez une valeur comprise entre 1 et 40 !")

    valeur_int = int(valeur_utilisateur)

    if valeur_int > mystere:
        print("Plus grand que le nombre mystere")
    elif valeur_int < mystere:
        print("Plus petit que le nombre mystere")
    else:
        print(f"Félicitation vous avez trouvé le nombre mystère, le nombre mystère est {valeur_int}")