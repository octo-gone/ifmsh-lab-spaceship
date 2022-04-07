from lab import models
from lab import generators

size = 10
space = models.Space(size, generators.barabasi_albert(size))
dice_1 = models.Dice()
dice_2 = models.Dice()

# do smth

print(dice_1.roll(), dice_2.roll())
