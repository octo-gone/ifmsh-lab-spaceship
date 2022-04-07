from lab import models
from lab import generators


space = models.Space(10, generators.barabasi_albert(10))

# do smth with space
