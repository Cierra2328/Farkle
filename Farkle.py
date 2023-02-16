import random

class dice:
    dice = [1, 2, 3, 4, 5, 6]

    def dice_roll(number_of_dice):
        for rolls in range(number_of_dice):
            roll[rolls] = random.randint(dice)
        
