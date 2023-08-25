# 'properties' changed to 'houses' in card description for clarity despite actual game wording

class Chance:
    def __init__(self):
        self.name = 'Chance? Card'
    pass


class Community:
    def __init__(self):
        self.name = 'Community Chest Card'
    pass


class Property:
    pass


class Railroad:
    def __init__(self):
        self.description = 'Rent $25. If 2 Railroads are owned: $50. If 3 Railroads are owned: $100. If 4 Railroads are owned: $200.'
        self.mortgage_val = 100
        self.unmortgage_val = 110
    pass


class Utility:
    pass


Chance_Card_1 = Chance()
Chance_Card_1.description = 'Bank pays you dividend of $50.'
Chance_Card_1.price = 50
Chance_Card_1.movement = 0

Chance_Card_2 = Chance()
Chance_Card_2.description = 'Advance to the next railroad. If unowned, you may buy it from the Bank. If owned, pay the owner twice the rent to which they are otherwise entitled. If you pass GO, collect $200.'
Chance_Card_2.price = 0
Chance_Card_2.movement = 1

Chance_Card_3 = Chance()
Chance_Card_3.description = 'Advance to the next railroad. If unowned, you may buy it from the Bank. If owned, pay the owner twice the rent to which they are otherwise entitled. If you pass GO, collect $200.'
Chance_Card_3.price = 0
Chance_Card_3.movement = 1

Chance_Card_4 = Chance()
Chance_Card_4.description = 'Speeding fine. Pay $15.'
Chance_Card_4.price = -15
Chance_Card_4.movement = 0

Chance_Card_5 = Chance()
Chance_Card_5.description = 'Go back three spaces.'
Chance_Card_5.price = 0
Chance_Card_5.movement = 2

Chance_Card_6 = Chance()
Chance_Card_6.description = 'You have been elected Chairperson of the Board. Pay each player $50.'
Chance_Card_6.price = 0
Chance_Card_6.movement = 3

Chance_Card_7 = Chance()
Chance_Card_7.description = 'Advance to ST. Charles Place. If you pass GO, collect $200.'
Chance_Card_7.price = 200
Chance_Card_7.movement = 4

Chance_Card_8 = Chance()
Chance_Card_8.description = 'GET OUT OF JAIL FREE. This card may be kept until needed, traded, or sold.'
Chance_Card_8.price = 0
Chance_Card_8.movement = 5

Chance_Card_9 = Chance()
Chance_Card_9.description = 'Make general repairs on all your property: For each house, pay $25. For each hotel, pay $100.'
Chance_Card_9.price = 0
Chance_Card_9.movement = 6

Chance_Card_10 = Chance()
Chance_Card_10.description = 'Advance to GO. Collect $200.'
Chance_Card_10.price = 200
Chance_Card_10.movement = 7

Chance_Card_11 = Chance()
Chance_Card_11.description = 'GO TO JAIL. GO DIRECTLY TO JAIL. Do not pass go. Do not collect $200.'
Chance_Card_11.price = 0
Chance_Card_11.movement = 8

Chance_Card_12 = Chance()
Chance_Card_12.description = 'Advance to the nearest utility. If unowned, you may buy it from the bank. If owned, roll the dice and the owner 10 times your roll. If you pass GO, collect $200.'
Chance_Card_12.price = 0
Chance_Card_12.movement = 9

Chance_Card_13 = Chance()
Chance_Card_13.description = 'Advance to Illinois Avenue. If you pass GO, collect $200.'
Chance_Card_13.price = 0
Chance_Card_13.movement = 10

Chance_Card_14 = Chance()
Chance_Card_14.description = 'Your building loan matures. Collect $150.'
Chance_Card_14.price = 150
Chance_Card_14.movement = 0

Chance_Card_15 = Chance()
Chance_Card_15.description = 'Make a trip to Reading Railroad. If you pass GO, collect $200.'
Chance_Card_15.price = 0
Chance_Card_15.movement = 11

