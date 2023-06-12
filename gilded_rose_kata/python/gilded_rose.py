# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


    def update_quality2(self):
        for item in self.items:
            # Skip any legendary items
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            #  Update "Aged Brie" items then skip to next
            elif item.name == "Aged Brie":
                item.quality += 1 if item.sell_in > 0 else 2
                if item.quality > 50:
                    item.quality = 50
                item.sell_in -= 1
                continue

            #  Update "Backstage pass" Items then skip to next
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality == 0:
                    item.sell_in -= 1
                    continue

                if item.sell_in > 10:
                    item.quality += 1 if item.quality < 50 else 0
                    item.sell_in -= 1
                    continue

                if 5 < item.sell_in <= 10:
                    item.quality += 2
                    if item.quality > 50:
                        item.quality = 50
                    item.sell_in -= 1
                    continue

                if 0 < item.sell_in <= 5:
                    item.quality += 3
                    if item.quality > 50:
                        item.quality = 50
                    item.sell_in -= 1
                    continue

                if item.sell_in == 0:
                    item.quality = 0
                    item.sell_in -= 1
                    continue

            #  Update "Conjured" Items then skip to next
            elif "Conjured" in item.name or "conjured" in item.name:
                if item.quality == 0:
                    item.sell_in -= 1
                    continue
                if item.sell_in > 0 and item.quality > 0:
                    item.quality -= 1
                if item.sell_in <= 0 <= item.quality:
                    item.quality -= 2
                if item.quality < 0:
                    item.quality = 0
                item.sell_in -= 1

            else:
                #  Update all other items
                if item.quality == 0:
                    item.sell_in -= 1
                    continue
                if item.sell_in > 0 and item.quality > 0:
                    item.sell_in -= 1
                    item.quality -= 1
                    continue
                if item.sell_in <= 0:
                    item.quality -= 2
                    item.sell_in -= 1
                    continue


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)