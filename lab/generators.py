from . import models
import random


def barabasi_albert(size: int, k: int = 2,
                    _route_length: tuple = tuple(range(4, 12))) -> tuple[tuple[int, int, models.Route], ...]:
    result = []
    for i in range(size):
        pool = tuple(set(range(i)) - {i})
        if pool:
            for j in random.choices(pool, k=min(len(pool), k)):
                result.append((i, j, models.Route(random.choice(_route_length))))
    return tuple(result)
