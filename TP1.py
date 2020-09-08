# Sujet
#
# Le but de notre programme est de déterminer si une année saisie par l'utilisateur
# est bissextile. Il s'agit d'un sujet très prisé des enseignants en informatique
# quand il s'agit d'expliquer les conditions. Mille pardons, donc, à ceux qui ont
# déjà fait cet exercice dans un autre langage mais je trouve que ce petit programme
# reprend assez de thèmes abordés dans ce chapitre pour être réellement intéressant.
#
# Je vous rappelle les règles qui déterminent si une année est bissextile ou non
# (vous allez peut-être même apprendre des choses que le commun des mortels ignore).
#
# Une année est dite bissextile si c'est un multiple de 4, sauf si c'est un multiple
# de 100. Toutefois, elle est considérée comme bissextile si c'est un multiple de 400.
# Je développe :
#               Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
#               Si elle est multiple de 4, on regarde si elle est multiple de 100.
#                   Si c'est le cas, on regarde si elle est multiple de 400.
#                       Si c'est le cas, l'année est bissextile.
#                       Sinon, elle n'est pas bissextile.
#                   Sinon, elle est bissextile.

year = input("Enter a year : ")
year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is bisextile.")
        else:
            print("This year is not bisextile.")
    else:
        print("This year is bisextile.")
else:
    print("This year is not bisextile.")


# CORRECTION

annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
bissextile = False # On crée un booléen qui vaut vrai ou faux
                   # selon que l'année est bissextile ou non

if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile: # Si l'année est bissextile
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")


# OPTIMISATION

annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
