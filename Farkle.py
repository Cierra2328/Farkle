import random
import time
from tkinter import *
from tkinter import messagebox


####Not working
### When keep_dice function runs, it has errors, keeps repeating error, button shows up 3 times, still need
###to add point system, lots of work to do


root = Tk()
root.title("Farkle")
mystery_dice = PhotoImage(file = "MysteryDice.png")
count = 0
roll_turns = 0
number_of_dice = 6
roll = [1, 1, 1, 1, 1, 1]
p1points = 0
p2points = 0
points = []
pair_numbers = []
turnCheck = 0
one = PhotoImage(file = "One.png")
two = PhotoImage(file = "Two.png")
three = PhotoImage(file = "Three.png")
four = PhotoImage(file = "Four.png")
five = PhotoImage(file = "Five.png")
six = PhotoImage(file = "Six.png")

def turn():
    global roll_turns, number_of_dice
    roll = dice_roll(number_of_dice)
    roll_button.configure(state = DISABLED)
    roll_turns += 1
    roll_again.configure(state = NORMAL)
    end_turn.configure(state = NORMAL)
    pair = pairs()
    if pair == True:
        dice_button.grid_forget()
        dice_button2.grid_forget()
        dice_button3.grid_forget()
        dice_button4.grid_forget()
        dice_button5.grid_forget()
        dice_button6.grid_forget()
        if turnCheck % 2 == 0:
            p1points += 1500
        else:
            p2points += 1500
        for number in pair_numbers:
            if number == 1:
                point_label = Label(root, image = one)
                point_label2 = Label(root, image = one)
                if count == 0:
                    point_label.grid(row = 2, column = 3)
                    point_label2.grid(row = 2, column = 4)
                    count += 2
                elif count == 2:
                    point_label.grid(row = 2, column = 5)
                    point_label2.grid(row = 2, column = 6)
                    count += 2
                elif count == 4:
                    point_label.grid(row = 2, column = 7)
                    point_label2.grid(row = 2, column = 8)
                    count = 0
            elif number == 2:
                point_label = Label(root, image = two)
                point_label2 = Label(root, image = two)
                if count == 0:
                    point_label.grid(row = 2, column = 3)
                    point_label2.grid(row = 2, column = 4)
                    count += 2
                elif count == 2:
                    point_label.grid(row = 2, column = 5)
                    point_label2.grid(row = 2, column = 6)
                    count += 2
                elif count == 4:
                    point_label.grid(row = 2, column = 7)
                    point_label2.grid(row = 2, column = 8)
                    count = 0
            elif number == 3:
                point_label = Label(root, image = three)
                point_label2 = Label(root, image = three)
                if count == 0:
                    point_label.grid(row = 2, column = 3)
                    point_label2.grid(row = 2, column = 4)
                    count += 2
                elif count == 2:
                    point_label.grid(row = 2, column = 5)
                    point_label2.grid(row = 2, column = 6)
                    count += 2
                elif count == 4:
                    point_label.grid(row = 2, column = 7)
                    point_label2.grid(row = 2, column = 8)
                    count = 0
            elif number == 4:
                point_label = Label(root, image = four)
                point_label2 = Label(root, image = four)
                if count == 0:
                    point_label.grid(row = 2, column = 3)
                    point_label2.grid(row = 2, column = 4)
                    count += 2
                elif count == 2:
                    point_label.grid(row = 2, column = 5)
                    point_label2.grid(row = 2, column = 6)
                    count += 2
                elif count == 4:
                    point_label.grid(row = 2, column = 7)
                    point_label2.grid(row = 2, column = 8)
                    count = 0
            elif number == 5:
                point_label = Label(root, image = five)
                point_label2 = Label(root, image = five)
                if count == 0:
                    point_label.grid(row = 2, column = 3)
                    point_label2.grid(row = 2, column = 4)
                    count += 2
                elif count == 2:
                    point_label.grid(row = 2, column = 5)
                    point_label2.grid(row = 2, column = 6)
                    count += 2
                elif count == 4:
                    point_label.grid(row = 2, column = 7)
                    point_label2.grid(row = 2, column = 8)
                    count = 0
            elif number == 6:
                point_label = Label(root, image = six)
                point_label2 = Label(root, image = six)
                if count == 0:
                    point_label.grid(row = 2, column = 3)
                    point_label2.grid(row = 2, column = 4)
                    count += 2
                elif count == 2:
                    point_label.grid(row = 2, column = 5)
                    point_label2.grid(row = 2, column = 6)
                    count += 2
                elif count == 4:
                    point_label.grid(row = 2, column = 7)
                    point_label2.grid(row = 2, column = 8)
                    count = 0
        
        ####end of three pairs
                    

def pairs():  ##function to determine if there are 3 pairs
    global roll, pair_numbers
    x = 0
    for number in roll:
        if roll.count(number) == 2:
            x += 1
            pair_numbers.append(number)
    if x > 2:
        return True
    else:
        return False

def addPoints(label):
    pass
    
def farkle():
    pass

def rollAgain():
    pass

