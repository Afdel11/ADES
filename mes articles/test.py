# Création d'un dictionnaire avec des clés uniques
mon_dictionnaire = {'a': 1, 'b': 2, 'c': 3}

# Tentative d'ajouter une clé identique
mon_dictionnaire['a'] = 4  # Cette opération met à jour la valeur associée à la clé 'a'

print(mon_dictionnaire) # Affiche {'a': 4, 'b': 2, 'c': 3}
