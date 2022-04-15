from lab import models
from lab import generators
import solution
import random

random.seed(1)

size = random.randint(5, 12)
space = models.Space(size, generators.barabasi_albert)

dice_1 = models.Dice()
dice_2 = models.Dice()

points_pool = list(range(size))
random.shuffle(points_pool)
start = points_pool.pop()
end = points_pool.pop()

result = solution.main(space, start, end, dice_1, dice_2)

print(result)
