import math
import equipment

class Player:
    #Will need to add mage/ranged stuff too but melee will work for now
    def __init__(self, str_lvl, boost, prayer, style_bonus, loadout, type=1, void=False, salve=False, salve_i=False, slayer=False):
        #For type:
        #1 is melee, 2 is ranged, 3 is mage
        self.str_lvl = str_lvl
        self.boost = boost
        self.prayer = prayer
        self.style_bonus = style_bonus
        self.void = void
        self.salve = salve
        self.salve_i = salve_i
        self.slayer = slayer
        self.type = type
        self.update_equipment(loadout)

    def update_equipment(self, loadout):
        self.loadout = loadout
        self.str_bonus = self.get_equipment_str()

    def get_equipment_str(self):
        stats = self.loadout.get_bonuses()

        if self.type == 1:
            return stats["str"]
        elif self.type == 2:
            return stats["range_str"]
        elif self.type == 3:
            return stats["mage_str"]
        else:
            Exception("Invalid Type Given")



        

    def eff_str_lvl(self):
        str = ((self.str_lvl + self.boost) * self.prayer) + self.style_bonus + 8
        
        if self.void:
            str += 1.1

        return math.floor(str)

    def max_hit(self):
        temp = (self.eff_str_lvl() * (self.str_bonus + 64)) + 320
        temp = math.floor(temp/640)

        mult = 1
        if self.slayer or self.salve:
            mult = (7/6)
        if (self.salve_i):
            mult = (1.2)

        temp *= mult

        return math.floor(temp)