#introduction de la chaine de caracteres
chaine = "Je suis étudiant à l'USTHB, je me gare à l'USTHB, j'habite près de l'USTHB et je connais l'USTHB depuis 2 ans"

def rempalce(string,occurrence):            # fonction remplace avec deux paramatres(chaine et l'occurence) qui substitue l’occurrence du mot « USTHB » par le caractère #
    chainex =  ""                           # chainex = chaine sans virgules et sans apostrophes

    for char in string:                     # parcour de la chaine caractere par caractere
        if char in "',":                    # si on trouve une virgule ou bien une apostrophe on la remplace par un espace
            char = "  "
        chainex += char                     # chaine sans "'" et ","

    mots = chainex.split()                  # split() pour séparer la chaine a partir des espaces
    i = 0                                   # initialisation de i
    nouv_chaine = ""                        # initialisation de la nouvelle chaine

    for m in mots:                          # parcourir la chaine mot par moot
        if "USTHB" in m:                    # recherche de "USTHB"
            i+=1                            # incrementation de i
            if i == occurrence:             # l'occurence qu'on veut remplacer
                m = "#"                     # remplacemenet
        nouv_chaine += m + " "              # insertion des mots a la nouvelle chaine et les separer par un espace
    return nouv_chaine[:-1]                 # retourne de la nouvelle chaine obtenue avec la suppression du dernier espace

choix = input("Quelle occurence du mot 'USTHB' voulez-vous remplacer : ")
while True:                                 # boucle do while
    if choix not in ['1','2','3','4']:      # si l'utilisateur introduit quelleque chose qui n'appartient pas a 1,2,3,4 on demande de réintoduire le choix
        choix = input("'USTHB' a 4 occurences choisir un nombre entre 1 et 4 (1,2,3,4) s'il vous plait : ")
    else:                                   # si l'utilisateur introduit une chaine inclus dans la liste des chaines ['1','2','3','4'] on sort de la boucle do while
        break

choix = int(choix)                          # transformer la chaine de caractere obtenue par la methode input a un entier
print(rempalce(chaine,choix))               # l'appel de la fonction en utilisant la chaine ci dessus et l'occurence de "USTHB" qu'on veut remplacer