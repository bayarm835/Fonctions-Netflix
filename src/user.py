import matplotlib.pyplot as plt
import pandas as pd

from helpers import *

user_bdd = '../res/users_bdd.csv'  # chemin vers la base de données des utilisateurs.
# Le dictionnaire contenant les informations de l'utilisateur actuel.
current_user = { 'name': "", 'genres': [], 'duree': [], 'pays': [] }      


def print_user_stats():
    '''
        # TODO
        + Doit afficher les informations contenue dans le dictionnaire `current_user`.
        Example de `current_user`: \n
        current_user = {
            'name' = "Bassam",
            'genres' = [ 'Action', 'Comedy', ...],
            'duree' = [ '< 60 minutes', '60 à 90 minutes', '90 à 120 minutes', '120 à 180 minutes', '> 180 minutes' ],
            "pays' = [ 'France', 'Myanmar , ...]
        }
    '''
    pass

def save_user_data(data:dict):
    '''
        # TODO
        + Doit sauvegareder le dictionnaire `data` (après la recherche) dans :
        1. `current_user` (sans effacer les données de recherche précédantes)
        2. `user_bdd` (la basedétruire de données des utilisateurs)
    '''
    pass

def is_username_valid(usernamme:str) -> bool:
    '''
        # TODO
        + Le `username` est valide s'il suit l'expression réguilère r'[a-zA-Z][a-zA-Z0-9]*'
    '''

    report_msg("Nom d'utilisateur validé !")
    return True

def create_user(username:str):
    with open(user_bdd, 'a') as f:
        f.write(username + "\n")

    current_user['name'] = username

def user_exists(name:str) -> bool:
    '''
    Retourne vraie, si `name` (le nom de l'utilisateur) existe
    dans le fichier `user_bdd.csv`
    '''
    return name in pd.read_csv(user_bdd)['username'].values
