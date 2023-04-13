from osrsbox import items_api

class OSBox:

    def __init__(self):
        self.items = items_api.load()

    def get_id(self, name):
        #Redo this to return the closest name's ID in the future

        for item in items:
            if name == item.name:
                return item
            
        return -1