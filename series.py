from movies import Movie


class Series(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_nr = []
        self.season_nr = 0

    def __str__(self):
        return f'{self.title} S{self.season_nr}E{self.episode_nr}'

    def show_episodes(self):
        return len(self.episode_nr)
