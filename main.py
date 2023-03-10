"""
Programme fait par Alexander Precup
Groupe: 402
Description: Objets orientées
Exercise 4 - Écrire une classe Hero
"""
import random


def rouler_de(nombre_des, nombre_cotes):
    """
    Rouler un nombre de dés avec un nombre de côtes et ajouter les valeurs obtenues
    Exemple 2d10 : rouler 2 dés avec 10 côtes et ajouter les valeurs obtenues
    """
    somme_des = 0

    # rouler les dés et ajouter les valeurs obtenues
    for i in range(nombre_des):
        somme_des = somme_des + random.randint(1, nombre_cotes)

    return somme_des


class Hero:
    """
     Classe Hero
        attributs pointsVie, force_attaque, force_defense, nom
        méthodes attaquer, recois_dommages, est_vivant
    """
    def __init__(self, nom):
        self.pointsVie = rouler_de(2, 10)       # "2d10"
        self.force_attaque = rouler_de(1, 6)    # "1d6"
        self.force_defense = rouler_de(1, 6)    # "1d6"
        self.nom = nom

    def attaque(self):
        self.pointsVie = rouler_de(1, 6) + self.force_attaque
        return self.pointsVie

    def recois_dommages(self, dommage):
        self.pointsVie = self.force_defense - dommage
        return self.pointsVie

    def est_vivant(self):
        if self.pointsVie > 0:
            return True
        else:
            return False


hero = Hero("IronMan")
print("*****************************************")
print(f"Attributs héro: {hero.nom}")
print("*****************************************")
print(f"Points de vie    : {hero.pointsVie}")
print(f"Force d'attaque  : {hero.force_attaque}")
print(f"Force défense    : {hero.force_defense}")
print("*****************************************")
hero_attaque = hero.attaque()                        # héro attaque
points_dommage = int(input("Entrez le nombre de points de dommage : "))
hero_dommage = hero.recois_dommages(points_dommage)  # héro recois points_dommage points de dommage
print(f"Après l'attaque, héro {hero.nom} a {hero_attaque} points de vie")
print(f"Après {points_dommage} points de dommages, héro {hero.nom} a {hero_dommage} points de vie")
if hero.est_vivant():
    print(f"Points de vie héro {hero.nom} : {hero.pointsVie}")
else:
    print(f"Héro  {hero.nom} est mort")
