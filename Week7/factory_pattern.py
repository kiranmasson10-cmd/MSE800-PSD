from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_product(self):
        pass


class Animals(ABC):

    @abstractmethod
    def run(self):
        pass


class Dog(Animals):

    def run(self):
        print("I'm a Dog, I can run!!")


class Cat(Animals):

    def run(self):
        print("I'm a Cat, I can run!!")


class DogFactory(Factory):

    def create_product(self):
        return Dog()


class CatFactory(Factory):

    def create_product(self):
        return Cat()


# Client Code
factory = DogFactory()
dog = factory.create_product()
dog.run()

factory = CatFactory()
cat = factory.create_product()
cat.run()