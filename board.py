from card import Property_Card_1, Property_Card_2, Property_Card_3, Property_Card_4, Property_Card_5, Property_Card_6, Property_Card_7, Property_Card_8, Property_Card_9, Property_Card_10, Property_Card_11, Property_Card_12, Property_Card_13, Property_Card_14, Property_Card_15, Property_Card_16, Property_Card_17, Property_Card_18, Property_Card_19, Property_Card_20, Property_Card_21, Property_Card_22, Railroad_Card_1, Railroad_Card_2, Railroad_Card_3, Railroad_Card_4, Utility_Card_1, Utility_Card_2


class Space:
    pass


class Property:
    pass


class Community:
    def __init__(self):
        self.name = 'COMMUNITY CHEST'
    pass


class Go:
    def __init__(self):
        self.name = 'GO -- Collect $200 salary as you pass'
    pass


class Tax:
    pass


class Chance:
    def __init__(self):
        self.name = 'CHANCE?'
    pass


class Jail:
    pass


class Utility:
    pass


class Parking:
    def __init__(self):
        self.name = 'Free Parking'
    pass


class Railroad:
    pass


class Property_Space(Space, Property):
    pass


class Community_Space(Space, Community):
    pass


class Go_Space(Space, Go):
    pass


class Tax_Space(Space, Tax):
    pass


class Chance_Space(Space, Chance):
    pass


class Jail_Space_Go_To(Space, Jail):
    pass


class Jail_Space_Just_Visting(Space, Jail):
    pass


class Utility_Space(Space, Utility):
    pass


class Parking_Space(Space, Parking):
    pass


class Railroad_Space(Space, Railroad):
    pass


space1 = Go_Space()
space1.no = 0

space2 = Property_Space()
space2.name = 'Mediteranean Avenue: $60'
space2.price = 60
space2.no = 1
space2.status = 0
space2.owner = ''
space2.card = Property_Card_1
space2.color = 'brown'
space2.houses = 0
space2.hotels = 0

space3 = Community_Space()
space3.no = 2
space3.name = 'COMMUNITY CHEST'

space4 = Property_Space()
space4.name = 'Baltic Avenue: $60'
space4.price = 60
space4.no = 3
space4.status = 0
space4.owner = ''
space4.card = Property_Card_2
space4.color = 'brown'
space4.houses = 0
space4.hotels = 0

space5 = Tax_Space()
space5.name = 'Income Tax: $200'
space5.price = 200
space5.no = 4

space6 = Railroad_Space()
space6.name = 'Reading Railroad: $200'
space6.price = 200
space6.no = 5
space6.status = 0
space6.owner = ''
space6.card = Railroad_Card_1

space7 = Property_Space()
space7.name = 'Oriental Avenue: $100'
space7.price = 100
space7.no = 6
space7.status = 0
space7.owner = ''
space7.card = Property_Card_3
space7.color = 'light blue'
space7.houses = 0
space7.hotels = 0

space8 = Chance_Space()
space8.no = 7
space8.name = 'CHANCE?'

space9 = Property_Space()
space9.name = 'Vermont Avenue: $100'
space9.price = 100
space9.no = 8
space9.status = 0
space9.owner = ''
space9.card = Property_Card_4
space9.color = 'light blue'
space9.houses = 0
space9.hotels = 0


space10 = Property_Space()
space10.name = 'Connecticut Avenue: $120'
space10.price = 120
space10.no = 9
space10.status = 0
space10.owner = ''
space10.card = Property_Card_5
space10.color = 'light blue'
space10.houses = 0
space10.hotels = 0

space11 = Jail_Space_Just_Visting()
space11.name = 'IN JAIL: just visiting - stay for one turn'
space11.no = 10

space12 = Property_Space()
space12.name = 'St. Charles Place: $140'
space12.price = 140
space12.no = 11
space12.status = 0
space12.owner = ''
space12.card = Property_Card_6
space12.color = 'pink'
space12.houses = 0
space12.hotels = 0

space13 = Utility_Space()
space13.name = 'Electric Company: $150'
space13.price = 150
space13.no = 12
space13.status = 0
space13.owner = ''
space13.card = Utility_Card_2


space14 = Property_Space()
space14.name = 'States Avenue: $140'
space14.price = 140
space14.no = 13
space14.status = 0
space14.owner = ''
space14.card = Property_Card_7
space14.color = 'pink'
space14.houses = 0
space14.hotels = 0


space15 = Property_Space()
space15.name = 'Virginia Avenue: $160'
space15.price = 160
space15.no = 14
space15.status = 0
space15.owner = ''
space15.card = Property_Card_8
space15.color = 'pink'
space15.houses = 0
space15.hotels = 0

space16 = Railroad_Space()
space16.name = 'Pennsylvania Railroad: $200'
space16.price = 200
space16.no = 15
space16.status = 0
space16.owner = ''
space16.card = Railroad_Card_2

space17 = Property_Space()
space17.name = 'St. James Place: $180'
space17.price = 180
space17.no = 16
space17.status = 0
space17.owner = ''
space17.card = Property_Card_9
space17.color = 'orange'
space17.houses = 0
space17.hotels = 0

