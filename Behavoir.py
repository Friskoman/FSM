import random
import time

has_item = False
holding = False
drop = False
behavior = [0,1,2]
player_nearby = True

class AI_behavior:


    def item_pickup():
        has_item = True
        return has_item


    def item_picker(has_item):
        item_type = [0,1]
        if has_item == True:
            item_type = random.choice(item_type)
            return item_type, has_item
        else:
            pass


    def player_update(player_nearby):
        time.sleep(1)
        randomizer = [1,2,3,4,5,6,7,8,9,10]
        num = random.choice(randomizer)
        if num == 4:
            player_nearby = not player_nearby
        print('player nearby =', player_nearby)
        return player_nearby


    def drop(has_item):
        if has_item == True:
            holding = False
            has_item = False
        return has_item


    def blok(has_item):
        randomizer = [1,2,3]
        if has_item == True:
            time.sleep(1)
            num = random.choice(randomizer)
            if num == 3:
                has_item = False
                print('item is consumed')
        return has_item

    def def_item_use(player_nearby, has_item):
        while player_nearby == True and has_item == True:
            player_nearby = AI_behavior.player_update(player_nearby)
            print('still holding on')
            has_item = AI_behavior.blok(has_item)
            holding = True
        has_item_update = AI_behavior.drop(has_item)
        return has_item_update
        


    def atc_item_use(player_nearby, has_item):
        while player_nearby == False:
            player_nearby = AI_behavior.player_update(player_nearby)
            holding = True
        has_item_update = AI_behavior.drop(has_item)
        return has_item_update

        
    def behavior():
        has_item = AI_behavior.item_pickup()
        while has_item == True:
            item_type, has_item = AI_behavior.item_picker(has_item)
            if item_type == 0:
                print('item type is defensive')
                behavior = 1
                has_item = AI_behavior.def_item_use(player_nearby, has_item)
                print("that bitch can't hit me")
            else:
                print('item type is offensive')
                behavior = 2
                has_item = AI_behavior.atc_item_use(player_nearby, has_item)
                print('you shot his ass')
        behavior = 0
        return behavior
        
while True:
    print(AI_behavior.behavior())