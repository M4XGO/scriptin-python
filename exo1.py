import os

def lister_contenu_repertoire(repertoire=None):
    if repertoire is None:
        # Lister le contenu du répertoire courant
        contenu = os.listdir('.')
    else:
        # Liste les fichiers et répertoire d’un répertoire dont le nom est passé en paramètre
        contenu = os.listdir(repertoire)
    
    fichiers = [f for f in contenu if os.path.isfile(os.path.join(repertoire or '.', f))]
    # Lister uniquement les fichiers du répertoire courant
    if repertoire is None:
        return fichiers
    else:
        return contenu

path_to_rep=input("Le chemin vers le répertoire: ", )

# print(path_to_rep)
# Exemple d'utilisation
print("Fichiers dans le répertoire courant:", lister_contenu_repertoire())
print("Contenu d'un répertoire spécifique:", lister_contenu_repertoire(path_to_rep))
