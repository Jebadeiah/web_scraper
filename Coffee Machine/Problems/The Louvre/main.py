class Painting:
    museum = 'Louvre'

    def __init__(self, painter, title, year):
        self.painter = painter
        self.title = title
        self.year = year


a_title = input()
an_artist = input()
a_year = input()

painting = Painting(an_artist, a_title, a_year)

print(f'"{painting.title}" by {painting.painter} ({painting.year}) hangs in the {painting.museum}.')
