import math

class Player:
    #Will need to add mage/ranged stuff too but melee will work for now
    def __init__(self, str_lvl, str_bonus, boost, prayer, style_bonus, void=False, salve=False, salve_i=False, slayer=False):
        self.strength = str_lvl

def eff_str_lvl(strength, boosts, prayer, style_bonus,void=False):
    str_lvl = ((strength + boosts) * prayer) + style_bonus + 8

    if void:
        str_lvl *= 1.1

    return math.floor(str_lvl)

def max_hit(str_bonus=0, str_lvl = -1, strength=0, boosts=0, prayer=0, style_bonus=0, void=False, salve=False, slayer=False):
    if str_lvl <= -1:
        str_lvl = eff_str_lvl(strength, boosts, prayer, style_bonus, void)
    
    temp = (str_lvl * (str_bonus + 64)) + 320
    temp = math.floor(temp / 640)

    if (slayer and salve) or salve:
        temp *= (7/6)
    if salve:
        temp *= 1.2
    

