import pandas as pd

from dialogs import *

src = '../res/metadata_rebuilt.csv'

global csv_df
csv_df = pd.read_csv(src)

global pays_dict
global genres_dict
pays_dict = {index + 1: country for index, country in enumerate(csv_df['production_countries'].str.split(", ", expand=True).stack().unique())}
genres_dict = {index + 1: country for index, country in enumerate(csv_df['genres'].str.split(", ", expand=True).stack().unique())}


def print_title(menu_name:str):
    print(f"---:[{menu_name}]:{'-' * 70}")

def print_options(options:dict, extras:dict = dialog_extra, format='\n'):
    for k, v in options.items():
        if k != 'desc':
            print(f" {k} : {v}", end=format)
    
    if extras != None:
        for k, v in extras.items():
            print(f"{k} : {v}", end=format)

    print()
    if ('desc' in options):
        print(options['desc'])

def affichage(df):
    to_display = ['genres', 'runtime', 'languages', 'actors']
    start_index = 1
    while start_index < len(df):
        print(df[to_display].iloc[start_index:start_index + 5])
        start_index += 5
        choix_suivant = input("Appuyez sur 'Entrée' pour afficher les 5 lignes suivantes ou entrez '.q' pour quitter : ")
        if choix_suivant.lower() == '.q':
            break

def select_option():
    option = input("(>) ")
    match (option):                 
        case '.q' : return -2
        case '..' : return -1

    try:
        return int(option)
    except ValueError as val_err:
        pass

    return option

def option_error(msg: str):
    input(f"---![Erreur]: {msg}")

def report_msg(msg: str):
    print(f"---![Rapport]: {msg}")