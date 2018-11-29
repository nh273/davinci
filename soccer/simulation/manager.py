"""These select the players based on different criteria"""


class Manager():
    """Boiler plate manager with basic functionalities"""

    def __init__(self, league):
        self.league = league
        self.players = {'on_field': [], 'on_bench': []}
        self.point_history = {}
        self.gw_point = 0
        self.budget = 100
        self.transfers = 2
        self.specials = {'Bench Boost': 1, 'Free Hit': 1, 'Triple Captain': 1}

    def transfer(self, player_sold, player_bought):
        pass

    def team_tally(self, player_sold, player_bought):
        """Tally up how many players are in the same team"""
        pass

    def sub(self, player_in, player_out):
        pass

    def calculate_gameweek_point(self):
        pass

    def step(self):
        """Will be called at each gameweek"""
        pass


class RandomManager(Manager):
    def __init__(self, league):
        super().__init__(self, league)

    def random_strategy(self):
        pass

    def step(self):
        pass
