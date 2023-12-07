import os
import pandas as pd
import matplotlib.pyplot as plt

from dialogs import *
from helpers import *
from user import *
from sous_filtre_selection import sous_filtre_selection

is_running = True


def stats_global():
    # Nombre de films
    nombre_total_de_film = len(csv_df)

    # Durée totale des films
    duree_totale = csv_df['runtime'].sum()

    # Nombre total des acteurs et ratio acteur / pays
    total_acteur = csv_df['actors'].apply(lambda x: len(x.split(", ")) if isinstance(x, str) else 0).sum()
    ratio_acteur_films = total_acteur / nombre_total_de_film

    print(f"Le nombre de films existants est de : {nombre_total_de_film}")
    print(f"La durée totale des films existants est de : {duree_totale} minutes")
    print(f"Dans tous ces films, il y a eu {total_acteur} acteurs au total")
    print(f"Le ratio acteur par films en moyenne est de : {ratio_acteur_films}")

    # Création d'un DataFrame pour compter le nombre de films par pays
    films_par_pays = csv_df['production_countries'].str.split(", ", expand=True).stack().value_counts().to_dict()

    # Filtrer les pays représentant moins d'un pourcent des films
    seuil = nombre_total_de_film * 0.01
    pays_autres = {pays: count for pays, count in films_par_pays.items() if count < seuil}
    pays_retenus = {pays: count for pays, count in films_par_pays.items() if count >= seuil}
    pays_retenus['Autres'] = sum(pays_autres.values())

    # Création d'un graphique à secteurs avec Matplotlib
    plt.figure(figsize=(8, 8))
    plt.pie(pays_retenus.values(), labels=pays_retenus.keys(), autopct='%1.1f%%')
    plt.title('Films par pays')
    plt.show()


def main():
    print()
    global is_running

    while (is_running):
        menu_welcome()


def menu_welcome():
    global is_running
    if (not is_running): return

    # Affiche le dialog du menu welcome
    print_title("Bienvenue")
    print_options(dialog_welcome, dialog_quit)
    option = select_option()

    match (option):
        case  2: menu_new_user()
        case  1: menu_user_connect()
        case -2: is_running = False; return
        case  _: option_error("Option invalide, veullez ressayer!")
        
    menu_welcome()


def menu_new_user():
    global is_running
    if (not is_running): return

    # Affiche le dialog de la création de compte
    print_title("Créer un compte")
    print_options(dialog_new_user)
    username = select_option()

    if (type(username) == int):
        match username:
            case -1: return
            case -2: is_running = False; return
            case  _: option_error("Option invalide, veullez ressayer!")
            
    elif is_username_valid(username) and (not user_exists(username)):
        create_user(username)
        report_msg("Création d'utilisateur réussi.")
        return
    
    else:
        option_error("Nom d'utilisateur déja pris.")

    menu_new_user()


def menu_user_connect():
    global is_running
    if (not is_running): return

    # Affiche le dialog de la connexion
    print_title("Connexion")
    print_options(dialog_connect)
    username = select_option()

    if (type(username) == int):
        match username:
            case -1: return
            case -2: is_running = False; return
            case  _: option_error("Option invalide, veullez ressayer!")

    elif user_exists(username):
        current_user['name'] = username
        report_msg("Authentification réussie!")
        menu_principal()
        
    else:
        option_error("Nom d'utilisateur introuvable. Veuillez réessayer.")

    menu_user_connect()


def menu_principal():
    global is_running
    if (not is_running): return

    # Affiche le dialog du menu principal
    print_title(f"Menu Principal][-u='{current_user['name']}'")
    print_options(dialog_principal)
    username = select_option()

    match (username):
        case  1: print_user_stats()
        case  2: stats_global()
        case  3: 
            filtered, user_data = sous_filtre_selection(csv_df)
            affichage(filtered)
            save_user_data(user_data)
        case -1: return
        case -2: is_running = False; return
        case  _: 
            option_error("Option invalide, veullez ressayer!")

    menu_principal()

main()