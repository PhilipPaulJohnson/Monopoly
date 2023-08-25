import random
import math


class Player:
    '''
    this parent class is for all players
    '''

    def __init__(self, name):

        self.name = name
        self.balance = 1500
        self.init_roll = 0
        self.space_no = 0
        self.getoutofjail_status = 0
        self.areyouinjail = 0
        self.doubles_tries = 0
        #self.howtogetout = 0

        # this is for the community & chance handler (possibly should be deleted)?
        self.houses = 0
        self.hotels = 0

        self.player_chance_card_ct = 0
        self.player_comm_card_ct = 0

        self.utility_ct = 0
        self.rr_ct = 0
        self.property_list = {}
        self.max_list = {'brown': 2, 'light blue': 3, 'pink': 3,
                         'orange': 3, 'red': 3, 'yellow': 3, 'green': 3, 'blue': 2}

        """
        AI attributes
        """

        chance = 0.45
        self.prop_propensity = math.floor(random.uniform(0, 1/(1-chance)))
        self.ai = 0
        self.getoutofjailchoice = random.randint(1, 3)
        self.aggression = 0
        self.risk = 0
        self.hoard = 0

    def init_dice_roll(self):
        self.init_roll = random.randint(1, 12)
        return

    def dice_roll(self):
        return random.randint(1, 12)

    def dice_roll_doubles(self):
        return random.randint(1, 6)