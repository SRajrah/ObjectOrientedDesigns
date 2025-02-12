from enum import Enum

class CrustType(Enum):
    THIN = 5.0
    THICK = 7.0
    GLUTEN_FREE = 8.0

class Size(Enum):
    SMALL = 0.8
    MEDIUM = 1.5
    LARGE = 2.0

class ToppingType(Enum):
    VEG = "Veg"
    NON_VEG = "Non-Veg"
    VEGAN = "Vegan"