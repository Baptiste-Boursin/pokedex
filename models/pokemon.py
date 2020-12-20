# Création de la classe pokemon
class Pokemon:
    def __init__(self, id, name, image = None, types=None, height=None, weight=None):
        self.id = id
        self.name = name
        self.image = image
        self.type=types
        self.height=height
        self.weight=weight