Chance_Card_16 = Chance()
Chance_Card_16.description = 'Advance to Boardwalk.'
Chance_Card_16.price = 0
Chance_Card_16.movement = 12

chance_card_list = [Chance_Card_1, Chance_Card_2, Chance_Card_3, Chance_Card_4, Chance_Card_5, Chance_Card_6, Chance_Card_7, Chance_Card_8,
                    Chance_Card_9, Chance_Card_10, Chance_Card_11, Chance_Card_12, Chance_Card_13, Chance_Card_14, Chance_Card_15, Chance_Card_16]


Community_Card_1 = Community()
Community_Card_1.description = 'You help your neighbors clean up their yards after a big storm. Collect $200.'
Community_Card_1.price = 200
Community_Card_1.acty = 1

Community_Card_2 = Community()
Community_Card_2.description = "Just when you think you can't go another step, you finish that foot race -- and raise money for your local hospital! Advance to GO. Collect $200."
Community_Card_2.price = 2
Community_Card_2.acty = 2

Community_Card_3 = Community()
Community_Card_3.description = 'You should have volunteered for that home improvement project -- you would have learned valuable skills! FOR EACH HOUSE YOU OWN, PAY $40. FOR EACH HOTEL YOU OWN, PAY $115.'
Community_Card_3.price = 0
Community_Card_3.acty = 3

Community_Card_4 = Community()
Community_Card_4.description = 'You volunteer at a blood drive. There are free cookies! Collect $10.'
Community_Card_4.price = 10
Community_Card_4.acty = 1

Community_Card_5 = Community()
Community_Card_5.description = "You organize a group to clean up your town's walking path. Collect $50."
Community_Card_5.price = 50
Community_Card_5.acty = 1

Community_Card_6 = Community()
Community_Card_6.description = "You spend the day playing games with kids at a local children's hospital. Collect $100."
Community_Card_6.price = 100
Community_Card_6.acty = 1

Community_Card_7 = Community()
Community_Card_7.description = 'You organize a block party so people on your street can get to know each other. Collect $10 from each player.'
Community_Card_7.price = 0
Community_Card_7.acty = 4

Community_Card_8 = Community()
Community_Card_8.description = 'You organize a bake sale for your local school. Collect $25.'
Community_Card_8.price = 25
Community_Card_8.acty = 1

Community_Card_9 = Community()
Community_Card_9.description = 'Blasting music late at night? Your neighbors do not approve. GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT PASS GO. DO NOT COLLECT $200.'
Community_Card_9.price = 0
Community_Card_9.acty = 5

Community_Card_10 = Community()
Community_Card_10.description = "You go to the local school's car wash fundraiser but you forget to close your windows! Pay $100."
Community_Card_10.price = -100
Community_Card_10.acty = 1

Community_Card_11 = Community()
Community_Card_11.description = 'You help your neighbor bring in her groceries. She makes you lunch to say thanks! Collect $20.'
Community_Card_11.price = 20
Community_Card_11.acty = 1

Community_Card_12 = Community()
Community_Card_12.description = 'You buy a few bags of cookies from that school bake sale. Yum! Pay $50.'
Community_Card_12.price = -50
Community_Card_12.acty = 1

Community_Card_13 = Community()
Community_Card_13.description = "You set aside time every week to hang out with your elderly neighbor -- you've heard some amazing stories! Collect $100."
Community_Card_13.price = 100
Community_Card_13.acty = 1

Community_Card_14 = Community()
Community_Card_14.description = 'You help build a school playground -- then you get to test the slide! Collect $100.'
Community_Card_14.price = 100
Community_Card_14.acty = 1

Community_Card_15 = Community()
Community_Card_15.description = 'Your fuzzy friends at the animal shelter will be thankful for your donation. $50.'
Community_Card_15.price = -50
Community_Card_15.acty = 1