def keep_dice(button):
    global count, number_of_dice 
    if button["text"] == "1" and count == 0:
        point_label = Label(root, image = one, text = "1")
        point_label.grid(row = 3, column = 3)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
        point_label = Label(root, image = two, text = "2")
        point_label.grid(row = 3, column = 3)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
        point_label = Label(root, image = three, text = "3")
        point_label.grid(row = 3, column = 3)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
        point_label = Label(root, image = four, text = "4")
        point_label.grid(row = 3, column = 3)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "5" and count == 0 and roll.count(5) >= 3:
        point_label = Label(root, image = five, text = "5")
        point_label.grid(row = 3, column = 3)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
        point_label = Label(root, image = six, text = "6")
        point_label.grid(row = 3, column = 3)
        count += 1
        number_of_dice -= 1
    else:
        messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
        exit
                             
    if button["text"] == "1" and count == 1:
        point_label2 = Label(root, image = one, text = "1")
        point_label2.grid(row = 2, column = 4)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
        point_label2 = Label(root, image = two, text = "2")
        point_label2.grid(row = 2, column = 4)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
        point_label2 = Label(root, image = three, text = "3")
        point_label2.grid(row = 2, column = 4)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
        point_label2 = Label(root, image = four, text = "4")
        point_label2.grid(row = 2, column = 4)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "5" and count == 1:
        point_label2 = Label(root, image = five, text = "5")
        point_label2.grid(row = 2, column = 4)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
        point_label2 = Label(root, image = six, text = "6")
        point_label2.grid(row = 2, column = 4)
        count += 1
        number_of_dice -= 1
    else:
        messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")

    if button["text"] == "1" and count == 2:
        point_label3 = Label(root, image = one, text = "1")
        point_label3.grid(row = 2, column = 5)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
        point_label3 = Label(root, image = two, text = "2")
        point_label3.grid(row = 2, column = 5)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
        point_label2 = Label(root, image = three, text = "3")
        point_label.grid(row = 2, column = 5)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
        point_label2 = Label(root, image = four, text = "4")
        point_label.grid(row = 2, column = 5)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "5" and count == 2 and roll.count(5) >= 3:
        point_label2 = Label(root, image = five, text = "5")
        point_label.grid(row = 2, column = 5)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
        point_label2 = Label(root, image = six, text = "6")
        point_label.grid(row = 2, column = 5)
        count += 1
        number_of_dice -= 1
    else:
        messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")

    if button["text"] == "1" and count == 3:
        point_label2 = Label(root, image = one, text = "1")
        point_label.grid(row = 2, column = 6)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
        point_label2 = Label(root, image = two, text = "2")
        point_label.grid(row = 2, column = 6)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
        point_label2 = Label(root, image = three, text = "3")
        point_label.grid(row = 2, column = 6)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
        point_label2 = Label(root, image = four, text = "4")
        point_label.grid(row = 2, column = 6)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "5" and count == 3 and roll.count(5) >= 3:
        point_label2 = Label(root, image = five, text = "5")
        point_label.grid(row = 2, column = 6)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
        point_label2 = Label(root, image = six, text = "6")
        point_label.grid(row = 2, column = 6)
        count += 1
        number_of_dice -= 1
    else:
        messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")

    if button["text"] == "1" and count == 4:
        point_label2 = Label(root, image = one, text = "1")
        point_label.grid(row = 2, column = 7)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
        point_label2 = Label(root, image = two, text = "2")
        point_label.grid(row = 2, column = 7)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
        point_label2 = Label(root, image = three, text = "3")
        point_label.grid(row = 2, column = 7)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
        point_label2 = Label(root, image = four, text = "4")
        point_label.grid(row = 2, column = 7)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "5" and count == 4 and roll.count(5) >= 3:
        point_label2 = Label(root, image = five, text = "5")
        point_label.grid(row = 2, column = 7)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
        point_label2 = Label(root, image = six, text = "6")
        point_label.grid(row = 2, column = 7)
        count += 1
        number_of_dice -= 1
    else:
        messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")

    if button["text"] == "1" and count == 5:
        point_label2 = Label(root, image = one, text = "1")
        point_label.grid(row = 2, column = 8)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
        point_label2 = Label(root, image = two, text = "2")
        point_label.grid(row = 2, column = 8)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
        point_label2 = Label(root, image = three, text = "3")
        point_label.grid(row = 2, column = 8)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
        point_label2 = Label(root, image = four, text = "4")
        point_label.grid(row = 2, column = 8)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "5" and count == 5 and roll.count(5) >= 3:
        point_label2 = Label(root, image = five, text = "5")
        point_label.grid(row = 2, column = 8)
        count += 1
        number_of_dice -= 1
    elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
        point_label2 = Label(root, image = six, text = "6")
        point_label.grid(row = 2, column = 8)
        count += 1
        number_of_dice -= 1
    else:
        messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
    
########end of normal roll
    

    
def EndTurn():
    global count, roll_turns
    count = 0
    roll_turns = 0

def dice_roll(number_of_dice):
    for rolls in range(number_of_dice):
        roll[rolls] = random.randint(1, 6)
        change_images()
    return roll

