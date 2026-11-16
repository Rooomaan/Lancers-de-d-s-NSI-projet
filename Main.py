"""
à savoir :
- Les points d'exclamation (!)
- Les points d'interrogation (?)
- Les "Todo"
sont une mise en forme pour une coloration syntaxique de l'extension "Better Comments" sur VSCode pour une meilleure lecture.
"""



#! Import des modules
import random

#! Fonctions
def lancers(nombre_de_lancers=8): #todo# parametre nombre_de_lancers: Nombre de lancers de dés à simuler.
    """Simule 8 lancers de dés."""
    liste = []
    for i in range(nombre_de_lancers):
        # Utilisation de random.randint(1, 6) pour avoir un nombre aléatoire entre 1 et 6 et le mettre dans une liste.
        liste.append(random.randint(1, 6))
    return liste

#? Test de la fonction lancers()
assert len(lancers(32)) == 32, "lancers(32) doit retourner une liste de 32 nombres."

def lancer_joli():
    """Réécrit un lancer de dé mais avec une belle mise en forme."""
    lancers()

def tour():
    """Simule un tour de jeu pour un joueur."""
    score = 0
    lancer = lancers()
    #print(lancer)
    nb_de_5 = 0
    for i in lancer:
        if i == 5:
            nb_de_5 += 1
        else:
            nb_de_5 += 0
    if nb_de_5 == 0:
        score -= 1
    elif nb_de_5 == 1:
        score += 0
    elif nb_de_5 >= 2:
        score += 1
    

    return score, nb_de_5, lancer

 


#! Initiation des valeurs
score_cam = 0
score_hug = 0
running = True


#! Boucle principale
while running:
    print("Tour de Camille :")
    addscore, nb_de_5, lancer = tour()
    score_cam += addscore
    print("Lancers de Camille :", lancer)
    print("Camille a", str(score_cam) + ", et son nombre de 5 à ce tour est", nb_de_5)


    if score_cam == 4:
        running = False
    else:
        print("Tour de Hugo :")
        addscore, nb_de_5, lancer = tour()
        score_hug += addscore
        print("Lancers de Hugo :", lancer)
        print("Hugo a", str(score_hug) + ", et son nombre de 5 à ce tour est", nb_de_5)

        if score_hug == 4:
            running = False

if score_cam == 4:
    print("Camille a gagné !")
else :
    print("Hugo a gagné")
