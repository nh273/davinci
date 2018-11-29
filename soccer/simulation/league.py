"""The leagues will keep control of time, activating actions
    in all other objects at each time step, collect data, etc."""

import os


class League():
    """This is a boiler plate League class"""

    def __init__(self):
        self.players = []
        self.managers = []
        self.time = 0

    def load_players(self, data_source):
        pass

    def step(self):
        pass


class RealDataLeague(League):
    """This league uses actual data from past gameweeks"""

    def __init__(self):
        super.__init__()

    def step(self):
        pass


class SimulatedDataLeague(League):
    """This league uses simulated data based on actual players'
    statistical performance"""

    def __init__(self):
        super.__init__()

    def step(self):
        pass
