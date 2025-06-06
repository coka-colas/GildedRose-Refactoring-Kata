# utf-8

class Updater(object):
    
    # Indication des min et max qualité
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    # En premier on crée la règle générale pour TOUS les items
    def normal_item(self, item):
        if item.sell_in > 0: 
            depreciation = -1
        else:
            depreciation = -2
        item.quality = max((item.quality + depreciation), self.MIN_QUALITY)
        item.sell_in += -1

    # Règle spéciale pour le brie
    def aged_brie(self, item):
        if item.sell_in > 0:
            appreciation = 1
        else:
            appreciation = 2
        item.quality = min((item.quality + appreciation), self.MAX_QUALITY)
        item.sell_in += -1
    
    # On passe pour l'item légendaire
    def sulfuras(self, item):
        pass
    
    # Règle spéciale pour les places en backstage
    def backstage_passes(self, item):

        def get_quality(item, appreciation):
            item.quality = min(item.quality + appreciation , self.MAX_QUALITY)

        if item.sell_in > 10:
            appreciation = 1
            get_quality(item, appreciation)
        elif item.sell_in > 5:
            appreciation = 2
            get_quality(item, appreciation)
        elif item.sell_in > 0:
            appreciation = 3
            get_quality(item, appreciation)
        else:
            item.quality = 0
        item.sell_in += -1

    # Règle spéciale pour la classe d'item maudite rajoutée dans l'exercice
    def conjured(self, item):
        if item.sell_in > 0:
            depreciation = -2
        else:
            depreciation = -4

        item.quality = max((item.quality + depreciation), self.MIN_QUALITY)
        item.sell_in += -1

# On enlève les 'if' imbriqués grâce à des 'elif' plus performants
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        updater = Updater()

        # On applique maintenant les règles spéciales, en commençant par les plus spécifiques pour finir avec la règle générale dans le 'else' pour couvrir tous les cas
        for item in self.items:
            if item.name == 'Aged Brie':
                updater.aged_brie(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                updater.backstage_passes(item)
            elif item.name == 'Sulfuras, Hand of Ragnaros':
                updater.sulfuras(item)
            elif item.name == 'Conjured Mana Cake':
                updater.conjured(item)
            else:
                updater.normal_item(item)

# Classe inchangée
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)