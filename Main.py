"""
Retrouvez ce projet sur github - https://github.com/Rooomaan/Lancers-de-d-s-NSI-projet/blob/main/Main.py

à savoir :
- Les points d'exclamation (!)
- Les points d'interrogation (?)
- Les "Todo"
sont une mise en forme pour une coloration syntaxique de l'extension "Better Comments" sur VSCode pour une meilleure lecture.
"""



#! Import des modules
import random

#! Fonctions

#todo# parametre nombre_de_lancers: Nombre de lancers de dés à simuler.
def lancers(nombre_de_lancers=8):
    """Simule 8 lancers de dés."""

    # liste principale qui a les résultats des lancers de dés.
    liste = []
    
    for i in range(nombre_de_lancers):
        # Utilisation de random.randint(1, 6) pour avoir un nombre aléatoire entre 1 et 6 et le mettre dans une liste.
        liste.append(random.randint(1, 6))

    return liste


def tour():
    """Simule un tour de jeu pour un joueur."""

    score = 0
    lancer = lancers()
    nb_de_5 = 0
    # On parcours la liste pour compter le nombre de 5
    for i in lancer:
        if i == 5:
            nb_de_5 += 1
        else:
            nb_de_5 += 0
    # On utilise le nombre de 5 pour le mettre en score suivant les règles:
    # un seul 5 -> +0 pts, plus ou égal a 2 -> +1 pts, zéro 5 -> -1 pts
    if nb_de_5 == 0:
        score -= 1
    elif nb_de_5 == 1:
        score += 0
    elif nb_de_5 >= 2:
        score += 1
    # Retourne sous forme de tuple les résultats
    return score, nb_de_5, lancer



#! Asserts obligatoires

#? Test de la fonction lancers()
assert len(lancers(32)) == 32, "lancers(32) doit retourner une liste de 32 nombres."
assert len(lancers(6)) == 6, "lancers(32) doit retourner une liste de 6 nombres."




#! Initiation des valeurs
score_cam = 0
score_hug = 0

compteur_tour_cam = 0
compteur_tour_hug = 0

running = True


#! Boucle principale
while running:

    print("Tour de Camille :")

    # On récupère le score, le nombre de 5 et le lancer qu'a fait Camille
    addscore, nb_de_5, lancer = tour()

    score_cam += addscore

    print("Lancers de Camille :", lancer)
    print("Camille est maintenant à", score_cam, "point(s), et son nombre de 5 à ce tour est", nb_de_5, "\n")
    compteur_tour_cam += 1

    if score_cam == 4:
        running = False
    else:

        print("Tour de Hugo :")
        # On récupère le score, le nombre de 5 et le lancer qu'a fait Hugo
        addscore, nb_de_5, lancer = tour()

        score_hug += addscore

        print("Lancers de Hugo :", lancer)
        print("Hugo est maintenant à", score_hug, "point(s), et son nombre de 5 à ce tour est", nb_de_5, "\n")

        compteur_tour_hug += 1

        if score_hug == 4:
            running = False
    

#? Annonce du gagnant
if score_cam == 4:
    print("Camille a gagné !")
    gagnant = "Camille"
else :
    print("Hugo a gagné")
    gagnant = "Hugo"

#! Récapitulatif mis en forme pour avoir un affichage plus clair et lisible
# Rapel: ":<37" = aligner à gauche pour un total de 37 caractères
# "<" gauche, ">" droite, "^" centre
# doc sur https://docs.python.org/fr/3/library/string.html

print("_" * 50) # Underscore
print(f"| {"Nombre de tours pour Camille :":<37} {compteur_tour_cam:>8} |")
print(f"| {"Nombre de tours pour Hugo :":<37} {compteur_tour_hug:>8} |")
print(f"| {"Gagnant :":<37} {gagnant:>8} |")
print(f"| {"Nombre total de dés lancés :":<37} {(compteur_tour_cam + compteur_tour_hug)*8:>8} |")
print("‾" * 50) # "Upperscore", un underscore dans l'autre sens


