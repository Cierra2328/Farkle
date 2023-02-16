import random
import time
from tkinter import *


root = Tk()
root.title("Farkle")
mystery_dice = PhotoImage(file = "MysteryDice.png")
def turn():
    number_of_dice = 6
    roll = dice_roll(number_of_dice)
    print(roll)
    
def keep_dice():
    pass

def dice_roll(number_of_dice):
    for rolls in range(number_of_dice):
        roll[rolls] = random.randint(1, 6)
        change_images()
    return roll

def change_images():
    for number in roll:
        if roll[0] == 1:
            dice_button.configure(image = one)
        elif roll[0] == 2:
            dice_button.configure(image = two)
        elif roll[0] == 3:
            dice_button.configure(image = three)
        elif roll[0] == 4:
            dice_button.configure(image = four)
        elif roll[0] == 5:
            dice_button.configure(image = five)
        elif roll[0] == 6:
            dice_button.configure(image = six)
        if roll[1] == 1:
            dice_button2.configure(image = one)
        elif roll[1] == 2:
            dice_button2.configure(image = two)
        elif roll[1] == 3:
            dice_button2.configure(image = three)
        elif roll[1] == 4:
            dice_button2.configure(image = four)
        elif roll[1] == 5:
            dice_button2.configure(image = five)
        elif roll[1] == 6:
            dice_button2.configure(image = six)
        if roll[2] == 1:
            dice_button3.configure(image = one)
        elif roll[2] == 2:
            dice_button3.configure(image = two)
        elif roll[2] == 3:
            dice_button3.configure(image = three)
        elif roll[2] == 4:
            dice_button3.configure(image = four)
        elif roll[2] == 5:
            dice_button3.configure(image = five)
        elif roll[2] == 6:
            dice_button3.configure(image = six)
        if roll[3] == 1:
            dice_button4.configure(image = one)
        elif roll[3] == 2:
            dice_button4.configure(image = two)
        elif roll[3] == 3:
            dice_button4.configure(image = three)
        elif roll[3] == 4:
            dice_button4.configure(image = four)
        elif roll[3] == 5:
            dice_button4.configure(image = five)
        elif roll[3] == 6:
            dice_button4.configure(image = six)
        if roll[4] == 1:
            dice_button5.configure(image = one)
        elif roll[4] == 2:
            dice_button5.configure(image = two)
        elif roll[4] == 3:
            dice_button5.configure(image = three)
        elif roll[4] == 4:
            dice_button5.configure(image = four)
        elif roll[4] == 5:
            dice_button5.configure(image = five)
        elif roll[4] == 6:
            dice_button5.configure(image = six)
        if roll[5] == 1:
            dice_button6.configure(image = one)
        elif roll[5] == 2:
            dice_button6.configure(image = two)
        elif roll[5] == 3:
            dice_button6.configure(image = three)
        elif roll[5] == 4:
            dice_button6.configure(image = four)
        elif roll[5] == 5:
            dice_button6.configure(image = five)
        elif roll[5] == 6:
            dice_button6.configure(image = six)
roll_button = Button(root, height = 5, width = 20, text = "Roll", command = lambda : turn())
dice_button = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice())
dice_button2 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice())
dice_button3 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice())
dice_button4 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice())
dice_button5 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice())
dice_button6 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice())
roll_button.grid(row = 3, column = 1, columnspan = 2)
dice_button.grid(row = 1, column = 1)
dice_button2.grid(row = 1, column = 2)
dice_button3.grid(row = 1, column = 3)
dice_button4.grid(row = 1, column = 4)
dice_button5.grid(row = 1, column = 5)
dice_button6.grid(row = 1, column = 6)
dice = [1, 2, 3, 4, 5, 6]
roll = [1, 1, 1, 1, 1, 1]
one = PhotoImage(file = "One.png")
two = PhotoImage(file = "Two.png")
three = PhotoImage(file = "Three.png")
four = PhotoImage(file = "Four.png")
five = PhotoImage(file = "Five.png")
six = PhotoImage(file = "Six.png")

            

p1points = 0
p2points = 0

    
points  = {
    1 : 100,
    5 : 50
    }
    
def main():
    print("Welcome to Farkle")
    player1 = input("Please enter your name to get started: ")
    print("Hello, " + player1)
    player2 = input("What is player 2's name? ")
    print("Hello, " + player2)
    print("Player 1 will roll first, you will start with 6 dice")
    print("Rolling...")
    turn()
    print("you must remove at least 1 die")
    print("what die or dice would you like to keep for points?")