Community_Card_16 = Community()
Community_Card_16.description = 'You rescue a puppy -- and you feel rescued too! GET OUT OF JAIL FREE. This card may be kept until needed, traded, or sold.'
Community_Card_16.price = 0
Community_Card_16.acty = 6

community_card_list = [Community_Card_1, Community_Card_2, Community_Card_3, Community_Card_4, Community_Card_5, Community_Card_6, Community_Card_7, Community_Card_8,
                       Community_Card_9, Community_Card_10, Community_Card_11, Community_Card_12, Community_Card_13, Community_Card_14, Community_Card_15, Community_Card_16]


Utility_Card_1 = Utility()
Utility_Card_1.name = 'Water Works'
Utility_Card_1.description = 'If one Utility is owned, rent is four times amount shown on dice. If both utilities are owned, rent is 10 times amount shown on dice.'
Utility_Card_1.mortgage_val = 75
Utility_Card_1.unmortgage_val = 83

Utility_Card_2 = Utility()
Utility_Card_2.name = 'Electric Company'
Utility_Card_2.description = 'If one Utility is owned, rent is four times amount shown on dice. If both utilities are owned, rent is 10 times amount shown on dice.'
Utility_Card_2.mortgage_val = 75
Utility_Card_2.unmortgage_val = 83


Railroad_Card_4 = Railroad()
Railroad_Card_4.name = 'Short Line'

Railroad_Card_3 = Railroad()
Railroad_Card_3.name = 'B. & O. Railroad'

Railroad_Card_2 = Railroad()
Railroad_Card_2.name = 'Pennsylvania Railroad'

Railroad_Card_1 = Railroad()
Railroad_Card_1.name = 'Reading Railroad'

Property_Card_22 = Property()
Property_Card_22.name = 'Boardwalk'
Property_Card_22.description = 'Rent $50. Rent with color set: $100. Rent with 1 Property: $200. Rent with 2 Properties: $600. Rent with 3 Properties: $1,400. Rent with 4 Properties: $1,700. Rent with maxed Property: $2,000.'
Property_Card_22.rent = 50
Property_Card_22.rent_colorset = 100
Property_Card_22.rent_1_property = 200
Property_Card_22.rent_2_property = 600
Property_Card_22.rent_3_property = 1400
Property_Card_22.rent_4_property = 1700
Property_Card_22.rent_max = 2000
Property_Card_22.house_cost = 200
Property_Card_22.hotel_cost = 200
Property_Card_22.mortgage_val = 200
Property_Card_22.unmortgage_val = 220

Property_Card_21 = Property()
Property_Card_21.name = 'Park Place'
Property_Card_21.description = 'Rent $35. Rent with color set: $70. Rent with 1 Property: $175. Rent with 2 Properties: $500. Rent with 3 Properties: $1,100. Rent with 4 Properties: $1,300. Rent with maxed Property: $1,500.'
Property_Card_21.rent = 35
Property_Card_21.rent_colorset = 70
Property_Card_21.rent_1_property = 175
Property_Card_21.rent_2_property = 500
Property_Card_21.rent_3_property = 1100
Property_Card_21.rent_4_property = 1300
Property_Card_21.rent_max = 1500
Property_Card_21.house_cost = 200
Property_Card_21.hotel_cost = 200
Property_Card_21.mortgage_val = 175
Property_Card_21.unmortgage_val = 193

Property_Card_20 = Property()
Property_Card_20.name = 'Pennsylvania Avenue'
Property_Card_20.description = 'Rent $28. Rent with color set: $56. Rent with 1 Property: $150. Rent with 2 Properties: $450. Rent with 3 Properties: $1,000. Rent with 4 Properties: $1,200. Rent with maxed Property: $1,400.'
Property_Card_20.rent = 28
Property_Card_20.rent_colorset = 56
Property_Card_20.rent_1_property = 150
Property_Card_20.rent_2_property = 450
Property_Card_20.rent_3_property = 1000
Property_Card_20.rent_4_property = 1200
Property_Card_20.rent_max = 1400
Property_Card_20.house_cost = 200
Property_Card_20.hotel_cost = 200
Property_Card_20.mortgage_val = 160
Property_Card_20.unmortgage_val = 176

