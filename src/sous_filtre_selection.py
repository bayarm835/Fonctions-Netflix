import pandas as pd

from helpers import *


def selections(categorie, cat_dict, filtID):
    #affichage des choix et demande pour choisir
    print(f"Vous Choix de {categorie}:")
    
    cat_list = []
    for key, value in cat_dict.items():
        print(f"{key} {value} : ")
        
    cat_id = input(f'Veuillez en choisir un ou plusieur {categorie} par numéro avec une espace entre: ')
    
    if categorie == 'duree':
        return cat_id
    else:
        
        list_results = cat_id.split(" ")  
        for value in list_results:
            if value != "":
                
                if cat_dict.get(key) != None:
                    cat_list.append(cat_dict.get(key))
            else: sous_filtre_choice(filtID)
            
    return cat_list
    
    
def sous_filtering(categorie, categorie_to_filter):
    
    if categorie == 'duree':
        conditions = [csv_df[categorie] for cat in categorie_to_filter]
    else:
        conditions = [csv_df[categorie].str.contains(cat) for cat in categorie_to_filter]
    combined_condition = pd.concat(conditions, axis=1).all(axis=1)

    combined_condition &= ~csv_df[categorie].isna()

    filtered_df = csv_df[combined_condition]
        
    return filtered_df

def sous_filtre_choice(filtID):
    """fonction pour les choix pour chaque filtre """
    match (filtID):
        #filtre genres
        case 1:
            categorie = 'genres'
            categorie_en = 'genres'
            # {1:'Action', 2:"Drama",3: 'Thriller' }
            categorie_dict = genres_dict #this needs to be a global variable in main
            
        #filtre duree
        case 2: 
            categorie = 'duree'
            categorie_en = 'runtime'
            
            categorie_dict = {1:'Moin que 60 minutes', 2: '60 à 90 minutes', 3:'90 minutes à 120 minutes', 4: '120 minutes à 180 minutes', 5:'plus que 180 minutes'}

            categorie_to_filter = selections(categorie, categorie_dict, filtID)
            
            match (int(categorie_to_filter)):
                case 1: result = csv_df[(csv_df['runtime'] < 60)]
                case 2: result = csv_df[(csv_df['runtime'] > 60) & (csv_df['runtime'] <= 90) ]
                case 3: result = csv_df[(csv_df['runtime'] > 90) & (csv_df['runtime'] <= 120) ]
                case 4: result = csv_df[(csv_df['runtime'] > 120) & (csv_df['runtime'] <= 180)]
                case 5: result = csv_df[(csv_df['runtime'] > 180)]
                case _:
                    option_error("Option invalide, veullez ressayer!")
                    sous_filtre_choice(filtID)
        #filtre pays    
        case 3:
            categorie = 'pays'
            categorie_en = 'production_countries'
            #{1:'United States of America', 2: 'France', 3:'Germany'}
            categorie_dict = pays_dict # this needs to be a global variable in main
        case _: 
            option_error("Option invalide, veullez ressayer!")
            sous_filtre_selection(csv_df)
            
    if filtID != 2:
        categorie_to_filter = selections(categorie, categorie_dict, filtID)
        result = sous_filtering(categorie_en, categorie_to_filter)
        
    user_dict = {categorie: categorie_to_filter}
    return result, user_dict
    
    

def sous_filtre_selection(df):
    print('Vous choix : \n 1 Genre: \n 2 Duree: \n 3 Pays:' )
    
    filtID = input('Veuillez en choisir un par numéro ')
    
    filtID = int(filtID)
    
    result, user_dict = sous_filtre_choice(filtID)
    
    
    return result, user_dict
    
        
      
#cat1, user_data = sous_filtre_selection(csv_df)
#print(user_data)
#print(cat1.sample(5))