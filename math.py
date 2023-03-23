import math

def eff_str_lvl(strength, boosts, prayer, style_bonus,void=False):
    str_lvl = ((strength + boosts) * prayer) + style_bonus + 8

    if void:
        str_lvl *= 1.1

    return math.floor(str_lvl)

def max_hit(str_bonus=0, str_lvl = -1, strength=0, boosts=0, prayer=0, style_bonus=0, void=False, salve=False, slayer=False):
    if str_lvl <= -1:
        str_lvl = eff_str_lvl(strength, boosts, prayer, style_bonus, void)
    
    temp = (str_lvl * ())

