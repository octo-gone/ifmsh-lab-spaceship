import random


class Route:
    none = None

    def __init__(self, length: int,
                 _pool: tuple = None,
                 _weights: tuple = None):
        """
        Маршрут между точками, состоит из ячеек со значениями

        :param length: длина маршрута
        :param _pool: варианты ячеек
        :param _weights: веса вариантов для генерации
        """

        if _pool is None:
            _pool = (0, 1, 2, 3, 4)
            _weights = (4, 1, 1, 1, 1)

        if _weights is None:
            _weights = tuple([1 for _ in range(len(_pool))])

        self.__length = length
        self.__route = random.choices(_pool, weights=_weights, k=length)

    @property
    def length(self):
        """Длина пути данного маршрута"""
        return self.__length

    @length.setter
    def length(self, value):
        pass

    @property
    def route(self):
        """Маршрут в формате кортежа (массива)"""
        return self.__route

    @route.setter
    def route(self, value):
        pass

    def __len__(self):
        return self.__length

    def __getitem__(self, item: tuple):
        if isinstance(item, int):
            return self.__route[item]

    def __repr__(self):
        if not self.__length:
            return f"<Route None>"
        return f"<Route {'-'.join(map(str, self.__route))}>"

    def reverse(self):
        """Функция инвертирования маршрута"""
        copied = Route(length=self.__length)
        copied.__route = tuple(reversed(self.__route.copy()))
        return copied


Route.none = Route(0)


class Space:
    def __init__(self, size: int, generating_algorithm, *alg_args, **alg_kwargs):
        """
        Космос в виде графа

        :param size: количество вершин
        :param generating_algorithm: алгоритм генерации
        :param alg_args: позиционные аргументы алгоритма генерации
        :param alg_kwargs: ключи-аргументы алгоритма генерации
        """
        self.__size = size

        routes = generating_algorithm(size, *alg_args, **alg_kwargs)

        self.__space = [[Route.none for _ in range(size)] for _ in range(size)]
        self.__routes = routes

        for i, j, value in routes:
            self.__space[i][j] = value
            self.__space[j][i] = value.reverse()

    @property
    def size(self):
        """Количество вершин"""
        return self.__size

    @size.setter
    def size(self, value):
        pass

    @property
    def routes(self):
        """Все маршрута (без инверсий)"""
        return self.__routes

    @routes.setter
    def routes(self, value):
        pass

    def __len__(self):
        return self.__size

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__space[item]
        return self.__space[item[0]][item[1]]

    def __repr__(self):
        return f"<Space size={self.__size}>"


class Dice:
    def __init__(self, change_prob: float = 0.3,
                 _pool: tuple = None,
                 _weights: tuple = None):
        """
        Кубик

        :param change_prob: вероятность изменения стороны
        :param _pool: возможные цвета точек
        :param _weights: веса возможных цветов точек
        """

        if _pool is None:
            _pool = (0, 1, 2, 3, 4)
            _weights = (16, 1, 1, 1, 1)

        if _weights is None:
            _weights = tuple([1 for _ in range(len(_pool))])

        sides = [random.randint(1, 6) if random.random() < change_prob else i for i in range(1, 7)]
        self.__sides = []
        for i, side in enumerate(sides):
            self.__sides.append(tuple(random.choices(_pool, weights=_weights, k=side)))
        self.__sides.sort(key=len)
        self.__sides = tuple(self.__sides)

    @property
    def sides(self):
        """Все стороны"""
        return self.__sides

    @sides.setter
    def sides(self, value):
        pass

    def roll(self):
        """Бросить кубик"""
        return random.choice(self.__sides)

    def __repr__(self):
        return f"<Dice {self.__sides}>"