Property_Card_19 = Property()
Property_Card_19.name = 'North Carolina Avenue'
Property_Card_19.description = 'Rent $26. Rent with color set: $52. Rent with 1 Property: $130. Rent with 2 Properties: $390. Rent with 3 Properties: $900. Rent with 4 Properties: $1,100. Rent with maxed Property: $1,275.'
Property_Card_19.rent = 26
Property_Card_19.rent_colorset = 52
Property_Card_19.rent_1_property = 130
Property_Card_19.rent_2_property = 390
Property_Card_19.rent_3_property = 900
Property_Card_19.rent_4_property = 1100
Property_Card_19.rent_max = 1275
Property_Card_19.house_cost = 200
Property_Card_19.hotel_cost = 200
Property_Card_19.mortgage_val = 150
Property_Card_19.unmortgage_val = 165

Property_Card_18 = Property()
Property_Card_18.name = 'Pacific Avenue'
Property_Card_18.description = 'Rent $26. Rent with color set: $52. Rent with 1 Property: $130. Rent with 2 Properties: $390. Rent with 3 Properties: $900. Rent with 4 Properties: $1,100. Rent with maxed Property: $1,275.'
Property_Card_18.rent = 26
Property_Card_18.rent_colorset = 52
Property_Card_18.rent_1_property = 130
Property_Card_18.rent_2_property = 390
Property_Card_18.rent_3_property = 900
Property_Card_18.rent_4_property = 1100
Property_Card_18.rent_max = 1275
Property_Card_18.house_cost = 200
Property_Card_18.hotel_cost = 200
Property_Card_18.mortgage_val = 150
Property_Card_18.unmortgage_val = 165

Property_Card_17 = Property()
Property_Card_17.name = 'Marvin Gardens'
Property_Card_17.description = 'Rent $24. Rent with color set: $48. Rent with 1 Property: $120. Rent with 2 Properties: $360. Rent with 3 Properties: $850. Rent with 4 Properties: $1,025. Rent with maxed Property: $1,200.'
Property_Card_17.rent = 24
Property_Card_17.rent_colorset = 48
Property_Card_17.rent_1_property = 120
Property_Card_17.rent_2_property = 360
Property_Card_17.rent_3_property = 850
Property_Card_17.rent_4_property = 1025
Property_Card_17.rent_max = 1200
Property_Card_17.house_cost = 150
Property_Card_17.hotel_cost = 150
Property_Card_17.mortgage_val = 140
Property_Card_17.unmortgage_val = 154

Property_Card_16 = Property()
Property_Card_16.name = 'Ventnor Avenue'
Property_Card_16.description = 'Rent $22. Rent with color set: $44. Rent with 1 Property: $110. Rent with 2 Properties: $330. Rent with 3 Properties: $800. Rent with 4 Properties: $975. Rent with maxed Property: $1,150.'
Property_Card_16.rent = 22
Property_Card_16.rent_colorset = 44
Property_Card_16.rent_1_property = 110
Property_Card_16.rent_2_property = 330
Property_Card_16.rent_3_property = 800
Property_Card_16.rent_4_property = 975
Property_Card_16.rent_max = 1150
Property_Card_16.house_cost = 150
Property_Card_16.hotel_cost = 150
Property_Card_16.mortgage_val = 130
Property_Card_16.unmortgage_val = 143

Property_Card_15 = Property()
Property_Card_15.name = 'Atlantic Avenue'
Property_Card_15.description = 'Rent $22. Rent with color set: $44. Rent with 1 Property: $110. Rent with 2 Properties: $330. Rent with 3 Properties: $800. Rent with 4 Properties: $975. Rent with maxed Property: $1,150.'
Property_Card_15.rent = 22
Property_Card_15.rent_colorset = 44
Property_Card_15.rent_1_property = 110
Property_Card_15.rent_2_property = 330
Property_Card_15.rent_3_property = 800
Property_Card_15.rent_4_property = 975
Property_Card_15.rent_max = 1150
Property_Card_15.house_cost = 150
Property_Card_15.hotel_cost = 150
Property_Card_15.mortgage_val = 130
Property_Card_15.unmortgage_val = 143

