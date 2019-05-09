# création d'une structure de dossiers
import os


def creer_dossiers(dossiers):
    for key,values in dossiers.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base,key,value)
            os.makedirs(dossier)
            print('Création du dossier {0}'.format(dossier))


base = '/Users/erion/Local/python'
structure = {
            'musique': ['alternative','classical','underground'],
            'cine': ['répertoire','recherche','courts'],
            'videos': ['chats','hamsters','concombres']
            }

creer_dossiers(structure)