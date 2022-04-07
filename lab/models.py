import random


class Route:
    def __init__(self, length: int,
                 _pool: tuple[int, ...] = None,
                 _weights: tuple[int, ...] = None):
        if _pool is None:
            _pool = (0, 1, 2, 3, 4)
            _weights = (4, 1, 1, 1, 1)

        if _weights is None:
            _weights = tuple([1 for _ in range(len(_pool))])

        self.__length = length
        self.__route = random.choices(_pool, weights=_weights, k=length)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        pass

    def __len__(self):
        return self.__length

    def __getitem__(self, item: tuple[int, int]):
        if isinstance(item, int):
            return self.__route[item]

    def __repr__(self):
        if not self.__length:
            return f"<Route None>"
        return f"<Route {'-'.join(map(str, self.__route))}>"

    def reverse(self):
        copied = Route(length=self.__length)
        copied.__route = reversed(self.__route.copy())
        return copied


Route.none = Route(0)


class Space:
    def __init__(self, size: int, routes: tuple[tuple[int, int, Route], ...]):
        self.__size = size
        self.__space = [[Route.none for _ in range(size)] for _ in range(size)]

        for i, j, value in routes:
            self.__space[i][j] = value
            self.__space[j][i] = value.reverse()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        pass

    def __len__(self):
        return self.__size

    def __getitem__(self, item: tuple[int, int]):
        return self.__space[item[0]][item[1]]

    def __repr__(self):
        s = '\t\n'.join(map(repr, self.__space))
        return f"<Space size={self.__size}\n{s}>"