Property_Card_14 = Property()
Property_Card_14.name = 'Illinois Avenue'
Property_Card_14.description = 'Rent $20. Rent with color set: $40. Rent with 1 Property: $100. Rent with 2 Properties: $300. Rent with 3 Properties: $750. Rent with 4 Properties: $925. Rent with maxed Property: $1,100.'
Property_Card_14.rent = 20
Property_Card_14.rent_colorset = 40
Property_Card_14.rent_1_property = 100
Property_Card_14.rent_2_property = 300
Property_Card_14.rent_3_property = 750
Property_Card_14.rent_4_property = 925
Property_Card_14.rent_max = 1100
Property_Card_14.house_cost = 150
Property_Card_14.hotel_cost = 150
Property_Card_14.mortgage_val = 120
Property_Card_14.unmortgage_val = 132

Property_Card_13 = Property()
Property_Card_13.name = 'Indiana Avenue'
Property_Card_13.description = 'Rent $18. Rent with color set: $36. Rent with 1 Property: $90. Rent with 2 Properties: $250. Rent with 3 Properties: $700. Rent with 4 Properties: $875. Rent with maxed Property: $1,050.'
Property_Card_13.rent = 18
Property_Card_13.rent_colorset = 36
Property_Card_13.rent_1_property = 90
Property_Card_13.rent_2_property = 250
Property_Card_13.rent_3_property = 700
Property_Card_13.rent_4_property = 875
Property_Card_13.rent_max = 1050
Property_Card_13.house_cost = 150
Property_Card_13.hotel_cost = 150
Property_Card_13.mortgage_val = 110
Property_Card_13.unmortgage_val = 121

Property_Card_12 = Property()
Property_Card_12.name = 'Kentucky Avenue'
Property_Card_12.description = 'Rent $18. Rent with color set: $36. Rent with 1 Property: $90. Rent with 2 Properties: $250. Rent with 3 Properties: $700. Rent with 4 Properties: $875. Rent with maxed Property: $1,050.'
Property_Card_12.rent = 18
Property_Card_12.rent_colorset = 36
Property_Card_12.rent_1_property = 90
Property_Card_12.rent_2_property = 250
Property_Card_12.rent_3_property = 700
Property_Card_12.rent_4_property = 875
Property_Card_12.rent_max = 1050
Property_Card_12.house_cost = 150
Property_Card_12.hotel_cost = 150
Property_Card_12.mortgage_val = 110
Property_Card_12.unmortgage_val = 121

Property_Card_11 = Property()
Property_Card_11.name = 'New York Avenue'
Property_Card_11.description = 'Rent $16. Rent with color set: $32. Rent with 1 Property: $80. Rent with 2 Properties: $220. Rent with 3 Properties: $600. Rent with 4 Properties: $800. Rent with maxed Property: $1,000.'
Property_Card_11.rent = 16
Property_Card_11.rent_colorset = 32
Property_Card_11.rent_1_property = 80
Property_Card_11.rent_2_property = 220
Property_Card_11.rent_3_property = 600
Property_Card_11.rent_4_property = 800
Property_Card_11.rent_max = 1000
Property_Card_11.house_cost = 100
Property_Card_11.hotel_cost = 100
Property_Card_11.mortgage_val = 100
Property_Card_11.unmortgage_val = 110

