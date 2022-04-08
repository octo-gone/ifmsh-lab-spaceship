from . import models
import random


def barabasi_albert(size: int, k: int = 2,
                    _route_length: tuple = tuple(range(4, 12))) -> tuple[tuple[int, int, models.Route], ...]:
    result = []
    for i in range(size):
        pool = list(set(range(i)) - {i})
        if pool:
            for _ in range(min(len(pool), k)):
                random.shuffle(pool)
                j = pool.pop(0)
                result.append((i, j, models.Route(random.choice(_route_length))))
    return tuple(result)


def halo(size: int, _route_length: tuple = (12,)) -> tuple[tuple[int, int, models.Route], ...]:
    result = []
    for i in range(size):
        j = i + 1
        if j == size:
            j = 0
        result.append((i, j, models.Route(random.choice(_route_length))))
    return tuple(result)
