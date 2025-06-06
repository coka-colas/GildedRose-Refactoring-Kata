import unittest
from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):


    def updater(obj = GildedRose, times = 1):
        for i in range(times):
            obj.update_quality()


    # Test unitaire de chaque règle spéciale
    def test_normal_item(self):

        # Set up l'item
        item = Item("+5 Dexterity Vest", 10, 20)
        gilded_rose = GildedRose([item])

        # 1 jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)
        
        # Vente si date dépassée
        GildedRoseTest.updater(gilded_rose, item.sell_in + 1)
        self.assertEqual(item.sell_in, -1)

        # Qualité se dégrade 2x plus vite
        self.assertEqual(item.quality, 8)
        GildedRoseTest.updater(gilded_rose, 10)
        self.assertEqual(item.sell_in, -11)
        self.assertEqual(item.quality, 0)  # jamais moins que zéro

    def test_aged_brie(self):
        # set up l'item
        item = Item("Aged Brie", 10, 20)
        gilded_rose = GildedRose([item])
        
        # 1 jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 21)

        # Vente si date dépassée
        GildedRoseTest.updater(gilded_rose, item.sell_in + 1)
        self.assertEqual(item.sell_in, -1)

        # Qualité augmente 2x plus vite à partir de maintenant
        self.assertEqual(item.quality, 32)
        GildedRoseTest.updater(gilded_rose, 10)
        self.assertEqual(item.sell_in, -11)
        self.assertEqual(item.quality, 50) 

    def test_sulfuras(self):
        # set up l'item
        item = Item("Sulfuras, Hand of Ragnaros", 20, 80)
        gilded_rose = GildedRose([item])

        # 1 jour après
        gilded_rose.update_quality()
        self.assertNotEqual(item.sell_in, 19)
        self.assertEqual(item.sell_in, 20)
        self.assertEqual(item.quality, 80)
        
        # vente si date dépassée
        GildedRoseTest.updater(gilded_rose, item.sell_in + 1)
        self.assertEqual(item.sell_in, 20)
        self.assertNotEqual(item.sell_in, -1)

    def test_backstage_passes(self):
        # set up l'item
        item = Item("Backstage passes to a TAFKAL80ETC concert", 20, 20)
        gilded_rose = GildedRose([item])

        # 1 jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 19)
        self.assertEqual(item.quality, 21)
        GildedRoseTest.updater(gilded_rose, 9)

        # Date limite à 10 jours ou moins
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 30)
        GildedRoseTest.updater(gilded_rose)
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 32)

        # Date limite à 5 jours ou moins
        GildedRoseTest.updater(gilded_rose, 4)
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 40)
        GildedRoseTest.updater(gilded_rose)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 43)
        GildedRoseTest.updater(gilded_rose, 2)
        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 49)

        # Ne va jamais au delà de 50 en qualité et passe à zéro si date passée
        GildedRoseTest.updater(gilded_rose)
        self.assertEqual(item.sell_in, 1)
        self.assertEqual(item.quality, 50)

        GildedRoseTest.updater(gilded_rose, 2)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_conjured(self):
        # set up l'item
        item = Item("Conjured Mana Cake", 20, 50)
        gilded_rose = GildedRose([item])

        # 1 jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 19)
        self.assertEqual(item.quality, 48)
        GildedRoseTest.updater(gilded_rose, item.sell_in + 1)

        # vente si date dépassée -- va baisser 2x plus vite que les items normaux (-4)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 6)

        GildedRoseTest.updater(gilded_rose)
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 2)

        GildedRoseTest.updater(gilded_rose)
        self.assertEqual(item.sell_in, -3)
        self.assertEqual(item.quality, 0)

if __name__ == '__main__':
    unittest.main()