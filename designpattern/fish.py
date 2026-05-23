from abc import ABC, abstractmethod


# -------------------------------
# Abstract Fish Class
# -------------------------------
class Fish(ABC):

    @abstractmethod
    def category(self):
        pass


# -------------------------------
# Concrete Fish Classes
# -------------------------------
class Goldfish(Fish):

    def category(self):
        return "Goldfish"


class Shark(Fish):

    def category(self):
        return "Shark"


class Angelfish(Fish):

    def category(self):
        return "Angelfish"


class Tuna(Fish):

    def category(self):
        return "Tuna"


class Salmon(Fish):

    def category(self):
        return "Salmon"

