import random
from player import *
from bank import *
from board import *
from card import *

def picker_y_n():
    while True:
        q = input('Property available! -would you like to purchase? (y/n): ')
        if q.lower() not in ('y','n'):
            print("Not an appropriate choice.")
        else:
            return q

def property_handler(space, player):
    if isinstance(space, Property_Space):
        if space.status == 0:
            if player.ai == 1 and player.prop_propensity == 1:
                q = 'y'
                space.status = 1
                space.owner = player
                # player.property_list['space'] = space
                player.property_list[space] = space.color
                player.balance -= space.price
                bank.balance += space.price
                print(player.name+', '+space.name +
                      ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                return
            if player.ai == 1 and player.prop_propensity == 0:
                q = 'n'
                print(player.name+', '+space.name +
                      ' has passed on purchasing this property. your balance remains $'+str(player.balance)+'\n')
                return
            if player.ai == 0:
                q = picker_y_n()
                if q == 'y':
                    space.status = 1
                    space.owner = player
                    # player.property_list['space'] = space
                    player.property_list[space] = space.color
                    player.balance -= space.price
                    bank.balance += space.price
                    print(player.name+', '+space.name +
                        ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                if q == 'n':
                    print(player.name+', '+space.name +
                      ' has passed on purchasing this property. your balance remains $'+str(player.balance)+'\n')
                    return
        elif space.status == 1:
            ct = 0
            for color in space.owner.property_list.values():
                if color == space.color:
                    # print(color)
                    # print(space.color)
                    ct += 1
                    continue
            print(space.name+' is currently owned by ' + space.owner.name + ' who has '+str(
                ct)+' of '+str(space.owner.max_list.get(space.color))+' space(s) from the '+space.color+' color set\n' + space.card.description)
            if ct < player.max_list.get(space.color):
                rent = space.card.rent
                player.balance -= rent
                space.owner.balance += rent
            elif ct == player.max_list.get(space.color) and space.houses == 0:
                rent = space.card.rent_colorset
                player.balance -= rent
                space.owner.balance += rent
            print(player.name+', $'+str(rent)+' in rent has been paid to ' +
                  space.owner.name+'. Your balance is now $' + str(player.balance)+'\n')
            return
        else:
            return
    else:
        return


def community_handler(space, player):
    if isinstance(space, Community_Space):
        comm_card_idx = 0
        for i in ordered_player_list:

            # testing
            # print(i.name)

            comm_card_idx += i.player_comm_card_ct
            continue

        # testing
        # print(comm_card_idx)

        card = community_card_list[comm_card_idx]
        print(card.description)
        player.player_comm_card_ct += 1

        if card.acty == 1:
            player.balance += card.price
            bank.balance -= card.price
            print(player.name+', Your balance is now $' +
                  str(player.balance)+'\n')
            return
        elif card.acty == 2:
            player.space_no = 0
            space.no = 0
            board_index = 0
            space = board[board_index]
            go_handler(space, player)
            return
        elif card.acty == 3:
            penalty = ((player.houses*40)+(player.hotels*115))
            player.balance -= penalty
            bank.balance += penalty
            print(player.name+' has '+str(player.houses)+' houses & '+str(player.hotels) + ' hotels\nA penalty of $' +
                  str(penalty)+' has been assessed\n'+player.name+', your balance is now $' + str(player.balance)+'\n')
            return
        elif card.acty == 4:
            for gamery in ordered_player_list:
                if gamery.name != player.name:
                    gamery.balance -= 10
                    player.balance += 10
                    print(player.name+', '+gamery.name +
                          ' has paid you $10 and your balance is now $'+str(gamery.balance))
                    continue
            print(player.name+', your balance is now $' +
                  str(player.balance)+'\n')
        elif card.acty == 5:
            player.space_no = 30
            space.no = 30
            board_index = 30
            space = board[board_index]
            jail_handler_go_to(space, player)
            return
        elif card.acty == 6:
            player.getoutofjail_status += 1
            print()
            return
        else:
            return
    else:
        return


def chance_handler(space, player):
    if isinstance(space, Chance_Space):
        chance_card_idx = 0
        for i in ordered_player_list:

            # testing
            # print(i.name)

            chance_card_idx += i.player_chance_card_ct
            continue

        # testing
        # print(chance_card_idx)

        card = chance_card_list[chance_card_idx]
        print(card.description)
        player.player_chance_card_ct += 1

        # testing
        # print('you git it')

        if card.movement == 0:
            player.balance += card.price
            bank.balance -= card.price
            print(player.name+', Your balance is now ' + str(player.balance)+'\n')
        elif card.movement == 1:

            # testing
            # print('Chance spaces: 7,22,36')
            # print('Railroad spaces: 5,15,25,35')
            # print('Current Space No: '+str(space.no))
            # print('Current Player Space No: '+str(player.space_no))

            if space.no == 7:
                who_turn.space_no = 15
                board_index = 15
                space = board[board_index]
                player = who_turn

                # testing
                # print('Current Space No: '+str(space.no))
                # print('Current Player Space No: '+str(player.space_no))

                railroad_handler_x2rent(space, player)
            elif space.no == 22:
                who_turn.space_no = 25
                board_index = 25
                space = board[board_index]
                player = who_turn

                # testing
                # print('Current Space No: '+str(space.no))
                # print('Current Player Space No: '+str(player.space_no))

                railroad_handler_x2rent(space, player)
            elif space.no == 36:
                who_turn.space_no = 5
                board_index = 5
                space = board[board_index]
                player = who_turn

                # testing
                # print('Current Space No: '+str(space.no))
                # print('Current Player Space No: '+str(player.space_no))#

                player.balance += 200
                bank.balance -= 200

                # add language that I passed Go
                print(player.name+', your balance is now $' +
                      str(player.balance)+'\n')
                railroad_handler_x2rent(space, player)
            else:
                return
        elif card.movement == 2:

            # testing
            # print('Current Space No: '+str(space.no))
            # print('Current Player Space No: '+str(player.space_no))

            who_turn.space_no -= 3
            # space.no -= 3
            current_space = who_turn.space_no
            print('current space: '+str(current_space))

            # testing - make this number the board index?
            # print('Current Player Space No: '+str(player.space_no))

            space = board[current_space]
            player = who_turn

            # testing
            # print('Current Space No: '+str(space.no))
            # print('Current Player Space No: '+str(player.space_no))

            tax_handler(space, player)
            property_handler(space, player)
            community_handler(space, player)
            return
        elif card.movement == 3:
            for gamer in ordered_player_list:
                if gamer.name != player.name:

                    # testing
                    # print(player.balance)

                    gamer.balance += 50
                    player.balance -= 50
                    print(gamer.name+', '+player.name +
                          ' has paid you $50 and your balance is now $'+str(gamer.balance))

                    # testing
                    # print(player.balance)
                    # print()
                else:
                    continue
            print(player.name+', your balance is now $'+str(player.balance)+'\n')
        elif card.movement == 4:
            if player.space_no < 11:
                interval_neg = 11-player.space_no
                player.space_no += interval_neg
            elif player.space_no > 10:
                interval_pos = (40-player.space_no)+11
                player.space_no += interval_pos
                player.balance += 200
                bank.balance -= 200
                print(
                    player.name + ' has passed Go. Your balance is now $'+str(player.balance))
            else:
                return
            board_index = 11
            space = board[board_index]

            # testing
            #print(space.name)

            player = who_turn
            property_handler(space, player)
            return
        elif card.movement == 5:
            player.getoutofjail_status += 1
            print('jail status: '+str(player.getoutofjail_status)+'\n')
            return
        elif card.movement == 6:
            penalty = ((player.houses*25)+(player.hotels*100))
            player.balance -= penalty
            bank.balance += penalty
            print(player.name+' has '+str(player.houses)+' houses & '+str(player.hotels) + ' hotels\nA penalty of $' +
                  str(penalty)+' has been assessed\n'+player.name+', your balance is now $' + str(player.balance)+'\n')
            return
        elif card.movement == 7:
            player.space_no = 0
            space.no = 0
            board_index = 0
            space = board[board_index]
            go_handler(space, player)
            return
        elif card.movement == 8:
            player.space_no = 30
            space.no = 30
            board_index = 30
            space = board[board_index]
            jail_handler_go_to(space, player)
            return
        elif card.movement == 9:
            if space.no < 12:
                player.space_no = 12
                space.no = 12
                board_index = 12
                space = board[board_index]
                utility_handler(space, player)
            elif space.no < 28 and space.no > 12:
                player.space_no = 28
                space.no = 28
                board_index = 28
                space = board[board_index]
                utility_handler(space, player)
            elif space.no > 28:
                player.space_no = 12
                space.no = 12
                board_index = 12
                space = board[board_index]
                utility_handler(space, player)
            else:
                return
        elif card.movement == 10:
            if player.space_no < 24:
                player.space_no = 24
                space.no = 24
                board_index = 24
                space = board[board_index]
                property_handler(space, player)
                return
            elif player.space_no > 24:
                player.space_no = 24
                space.no = 24
                board_index = 24
                space = board[board_index]
                player.balance += 200
                bank.balance -= 200
                print(
                    player.name + ' has passed Go. Your balance is now $'+str(player.balance))
                property_handler(space, player)
                return
        elif card.movement == 11:
            if player.space_no < 5:
                player.space_no = 5
                space.no = 5
                board_index = 5
                space = board[board_index]
                railroad_handler(space, player)
                return
            elif player.space_no > 5:
                player.space_no = 5
                space.no = 5
                board_index = 5
                space = board[board_index]
                player.balance += 200
                bank.balance -= 200
                print(
                    player.name + ' has passed Go. Your balance is now $'+str(player.balance))
                railroad_handler(space, player)
                return
        elif card.movement == 12:
            player.space_no = 39
            space.no = 39
            board_index = 39
            space = board[board_index]
            property_handler(space, player)
            return
        else:
            return
    else:
        return


def tax_handler(space, player):
    if isinstance(space, Tax_Space):
        # print(space.name)
        player.balance -= space.price
        print(player.name+', your balance is now $' +
              str(player.balance)+'\n')
        return
    else:
        return


def utility_handler(space, player):
    if isinstance(space, Utility_Space):
        # print(space.name)
        if space.status == 0:
            if player.ai == 1 and player.prop_propensity == 1:
                q = 'y'
                space.status = 1
                space.owner = player
                player.utility_ct += 1
                player.balance -= space.price
                bank.balance += space.price
                print(player.name+', '+space.name +
                      ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                return
            if player.ai == 1 and player.prop_propensity == 0:
                q = 'n'
                print(player.name+', '+space.name +
                      ' has passed on purchasing this property. your balance remains $'+str(player.balance)+'\n')
                return
            if player.ai == 0:
                q = picker_y_n()
                if q == 'y':
                    space.status = 1
                    space.owner = player
                    player.utility_ct += 1
                    player.balance -= space.price
                    bank.balance += space.price
                    print(player.name+', '+space.name +
                        ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                    return
                if q == 'n':
                    print(player.name+', '+space.name +
                      ' has passed on purchasing this property. your balance remains $'+str(player.balance)+'\n')
                    return
        if space.status == 1 and player.ai == 0:
            print(space.name+' is currently owned by ' + space.owner.name +
                  ' who has '+str(space.owner.utility_ct)+' Utility space(s)')
            print(space.card.description)
            roll = who_turn.dice_roll()
            print(player.name+' has rolled a '+str(roll))
            if space.owner.utility_ct == 1:
                utility_cost = 4*roll
            elif space.owner.utility_ct == 2:
                utility_cost = 10*roll
            else:
                return

            player.balance -= utility_cost
            space.owner.balance += utility_cost

            print(player.name+', your balance is now $' +
                  str(player.balance)+'\n'+space.owner.name+', your balance is now $' +
                  str(space.owner.balance)+'\n')
            return
        else:
            return
    else:
        return


def railroad_handler(space, player):
    if isinstance(space, Railroad_Space):
        # print(space.name)
        if space.status == 0:
            if player.ai == 1 and player.prop_propensity == 1:
                q = 'y'
                space.status = 1
                space.owner = player
                player.rr_ct += 1
                player.balance -= space.price
                bank.balance += space.price
                print(player.name+', '+space.name +
                      ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                return
            if player.ai == 1 and player.prop_propensity == 0:
                q = 'n'
                print(player.name+', '+space.name +
                      ' has passed on purchasing this property. your balance remains $'+str(player.balance)+'\n')
                return
            if player.ai == 0:
                q = picker_y_n()
                if q == 'y':
                    space.status = 1
                    space.owner = player
                    player.rr_ct += 1
                    player.balance -= space.price
                    bank.balance += space.price
                    print(player.name+', '+space.name +
                        ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                    return
                if q == 'n':
                    print(player.name+', '+space.name +
                      ' has passed on purchasing this property. your balance remains $'+str(player.balance)+'\n')
                    return
        if space.status == 1:

            # testing
            # print(space.owner)
            # print(space.owner.rr_ct)

            print(space.name+' is currently owned by ' + space.owner.name +
                    ' who has '+str(space.owner.rr_ct)+' Railroad space(s)')
            print(space.card.description)
            if space.owner.rr_ct == 1:
                rr_cost = 25
            elif space.owner.rr_ct == 2:
                rr_cost = 50
            elif space.owner.rr_ct == 3:
                rr_cost = 100
            elif space.owner.rr_ct == 4:
                rr_cost = 200
            else:
                return

            # testing
            # print('Player Bal: '+str(player.balance))
            # print('Space Own Bal: '+str(space.owner.balance))

            player.balance -= rr_cost
            space.owner.balance += rr_cost

            # testing
            # print('Space Own Bal: '+str(space.owner.balance))

            print(player.name+', your balance is now $' +
                    str(player.balance)+'\n')
            return
        else:
            return
    else:
        return


def railroad_handler_x2rent(space, player):
    # 2X rent for Chance cards 2 & 3 w/ no auction
    if isinstance(space, Railroad_Space):
        # print(space.name)
        if space.status == 0:
            if player.ai == 1 and player.prop_propensity == 1:
                q = 'y'
                space.status = 1
                space.owner = player
                player.rr_ct += 1
                player.balance -= space.price
                bank.balance += space.price
                print(player.name+', '+space.name +
                      ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                return
            if player.ai == 1 and player.prop_propensity == 0:
                q = 'n'
                print(player.name+', '+space.name +
                      ' has passed on purchasing this property. your balance remains $'+str(player.balance)+'\n')
                return
            if player.ai == 0:
                q = picker_y_n()
                if q == 'y':
                    space.status = 1
                    space.owner = player
                    player.rr_ct += 1
                    player.balance -= space.price
                    bank.balance += space.price
                    print(player.name+', '+space.name +
                        ' has been purchased and your balance is now $'+str(player.balance)+'\n')
                    return
        if space.status == 1:

            # testing
            # print(space.owner)
            # print(space.owner.rr_ct)

            print(space.name+' is currently owned by ' + space.owner.name +
                  ' who has '+str(space.owner.rr_ct)+' Railroad space(s)')
            print(space.card.description)
            if space.owner.rr_ct == 1:
                rr_cost = 50
            elif space.owner.rr_ct == 2:
                rr_cost = 100
            elif space.owner.rr_ct == 3:
                rr_cost = 200
            elif space.owner.rr_ct == 4:
                rr_cost = 400
            else:
                return

            # testing
            # print('Player Bal: '+str(player.balance))
            # print('Space Own Bal: '+str(space.owner.balance))

            player.balance -= rr_cost
            space.owner.balance += rr_cost

            # testing
            # print('Space Own Bal: '+str(space.owner.balance))

            print(player.name+', your balance is now $' +
                  str(player.balance)+'\n')
            return
        else:
            return
    else:
        return


def jail_handler_go_to(space, player):
    if isinstance(space, Jail_Space_Go_To):
        player.areyouinjail += 1
        # print('upping areyouinjailcounter: '+str(player.areyouinjail)+'\n')
        print()
        return
    else:
        return

def jail_handler_just_visiting(space, player):
    if isinstance(space, Jail_Space_Just_Visting):
        # player.areyouinjail += 1
        print()
        return
    else:
        return


def parking_handler(space, player):
    if isinstance(space, Parking_Space):
        # print(space.name+'\n')
        print()
        return
    else:
        return


def go_handler(space, player):
    if isinstance(space, Go_Space):
        print(space.name)
        player.balance += 200
        bank.balance -= 200
        print(player.name+', your balance is now $'+str(player.balance)+'\n')
        return
    else:
        return

print('\nWelcome to... Four Player Monopoly!\nThis game will be played with 3 computer players (Luis, Sarah & Kathleen) and you can join the fun!')
human_player_ct = 'y'  # use code below
# input('Would you like to play? (y/n): ')

player_list = []

if human_player_ct == 'y':
    ai_player_ct = 3
    human_player1 = input('\nHuman Player please enter your name!: ')
    human_player1 = Player(human_player1)
    player_list.append(human_player1)
    human_player1.init_dice_roll()
    print('\nWelcome '+human_player1.name+'! your balance is: $' + str(human_player1.balance) +
          '\nYour initial dice roll is: '+str(human_player1.init_roll))
else:
    ai_player_ct = 4

ai_player1 = Player('Luis')
player_list.append(ai_player1)
ai_player1.ai = 1
ai_player1.init_dice_roll()
print('\nWelcome '+ai_player1.name+'! your balance is: $' +
      str(ai_player1.balance) + '\nYour initial dice roll is: '+str(ai_player1.init_roll))

ai_player2 = Player('Sarah')
player_list.append(ai_player2)
ai_player2.ai = 1
ai_player2.init_dice_roll()
print('\nWelcome '+ai_player2.name+'! your balance is: $' +
      str(ai_player2.balance)+'\nYour initial dice roll is: '+str(ai_player2.init_roll))

ai_player3 = Player('Kathleen')
player_list.append(ai_player3)
ai_player3.ai = 1
ai_player3.init_dice_roll()
print('\nWelcome '+ai_player3.name+'! your balance is: $' +
      str(ai_player3.balance)+'\nYour initial dice roll is: '+str(ai_player3.init_roll))

if ai_player_ct == 4:
    ai_player4 = Player('Philip')
    player_list.append(ai_player4)
    ai_player4.ai = 1
    ai_player4.init_dice_roll()
    print('\nWelcome '+ai_player4.name+'! your balance is: $' +
          str(ai_player4.balance)+'\nYour initial dice roll is: '+str(ai_player4.init_roll))

bank = Bank()
print('\nBank instantiated!\n$'+str(bank.balance)+' available\n' + str(bank.hotels) +
      ' hotels available\n'+str(bank.houses)+' houses available')

high_roll_list = sorted(player_list, key=lambda x: x.init_roll)
print('\nCongratulations! The initial roll winner is ' +
      high_roll_list[-1].name+' with a roll of: '+str(high_roll_list[-1].init_roll)+'\n')

init_roll_winner_index = player_list.index(high_roll_list[-1])
ordered_player_list = []
ordered_player_list.append(player_list[init_roll_winner_index])
player_list.pop(init_roll_winner_index)
ordered_player_list += player_list

game_turn_idx = 0
game_turn_iter = 1

game = True
while game:

    game_turn_idx += game_turn_iter

    # testing - use to shorten game!
    if game_turn_idx == 45:
        game = False

    # testing
    # print('Game Turn: '+str(game_turn_idx)+'\n')

    for who_turn in ordered_player_list:

        #if who_turn.doubles_tries == 3:
            #who_turn.doubles_tries = 0
        # testing
        # print(who_turn.property_list)
        # print(who_turn.property_list.values)

        howtogetout = 0

        if who_turn.areyouinjail == 1:
            print(who_turn.name+', how would you like to leave jail? -you have 3 options:\n1. pay $50 and begin your turn\n2. roll doubles\n3. use your Get Out of Jail Free card')
            if who_turn.ai == 1:
                howtogetout = random.randint(1,3)
            else:
                howtogetout = int(input('Please select(1, 2 or 3): '))

        if howtogetout == 3 and who_turn.getoutofjail_status > 0:
                who_turn.getoutofjail_status -= 1
                who_turn.areyouinjail -= 1
                print(
                    who_turn.name+', you have elected to use your Get Out of Jail Free card. Continue game-play!')
        
        if howtogetout == 3 and who_turn.getoutofjail_status == 0:
                print(
                    who_turn.name+', you do not have a Get Out of Jail Free card. Try another option.\n')

        if howtogetout == 3:
            print(who_turn.name+', how would you like to leave jail? -you have 2 options:\n1. pay $50 and begin your turn\n2. roll doubles\n')
            if who_turn.ai == 1:
                howtogetout = random.randint(1,2)
            else:
                howtogetout = int(input('Please select(1 or 2): '))        
        
        if howtogetout == 1:
            who_turn.areyouinjail -= 1
            who_turn.balance -= 50
            bank.balance += 50
            print(who_turn.name+', you have elected to pay $50 and leave jail and continue with your turn\nYour new balance is $'+str(who_turn.balance)+'\n')

        if howtogetout == 2:
            doubles_roll_1 = who_turn.dice_roll_doubles()
            doubles_roll_2 = who_turn.dice_roll_doubles()
            doubles_roll = doubles_roll_1+doubles_roll_2

            if who_turn.doubles_tries < 2:
                print(who_turn.name +
                        ', you have elected to try for doubles!')
                print('Please roll your dice\nYou have rolled a ' +
                        str(doubles_roll_1) + ' and a ' + str(doubles_roll_2))
                if doubles_roll_1 == doubles_roll_2:
                    who_turn.areyouinjail -= 1
                    print('Congratulations! you have rolled doubles. Please advance ' +
                            str(doubles_roll)+' spaces. That is the end of your turn.')
                elif doubles_roll_1 != doubles_roll_2:
                    who_turn.doubles_tries += 1
                    tries_left = 3-who_turn.doubles_tries
                    print(
                        'Sorry, you have not rolled doubles this turn. You have '+str(tries_left)+' tries left.'+'\n')

            elif who_turn.doubles_tries == 2:
                print(who_turn.name +
                        ', this is your last try for doubles!')
                print('Please roll your dice\nYou have rolled a ' +
                        str(doubles_roll_1) + ' and a ' + str(doubles_roll_2))
                if doubles_roll_1 != doubles_roll_2:
                    who_turn.doubles_tries += 1
                    tries_left = 3-who_turn.doubles_tries
                    who_turn.areyouinjail = 0
                    print(
                        'Sorry you have not rolled doubles this turn. You have '+str(tries_left)+' tries left.')
                    print(who_turn.name+', pay $50, leave jail and advance ' +
                            str(doubles_roll)+' spaces. That is the end of your turn.\nYour new balance is $'+str(who_turn.balance))

                elif doubles_roll_1 == doubles_roll_2:
                    who_turn.areyouinjail -= 1
                    print('Congratulations! you have rolled doubles. Please advance ' +
                            str(doubles_roll)+' spaces. That is the end of your turn.\n')

        if who_turn.doubles_tries == 0:                

            who_turn_roll = who_turn.dice_roll()
            who_turn_space = who_turn.space_no        

            print(who_turn.name + ', your balance is $' + str(who_turn.balance) +
                '. Please roll your dice!\nYou have rolled: ' + str(who_turn_roll))

            # testing
            # print('Prev Space: '+str(who_turn_space))
            # print('before 40: '+str(board_index))

            board_index = who_turn_roll + who_turn_space

            if board_index > 39:
                board_index = board_index - 40
            else:
                board_index = who_turn_roll + who_turn_space

            who_turn.space_no += who_turn_roll

            if who_turn.space_no > 39:
                who_turn.space_no = who_turn.space_no - 40
            else:
                board_index = who_turn_roll + who_turn_space

            # testing
            # print('after 40: '+str(board_index)
            # print('Current Space: '+str(who_turn.space_no))

            print('Please advance ' + str(who_turn_roll) +
                ' space(s) to: '+board[who_turn.space_no].name)

            space = board[board_index]
            player = who_turn

            property_handler(space, player)
            community_handler(space, player)
            tax_handler(space, player)
            chance_handler(space, player)
            utility_handler(space, player)
            railroad_handler(space, player)
            parking_handler(space, player)
            jail_handler_go_to(space, player)
            jail_handler_just_visiting(space, player)
            go_handler(space, player)

        if who_turn.doubles_tries > 0 and who_turn.areyouinjail == 0:                

            who_turn_roll = doubles_roll
            who_turn_space = who_turn.space_no 
            if who_turn.doubles_tries == 3:
                who_turn.doubles_tries = 0       

            # testing
            # print('Prev Space: '+str(who_turn_space))
            # print('before 40: '+str(board_index))

            board_index = who_turn_roll + who_turn_space

            if board_index > 39:
                board_index = board_index - 40
            else:
                board_index = who_turn_roll + who_turn_space

            who_turn.space_no += who_turn_roll

            if who_turn.space_no > 39:
                who_turn.space_no = who_turn.space_no - 40
            else:
                board_index = who_turn_roll + who_turn_space

            # testing
            # print('after 40: '+str(board_index)
            # print('Current Space: '+str(who_turn.space_no))

            print('Please advance ' + str(who_turn_roll) +
                ' space(s) to: '+board[who_turn.space_no].name)
            
            #who_turn.doubles_tries = 0
            #print(who_turn.doubles_tries)

            space = board[board_index]
            player = who_turn

            property_handler(space, player)
            community_handler(space, player)
            tax_handler(space, player)
            chance_handler(space, player)
            utility_handler(space, player)
            railroad_handler(space, player)
            parking_handler(space, player)
            jail_handler_go_to(space, player)
            jail_handler_just_visiting(space, player)
            go_handler(space, player)
