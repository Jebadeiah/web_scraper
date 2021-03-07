class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def convert_height(self):
        return self.height / .3048