def change_images():
    for number in roll:
        if roll[0] == 1:
            dice_button.configure(image = one)
            dice_button.configure(text = "1")
        elif roll[0] == 2:
            dice_button.configure(image = two)
            dice_button.configure(text = "2")
        elif roll[0] == 3:
            dice_button.configure(image = three)
            dice_button.configure(text = "3")
        elif roll[0] == 4:
            dice_button.configure(image = four)
            dice_button.configure(text = "4")
        elif roll[0] == 5:
            dice_button.configure(image = five)
            dice_button.configure(text = "5")
        elif roll[0] == 6:
            dice_button.configure(image = six)
            dice_button.configure(text = "6")
        if roll[1] == 1:
            dice_button2.configure(image = one)
            dice_button2.configure(text = "1")
        elif roll[1] == 2:
            dice_button2.configure(image = two)
            dice_button2.configure(text = "2")
        elif roll[1] == 3:
            dice_button2.configure(image = three)
            dice_button2.configure(text = "3")
        elif roll[1] == 4:
            dice_button2.configure(image = four)
            dice_button2.configure(text = "4")
        elif roll[1] == 5:
            dice_button2.configure(image = five)
            dice_button2.configure(text = "5")
        elif roll[1] == 6:
            dice_button2.configure(image = six)
            dice_button2.configure(text = "6")
        if roll[2] == 1:
            dice_button3.configure(image = one)
            dice_button3.configure(text = "1")
        elif roll[2] == 2:
            dice_button3.configure(image = two)
            dice_button3.configure(text = "2")
        elif roll[2] == 3:
            dice_button3.configure(image = three)
            dice_button3.configure(text = "3")
        elif roll[2] == 4:
            dice_button3.configure(image = four)
            dice_button3.configure(text = "4")
        elif roll[2] == 5:
            dice_button3.configure(image = five)
            dice_button3.configure(text = "5")
        elif roll[2] == 6:
            dice_button3.configure(image = six)
            dice_button3.configure(text = "6")
        if roll[3] == 1:
            dice_button4.configure(image = one)
            dice_button4.configure(text = "1")
        elif roll[3] == 2:
            dice_button4.configure(image = two)
            dice_button4.configure(text = "2")
        elif roll[3] == 3:
            dice_button4.configure(image = three)
            dice_button4.configure(text = "3")
        elif roll[3] == 4:
            dice_button4.configure(image = four)
            dice_button4.configure(text = "4")
        elif roll[3] == 5:
            dice_button4.configure(image = five)
            dice_button4.configure(text = "5")
        elif roll[3] == 6:
            dice_button4.configure(image = six)
            dice_button4.configure(text = "6")
        if roll[4] == 1:
            dice_button5.configure(image = one)
            dice_button5.configure(text = "1")
        elif roll[4] == 2:
            dice_button5.configure(image = two)
            dice_button5.configure(text = "2")
        elif roll[4] == 3:
            dice_button5.configure(image = three)
            dice_button5.configure(text = "3")
        elif roll[4] == 4:
            dice_button5.configure(image = four)
            dice_button5.configure(text = "4")
        elif roll[4] == 5:
            dice_button5.configure(image = five)
            dice_button5.configure(text = "5")
        elif roll[4] == 6:
            dice_button5.configure(image = six)
            dice_button5.configure(text = "6")
        if roll[5] == 1:
            dice_button6.configure(image = one)
            dice_button6.configure(text = "1")
        elif roll[5] == 2:
            dice_button6.configure(image = two)
            dice_button6.configure(text = "2")
        elif roll[5] == 3:
            dice_button6.configure(image = three)
            dice_button6.configure(text = "3")
        elif roll[5] == 4:
            dice_button6.configure(image = four)
            dice_button6.configure(text = "4")
        elif roll[5] == 5:
            dice_button6.configure(image = five)
            dice_button6.configure(text = "5")
        elif roll[5] == 6:
            dice_button6.configure(image = six)
            dice_button6.configure(text = "6")

roll_button = Button(root, height = 5, width = 20, text = "Roll", command = lambda : turn())
end_turn = Button(root, height = 5, width = 20, text = "End Turn", state = DISABLED, command = lambda : EndTurn())
roll_again = Button(root, height = 5, width = 20, text = "Roll Remaining Dice",  state = DISABLED, command = lambda : rollAgain())
dice_button = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button))
dice_button2 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button2))
dice_button3 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button3))
dice_button4 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button4))
dice_button5 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button5))
dice_button6 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button6))

roll_button.grid(row = 2, column = 1, columnspan = 2)
roll_again.grid(row = 3, column = 1, columnspan = 2)
end_turn.grid(row = 4, column = 1, columnspan = 2)
dice_button.grid(row = 1, column = 1)
dice_button2.grid(row = 1, column = 2)
dice_button3.grid(row = 1, column = 3)
dice_button4.grid(row = 1, column = 4)
dice_button5.grid(row = 1, column = 5)
dice_button6.grid(row = 1, column = 6)
dice = [1, 2, 3, 4, 5, 6]


            




    
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


