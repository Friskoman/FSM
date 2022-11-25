import random
import time

has_item = False
holding = False
drop = False
behavior = [0,1,2]
player_nearby = True

class AI_behavior:

    # item_pickup() set Has_item true op het moment dat er een item wordt opgepakt
    def item_pickup():
        has_item = True
        return has_item


    # item_picker() kijkt of de Ai een item heeft zo ja dan wordt een willekeurig een item_type gekozen 
    def item_picker(has_item):
        #parameters:
        # @ has_item : bool
        item_type = [0,1]
        if has_item == True:
            item_type = random.choice(item_type)
            return item_type, has_item
        else:
            pass


    # player_update() blijft elke seconde opnieuw kijken of er een andere speler in de buurt is
    # voor bij de casus is er een 10% kans dat de status van player_nearby verandert
    def player_update(player_nearby):
        #parameters:
        # @ player_nearby : bool
        time.sleep(1)
        randomizer = [1,2,3,4,5,6,7,8,9,10]
        num = random.choice(randomizer)
        if num == 4:
            player_nearby = not player_nearby
        print('player nearby =', player_nearby)
        return player_nearby


    # drop() dropt het item en returns has_item als False
    def drop(has_item,):
        #parameters:
        # @ has_item : bool
        if has_item == True:
            holding = False
            has_item = False
        return has_item


    # blok() heeft 33% kans op het item wat de AI vast heeft te consumeren 
    # als het item wordt geconsumeerd dan wordt has_item gereturned als False
    def blok(has_item, player_nearby):
        #parameters:
        # @ has_item : bool
        if player_nearby == True:
            randomizer = [1,2,3]
            if has_item == True:
                time.sleep(1)
                num = random.choice(randomizer)
                if num == 3:
                    has_item = False
                    print('item is consumed')
        has_item = AI_behavior.drop(has_item)
        return has_item


    # def_item_use() controleert de value player_nearby zo ja dan wordt blok() opgeroepen zo nee wordt drop() opgeroepen
    def def_item_use(has_item):
        #parameters:
        # @ player_nearby : bool
        # @ has_item : bool
        while has_item == True:
            player_nearby = AI_behavior.player_update(player_nearby)
            print('still holding on')
            has_item = AI_behavior.blok(has_item, player_nearby)
            holding = True
        return has_item
        

    # atc_item_use() controleert de value player_nearby zo nee wordt er gewacht zo ja wordt drop() opgeroepen
    def atc_item_use(player_nearby, has_item):
        #parameters:
        # @ player_nearby : bool
        # @ has_item : bool
        while player_nearby == False:
            player_nearby = AI_behavior.player_update(player_nearby)
            holding = True
        has_item_update = AI_behavior.drop(has_item)
        return has_item_update


    # behavior() is het mijn procces hierin worden meeste functie opgeroepen om alle mogelijke handelingen uit te voeren
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