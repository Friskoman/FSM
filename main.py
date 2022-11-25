def menu(input_function, input_type):
    res = None
    while res == None:
        try:
            res = input_type(input_function)
        except:
            print('Invalid input')
    return res




def behavior():
    has_item = menu(input('---------------------------- \n Did you grab a item?  \n---------------------------- \n (y/n):').lower().strip() == 'y', bool)
    while has_item == True:
        item_type = menu(input('---------------------------- \nwhat kind of item do you have?\n----------------------------\n0 = def \n1 = atc \n'), int)
        if item_type == 0:
            behavior = 1
            print('defensive state')
            has_item = def_item_use(has_item)
            print("that bitch can't hit me")
        else:
            behavior = 2
            print('aggressive state')
            has_item = atc_item_use(has_item)
            print('you shot his ass')
    behavior = 0
    return 'neutral state'

    

def player_update(player_nearby):
    player_nearby = menu(input('is there a player nearby? (y/n): ').lower().strip() == 'y', bool)
    return player_nearby


def drop(has_item):
    if has_item == True:
        has_item = False
    return has_item


def blok(has_item): 
    if has_item == True:
        time.sleep(1)
        consumed = menu(input('did you get hit? (y/n): ').lower().strip() == 'y', bool)
        if consumed == True:
            has_item = False
            print('item is consumed')
    return has_item

def def_item_use(has_item):
    player_nearby = menu(input('is there a player nearby? (y/n): ').lower().strip() == 'y', bool)
    while player_nearby == True and has_item == True:
        print('still holding on')
        has_item = blok(has_item)
        player_nearby = player_update(player_nearby)
    has_item_update = drop(has_item)
    return has_item_update
    


def atc_item_use(has_item):
    player_nearby = menu(input('is there a player nearby? (y/n): ').lower().strip() == 'y', bool)
    while player_nearby == False:
        player_nearby = player_update(player_nearby)
    has_item_update = drop(has_item)
    return has_item_update

while True:
    print(behavior())