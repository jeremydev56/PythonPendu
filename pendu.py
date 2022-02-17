from getpass import getpass

# Le mot de passe
mot = getpass("Entrez votre mot ")


liste=[]
votre_liste=[]

for x in mot:
    # affiche chaque lettre du mot
    liste.append(x)
    # on ajoute x à la liste
    votre_liste.append('*')
    # et ajoute à la "votre_liste" le nombre d'étoiles correspondant à la longueur du mot choisi !
    
print("".join(votre_liste))
# cela afiche le mot ... mais caché !


# Une nouvelle variable : le nombre d'erreurs
nb_erreur = 0
while nb_erreur < 9:
    # tant que le nombre d'erreurs est inférieur à 9
    lettre = input("entrez votre lettre ")
    # l'utilisateur peut entrer sa lettre

    if len(lettre)>1:
        # si la longueur de la lettre est supérieure à 1
        if lettre == mot:
            # si la lettre correspond au mot choisi
            print("Vous avez trouvé ")
            break
        
    if lettre in liste:
        # si la lettre est dans la liste
        for (x,y) in enumerate(liste):
            # x = index / y = valeur
            #(AZE : x=0 & y=a, x=1 & y=z, x=2 & y=e)
            if x == lettre:
                votre_liste[index] = x
        v = "".join(votre_liste)
        print("C'est la bonne lettre", v)

        # si la liste est égale à notre liste
        if liste==votre_liste:
            print("Vous avez trouvé ")
            break
        

    else :
        # si pas la bonne lettre trouvée
        nb_erreur +=1
        print('Mauvaise lettre : il vous reste %s essai(s)'%(9-nb_erreur))

if nb_erreur == 9:
    print("Vous avez perdu ! ")

            
            
