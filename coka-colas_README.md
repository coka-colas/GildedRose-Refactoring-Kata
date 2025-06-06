# Modification du Gilded Rose original

J'ai suivi la règle interdisant de modifier la classe "Item".
La classe "GildedRose" a été modifiée.
La classe "Updater" a été ajoutée.

Pour arriver à enlever tous les "if" imbriqués, il a fallu ajouter à la classe "GildedRose" un check "item.name" dans une clause "if", avec des options "elif" et un "else" plus général pour les items normaux.
Ce sera plus facile à maintenir car tout est plus explicite.

# Maintenance

Pour chaque item, une fonction est instanciée. Si des nouveaux types d'items (tels que la classe maudite) doivent être implémentés, il suffit de les ajouter après le dernier "elif" et créer la fonction qui gérera le "sell_in" et la "quality" associée à cet item.

# Tests

Le fichier "texttest_fixture.py" a été conservé à l'identique et peut être lancé pour vérifier les résultats. Le fichier "unit_tests.py" contient des tests pas-à-pas pour assurer toutes les possibilités de mise à jour pour les différents types d'items.