Property_Card_10 = Property()
Property_Card_10.name = 'Tennessee Avenue'
Property_Card_10.description = 'Rent $14. Rent with color set: $28. Rent with 1 Property: $70. Rent with 2 Properties: $200. Rent with 3 Properties: $550. Rent with 4 Properties: $750. Rent with maxed Property: $950.'
Property_Card_10.rent = 14
Property_Card_10.rent_colorset = 28
Property_Card_10.rent_1_property = 70
Property_Card_10.rent_2_property = 200
Property_Card_10.rent_3_property = 550
Property_Card_10.rent_4_property = 750
Property_Card_10.rent_max = 950
Property_Card_10.house_cost = 100
Property_Card_10.hotel_cost = 100
Property_Card_10.mortgage_val = 90
Property_Card_10.unmortgage_val = 99

Property_Card_9 = Property()
Property_Card_9.name = 'ST. James Place'
Property_Card_9.description = 'Rent $14. Rent with color set: $28. Rent with 1 Property: $70. Rent with 2 Properties: $200. Rent with 3 Properties: $550. Rent with 4 Properties: $750. Rent with maxed Property: $950.'
Property_Card_9.rent = 14
Property_Card_9.rent_colorset = 28
Property_Card_9.rent_1_property = 70
Property_Card_9.rent_2_property = 200
Property_Card_9.rent_3_property = 550
Property_Card_9.rent_4_property = 750
Property_Card_9.rent_max = 950
Property_Card_9.house_cost = 100
Property_Card_9.hotel_cost = 100
Property_Card_9.mortgage_val = 90
Property_Card_9.unmortgage_val = 99

Property_Card_8 = Property()
Property_Card_8.name = 'Viginia Avenue'
Property_Card_8.description = 'Rent $12. Rent with color set: $24. Rent with 1 Property: $60. Rent with 2 Properties: $180. Rent with 3 Properties: $500. Rent with 4 Properties: $700. Rent with maxed Property: $900.'
Property_Card_8.rent = 12
Property_Card_8.rent_colorset = 24
Property_Card_8.rent_1_property = 60
Property_Card_8.rent_2_property = 180
Property_Card_8.rent_3_property = 500
Property_Card_8.rent_4_property = 700
Property_Card_8.rent_max = 900
Property_Card_8.house_cost = 100
Property_Card_8.hotel_cost = 100
Property_Card_8.mortgage_val = 80
Property_Card_8.unmortgage_val = 88

Property_Card_7 = Property()
Property_Card_7.name = 'States Avenue'
Property_Card_7.description = 'Rent $10. Rent with color set: $20. Rent with 1 Property: $50. Rent with 2 Properties: $150. Rent with 3 Properties: $450. Rent with 4 Properties: $625. Rent with maxed Property: $750.'
Property_Card_7.rent = 10
Property_Card_7.rent_colorset = 20
Property_Card_7.rent_1_property = 50
Property_Card_7.rent_2_property = 150
Property_Card_7.rent_3_property = 450
Property_Card_7.rent_4_property = 625
Property_Card_7.rent_max = 750
Property_Card_7.house_cost = 100
Property_Card_7.hotel_cost = 100
Property_Card_7.mortgage_val = 70
Property_Card_7.unmortgage_val = 77

Property_Card_6 = Property()
Property_Card_6.name = 'ST. Charles Place'
Property_Card_6.description = 'Rent $10. Rent with color set: $20. Rent with 1 Property: $50. Rent with 2 Properties: $150. Rent with 3 Properties: $450. Rent with 4 Properties: $625. Rent with maxed Property: $750.'
Property_Card_6.rent = 10
Property_Card_6.rent_colorset = 20
Property_Card_6.rent_1_property = 50
Property_Card_6.rent_2_property = 150
Property_Card_6.rent_3_property = 450
Property_Card_6.rent_4_property = 625
Property_Card_6.rent_max = 750
Property_Card_6.house_cost = 100
Property_Card_6.hotel_cost = 100
Property_Card_6.mortgage_val = 70
Property_Card_6.unmortgage_val = 77

