import math

class Player:
    #Will need to add mage/ranged stuff too but melee will work for now
    def __init__(self, str_lvl, str_bonus, boost, prayer, style_bonus, void=False, salve=False, salve_i=False, slayer=False):
        self.str_lvl = str_lvl
        self.str_bonus = str_bonus
        self.boost = boost
        self.prayer = prayer
        self.style_bonus = style_bonus
        self.void = void
        self.salve = salve
        self.salve_i = salve_i
        self.slayer = slayer

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