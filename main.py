from lab import models
from lab import generators

size = 10
space = models.Space(size, generators.halo(size))

dice_1 = models.Dice()
dice_2 = models.Dice()

print(dice_1.roll(), dice_2.roll())

# do smth
