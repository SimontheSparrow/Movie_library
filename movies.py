class Movie:
    def __init__(self, title, released, genre):
        self.title = title
        self.released = released
        self.genre = genre
        self.views = 0

    def __str__(self):
        return f'{self.title} {self.released}'

    def play(self):
        self.views += 1