Property_Card_5 = Property()
Property_Card_5.name = 'Connecticut Avenue'
Property_Card_5.description = 'Rent $8. Rent with color set: $16. Rent with 1 Property: $40. Rent with 2 Properties: $100. Rent with 3 Properties: $300. Rent with 4 Properties: $450. Rent with maxed Property: $600.'
Property_Card_5.rent = 8
Property_Card_5.rent_colorset = 16
Property_Card_5.rent_1_property = 40
Property_Card_5.rent_2_property = 100
Property_Card_5.rent_3_property = 300
Property_Card_5.rent_4_property = 450
Property_Card_5.rent_max = 600
Property_Card_5.house_cost = 50
Property_Card_5.hotel_cost = 50
Property_Card_5.mortgage_val = 60
Property_Card_5.unmortgage_val = 66

Property_Card_4 = Property()
Property_Card_4.name = 'Vermont Avenue'
Property_Card_4.description = 'Rent $6. Rent with color set: $12. Rent with 1 Property: $30. Rent with 2 Properties: $90. Rent with 3 Properties: $270. Rent with 4 Properties: $400. Rent with maxed Property: $550.'
Property_Card_4.rent = 6
Property_Card_4.rent_colorset = 12
Property_Card_4.rent_1_property = 30
Property_Card_4.rent_2_property = 90
Property_Card_4.rent_3_property = 270
Property_Card_4.rent_4_property = 400
Property_Card_4.rent_max = 550
Property_Card_4.house_cost = 50
Property_Card_4.hotel_cost = 50
Property_Card_4.mortgage_val = 50
Property_Card_4.unmortgage_val = 55

Property_Card_3 = Property()
Property_Card_3.name = 'Oriental Avenue'
Property_Card_3.description = 'Rent $6. Rent with color set: $12. Rent with 1 Property: $30. Rent with 2 Properties: $90. Rent with 3 Properties: $270. Rent with 4 Properties: $400. Rent with maxed Property: $550.'
Property_Card_3.rent = 6
Property_Card_3.rent_colorset = 12
Property_Card_3.rent_1_property = 30
Property_Card_3.rent_2_property = 90
Property_Card_3.rent_3_property = 270
Property_Card_3.rent_4_property = 400
Property_Card_3.rent_max = 550
Property_Card_3.house_cost = 50
Property_Card_3.hotel_cost = 50
Property_Card_3.mortgage_val = 50
Property_Card_3.unmortgage_val = 55

Property_Card_2 = Property()
Property_Card_2.name = 'Baltic Avenue'
Property_Card_2.description = 'Rent $4. Rent with color set: $8. Rent with 1 Property: $20. Rent with 2 Properties: $60. Rent with 3 Properties: $180. Rent with 4 Properties: $320. Rent with maxed Property: $450.'
Property_Card_2.rent = 4
Property_Card_2.rent_colorset = 8
Property_Card_2.rent_1_property = 20
Property_Card_2.rent_2_property = 60
Property_Card_2.rent_3_property = 180
Property_Card_2.rent_4_property = 320
Property_Card_2.rent_max = 450
Property_Card_2.house_cost = 50
Property_Card_2.hotel_cost = 50
Property_Card_2.mortgage_val = 30
Property_Card_2.unmortgage_val = 33

Property_Card_1 = Property()
Property_Card_1.name = 'Mediterranean Avenue'
Property_Card_1.description = 'Rent $2. Rent with color set: $4. Rent with 1 Property: $10. Rent with 2 Properties: $30. Rent with 3 Properties: $90. Rent with 4 Properties: $160. Rent with maxed Property: $250.'
Property_Card_1.rent = 2
Property_Card_1.rent_colorset = 4
Property_Card_1.rent_1_property = 10
Property_Card_1.rent_2_property = 30
Property_Card_1.rent_3_property = 90
Property_Card_1.rent_4_property = 160
Property_Card_1.rent_max = 250
Property_Card_1.house_cost = 50
Property_Card_1.hotel_cost = 50
Property_Card_1.mortgage_val = 30
Property_Card_1.unmortgage_val = 33
