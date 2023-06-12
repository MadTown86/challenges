# -*- coding: utf-8 -*-
import unittest
from time import perf_counter

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            Item(name="Stilleto Of Burlosconi: The Dark Scandal", sell_in=50, quality=50),
            Item(name="Conjured Christmas Pie", sell_in=10, quality=5),
            Item(name="Mana Stone Cupcakes", sell_in=4, quality=14),
            Item(name="Aged Brie of Winterfell", sell_in=5, quality=0),
            Item(name="Crapcuirass: The Stink Sword", sell_in=50, quality=42),
            Item(name="Squeemitar: The Vomit King", sell_in=1, quality=31)
        ]
    def test_sulfurus_unchanging(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        ]
        gilded_rose = GildedRose(items)
        days = 5

        while days:
            gilded_rose.update_quality()
            days -= 1
        self.assertEqual((80, 0), (items[0].quality, items[0].sell_in))

    def test_backStage(self):
        items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        ]
        gilded_rose = GildedRose(items)
        days = 6

        while days:
            gilded_rose.update_quality()
            days -= 1

        self.assertEqual((9, 27), (items[0].sell_in, items[0].quality))
        self.assertEqual((4, 50), (items[1].sell_in, items[1].quality))
        self.assertEqual((-1, 0), (items[2].sell_in, items[2].quality))

    def test_Brie(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Aged Brie", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=10, quality=46),
        ]

        gilded_rose = GildedRose(items)
        days = 5

        while days:
            gilded_rose.update_quality()
            days -= 1

        self.assertEqual((-3, 8), (items[0].sell_in, items[0].quality))
        self.assertEqual((5, 25), (items[1].sell_in, items[1].quality))
        self.assertEqual((5, 50), (items[2].sell_in, items[2].quality))

    def test_prime1(self):
        gilded_rose = GildedRose(self.items)
        days = 30

        while days:
            gilded_rose.update_quality()
            days -= 1

    def test_prime2(self):
        gilded_rose = GildedRose(self.items)
        days = 30

        while days:
            gilded_rose.update_quality2()
            days -= 1

    def test_time(self):
        start1 = perf_counter()
        times = 50000
        while times:
            self.test_prime1()
            times -= 1
        end1 = perf_counter()

        print(f'LEGACY: {end1-start1}')

        start2 = perf_counter()
        times = 50000
        while times:
            self.test_prime2()
            times -= 1
        end2 = perf_counter()

        print(f'SELF: {end2-start2}')






if __name__ == '__main__':
    unittest.main()
