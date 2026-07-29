from enum import Enum, auto

class City(Enum):
    Atlanta = auto()
    Boston = auto()
    Chicago = auto()
    Denver = auto()
    El_Paso = auto()
    Fresno = auto()
    Greensboro = auto()
    Houston = auto()
    Indianapolis = auto()
    Jacksonville = auto()
    Kansas_City = auto()
    Los_Angeles = auto()
    Miami = auto()
    New_York_City = 'New York', 'NYC'
    Orlando = auto()
    Philadelphia = auto()
    Quincy = auto()
    Reno = auto()
    San_Francisco = auto()
    Tucson = auto()
    Union_City = auto()
    Virginia_Beach = auto()
    Washington = 'Washington D.C.'
    Xenia = auto()
    Yonkers = auto()
    Zion = auto()

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

for city in City:
    print(city)

print("-" * 50)
for direction in Direction:
    print(direction.name, direction.value)