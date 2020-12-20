# Création de la classe pokemon
class Pokemon:
    def __init__(self, id, name, image = None, types=None, height=None, weight=None):
        self.id = id
        self.name = name
        self.image = image
        self.types = types
        self.height = height
        self.weight = weight
    
    def __eq__(self, other):
        if not isinstance(other, Pokemon):
            return False
        return (
            self.id == other.id and
            self.name == other.name and
            self.types == other.types and
            self.image == other.image and
            self.height == other.height and
            self.weight == other.weight 
        )
    
    def __str__(self):
        return f'n° {self.id}, name : {self.name}, types : {self.types}, height : {self.height}, width : {self.weight}'