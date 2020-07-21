from .animal import Animal
from ..movements import Swimming, Walking

class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
        Swimming.__init__(self)
        Walking.__init__(self)
    
    def honk(self): 
        print("The goose honks. A lot")

    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f'{self.name} the Goose'