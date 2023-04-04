

class Equipment:

    #Types:
    #Armor, 1h, 2h
    def __init__(self, type, stab, slash, crush, mage, ranged, stab_def, slash_def, crush_def, mage_def, range_def, str, range_str, mage_str, pray, weight, ticks=0):
        self.type = type
        self.stab = stab
        self.slash = slash
        self.crush = crush
        self.mage = mage
        self.ranged = ranged
        self.stab_def = stab_def
        self.slash_def = slash_def
        self.crush_def = crush_def
        self.mage_def = mage_def
        self.range_def = range_def
        self.str = str
        self.range_str = range_str
        self.mage_str = mage_str
        self.pray = pray
        self.weight = weight
        self.ticks = ticks

class Loadout:

    def __init__(self, head, amulet, chest, legs, boots, cape, ammo, main_hand, off_hand, ring, gloves):
        self.head = head
        self.amulet = amulet
        self.chest = chest
        self.legs = legs
        self.boots = boots
        self.cape = cape
        self.ammo = ammo
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.ring = ring
        self.gloves = gloves

    def update_equipment(self, slot, new):

        if slot.lower() =="head":
            self.head = new
        elif slot.lower() =="amulet":
            self.amulet = new
        elif slot.lower() =="chest":
            self.chest = new
        elif slot.lower() =="legs":
            self.legs = new
        elif slot.lower() =="boots":
            self.boots = new
        elif slot.lower() =="cape":
            self.cape = new
        elif slot.lower() =="ammo":
            self.ammo = new
        elif slot.lower() =="main_hand":
            self.main_hand = new
        elif slot.lower() =="off_hand":
            self.off_hand = new
        elif slot.lower() =="ring":
            self.ring = new
        elif slot.lower() =="gloves":
            self.gloves = new

    def __iter__(self):
        for attr in dir(self):
            yield attr

    def get_bonuses(self):
        ret = {}

        for item in self:
            ret["stab"] += item.stab
            ret["slash"] += item.slash
            ret["crush"] += item.crush
            ret["mage"] += item.mage
            ret["ranged"] += item.ranged
            ret["stab_def"] += item.stab_def
            ret["slash_def"] += item.slash_def
            ret["crush_def"] += item.crush_def
            ret["mage_def"] += item.mage_def
            ret["range_def"] += item.range_def
            ret["str"] += item.str
            ret["range_str"] += item.range_str
            ret["mage_str"] += item.mage_str
            ret["pray"] += item.pray
            ret["weight"] += item.weight
        
        ret["ticks"] = self.ticks

        return ret