space18 = Community_Space()
space18.no = 17
space18.name = 'COMMUNITY CHEST'

space19 = Property_Space()
space19.name = 'Tennessee Avenue: $180'
space19.price = 180
space19.no = 18
space19.status = 0
space19.owner = ''
space19.card = Property_Card_10
space19.color = 'orange'
space19.houses = 0
space19.hotels = 0

space20 = Property_Space()
space20.name = 'New York Avenue: $200'
space20.price = 200
space20.no = 19
space20.status = 0
space20.owner = ''
space20.card = Property_Card_11
space20.color = 'orange'
space20.houses = 0
space20.hotels = 0

space21 = Parking_Space()
space21.name = 'FREE PARKING'
space21.no = 20

space22 = Property_Space()
space22.name = 'Kentucky Avenue: $220'
space22.price = 220
space22.no = 21
space22.status = 0
space22.status = 0
space22.owner = ''
space22.card = Property_Card_12
space22.color = 'red'
space22.houses = 0
space22.hotels = 0

space23 = Chance_Space()
space23.no = 22
space23.name = 'CHANCE?'

space24 = Property_Space()
space24.name = 'Indiana Avenue: $220'
space24.price = 220
space24.no = 23
space24.status = 0
space24.owner = ''
space24.card = Property_Card_13
space24.color = 'red'
space24.houses = 0
space24.hotels = 0

space25 = Property_Space()
space25.name = 'Illinois Avenue: $240'
space25.price = 240
space25.no = 24
space25.status = 0
space25.owner = ''
space25.card = Property_Card_14
space25.color = 'red'
space25.houses = 0
space25.hotels = 0

space26 = Railroad_Space()
space26.name = 'B. & O. Railroad: $200'
space26.price = 200
space26.no = 25
space26.status = 0
space26.owner = ''
space26.card = Railroad_Card_3

space27 = Property_Space()
space27.name = 'Atlantic Avenue: $260'
space27.price = 260
space27.no = 26
space27.status = 0
space27.owner = ''
space27.card = Property_Card_15
space27.color = 'yellow'
space27.houses = 0
space27.hotels = 0

space28 = Property_Space()
space28.name = 'Ventnor Avenue: $260'
space28.price = 260
space28.no = 27
space28.status = 0
space28.owner = ''
space28.card = Property_Card_16
space28.color = 'yellow'
space28.houses = 0
space28.hotels = 0

space29 = Utility_Space()
space29.name = 'Water Works: $150'
space29.price = 150
space29.no = 28
space29.status = 0
space29.owner = ''
space29.card = Utility_Card_1

space30 = Property_Space()
space30.name = 'Marvin Gardens: $280'
space30.price = 280
space30.no = 29
space30.status = 0
space30.owner = ''
space30.card = Property_Card_17
space30.color = 'yellow'
space30.houses = 0
space30.hotels = 0

space31 = Jail_Space_Go_To()
space31.name = 'GO TO JAIL'
space31.no = 30

space32 = Property_Space()
space32.name = 'Pacific Avenue: $300'
space32.price = 300
space32.no = 31
space32.status = 0
space32.owner = ''
space32.card = Property_Card_18
space32.color = 'green'
space32.houses = 0
space32.hotels = 0

space33 = Property_Space()
space33.name = 'North Carolina Avenue: $300'
space33.price = 300
space33.no = 32
space33.status = 0
space33.owner = ''
space33.card = Property_Card_19
space33.color = 'green'
space33.houses = 0
space33.hotels = 0

space34 = Community_Space()
space34.no = 33
space34.name = 'COMMUNITY CHEST'

space35 = Property_Space()
space35.name = 'Pennsylvania Avenue: $320'
space35.price = 320
space35.no = 34
space35.status = 0
space35.owner = ''
space35.card = Property_Card_20
space35.color = 'green'
space35.houses = 0
space35.hotels = 0

space36 = Railroad_Space()
space36.name = 'Short Line: $200'
space36.price = 200
space36.no = 35
space36.status = 0
space36.owner = ''
space36.card = Railroad_Card_4

space37 = Chance_Space()
space37.no = 36
space37.name = 'CHANCE?'

space38 = Property_Space()
space38.name = 'Park Place: $350'
space38.price = 350
space38.no = 37
space38.status = 0
space38.owner = ''
space38.card = Property_Card_21
space38.color = 'blue'
space38.houses = 0
space38.hotels = 0

space39 = Tax_Space()
space39.name = 'Luxury Tax: $100'
space39.price = 100
space39.no = 38

space40 = Property_Space()
space40.name = 'Boardwalk: $400'
space40.price = 400
space40.no = 39
space40.status = 0
space40.owner = ''
space40.card = Property_Card_22
space40.color = 'blue'
space40.houses = 0
space40.hotels = 0

board = [space1, space2, space3, space4, space5, space6, space7, space8, space9, space10, space11, space12, space13, space14, space15, space16, space17, space18, space19, space20,
         space21, space22, space23, space24, space25, space26, space27, space28, space29, space30, space31, space32, space33, space34, space35, space36, space37, space38, space39, space40]
