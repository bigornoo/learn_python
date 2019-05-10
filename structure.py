# création d'une structure de dossiers
import os
import json

def print_hierarchie(fichier_json):
    with open(fichier_json,'r') as f:
        structure = json.load(f)
        print('La hiérarchie existe déjà')
        print('Celle-ci est la suivante :')
        for keys,values in structure.items():
            print('. {0}'.format(key))
            for value in values:
                print('--- {0}'.format(value))

                print('='*25)

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


if os.path.isfile(fichier_json):
    print_hierarchie(fichier_json)
else:
    creer_dossiers(structure)
    creer_json(fichier_json, structure)