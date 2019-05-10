# création d'une structure de dossiers
import os
import json

def creer_dossiers(dossiers):
    for key,values in dossiers.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base,key,value)
            os.makedirs(dossier)
            print('Création du dossier {0}'.format(dossier))
def creer_json(fichier_json,dictionnaire):
    with open(fichier_json, 'w') as f:
        json.dump(dictionnaire,f,indent=4)



base = '/Users/erion/Local/python'
fichier_json = '/Users/erion/Local/python/structure.json'
structure = {
            'musique': ['alternative','classical','underground'],
            'cine': ['répertoire','recherche','courts'],
            'videos': ['chats','hamsters','concombres']
            }

creer_dossiers(structure)
creer_json(fichier_json,structure)