from .animal import Animal
from ..movements import Slithering

class Snake(Animal, Slithering):

    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
        Slithering.__init__(self)