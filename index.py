from petting_zoo.animals import Donkey
from petting_zoo.animals import Llama
from petting_zoo.animals import Fish
from petting_zoo.animals import Snake
from petting_zoo.animals import Goose
from petting_zoo.attractions import PettingZoo
from petting_zoo.attractions import SnakePit
from petting_zoo.attractions import Wetlands

jack = Donkey('Jack', 'Irish', 'midday', 'kibles')
tina = Llama('Tina', 'Llama', 'morning', 'bits')
bruce = Snake('Bruce', 'Copperhead','mice')
gigi = Fish('Gigi', 'Clown', 'flakes')
bob = Goose('Bob', 'Canada Goose', 'sandwiches')
bob.run()
bob.honk()

pettingZoo = PettingZoo('Broncos Fun', 'Have a great time at the barn.')
snakePit = SnakePit('Slithering Substance', 'See the creepy crawlers')
wetlands = Wetlands('Moist place','Be immersed')

print(pettingZoo)

pettingZoo.add_animal(jack)
pettingZoo.add_animal(tina)
snakePit.add_animal(bruce)
wetlands.add_animal(gigi)
pettingZoo.add_animal(bob)

for animal in pettingZoo.animals:
    print(animal.name)