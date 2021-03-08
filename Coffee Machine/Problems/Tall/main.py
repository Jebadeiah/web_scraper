class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __iadd__(self, other):
        gza = self.height + other
        return Person(self.name, gza)

    def __isub__(self, other):
        gza = self.height - other
        return Person(self.name, gza)
