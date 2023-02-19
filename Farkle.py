import random
from tkinter import *
from tkinter import messagebox



root = Tk()
root.title("Farkle")
mystery_dice = PhotoImage(file = "question mark.png")
count = 0
roll_turns = 0
number_of_dice = 6
roll = [1, 1, 1, 1, 1, 1]
p1points = 0
p2points = 0
turn_point = []
pair_numbers = []
labels = []
turnCheck = 0
numLabels = 0
rolls = []
root.geometry("900x900")
one = PhotoImage(file = "One.png")
two = PhotoImage(file = "Two.png")
three = PhotoImage(file = "Three.png")
four = PhotoImage(file = "Four.png")
five = PhotoImage(file = "Five.png")
six = PhotoImage(file = "Six.png")


def points():
    global labels, numLabels, rolls, turn_point
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0
    total = 0
    turn_point = []
    numLabels += len(labels)
    points_box.delete(0, END)
    for label in labels:
        if label["text"] == "1":
            d1 += 1
        elif label["text"] == "2":
            d2 += 1
        elif label["text"] == "3":
            d3 += 1
        elif label["text"] == "4":
            d4 += 1
        elif label["text"] == "5":
            d5 += 1
        elif label["text"] == "6":
            d6 += 1
    if rolls == 1:
        pairs()
        straight()
        triplets()
        fourPair()
    if d5 < 3:
        turn_point.append(d5*50)
    if d1 < 4:
        turn_point.append(d1*100)
    if d2 == 3:
        if triplets() == False:
            turn_point.append(200)
    if d3 == 3:
        if triplets() == False:
            turn_point.append(300)
    if d4 == 3:
        if triplets() == False:
            turn_point.append(400)
    if d5 == 3:
        if triplets() == False:
            turn_point.append(500)
    if d6 == 3:
        if triplets() == False:
            turn_point.append(600)
    if d1 == 4 or d2 == 4 or d3 == 4 or d5 == 4 or d6 == 4:
        if fourPair() == False:
            turn_point.append(1000)
    elif d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 or d5 == 5 or d6 == 5:
        turn_point.append(2000)
    elif d1 == 6 or d2 == 6 or d3 == 6 or d4 == 6 or d5 == 6 or d6 == 6:
        turn_point.append(3000)

    if straight() == True or pairs() == True or fourPair() == True:
        turn_point.append(1500)
    if triplets() == True:
        turn_point.append(2500)
    for point in turn_point:
        total += point

    points_box.insert(0, total)

def straight():
    return False

def triplets():
    return False
    

def fourPair():
    return False
    


    
def turn():
    global roll_turns, number_of_dice, count
    roll = dice_roll(number_of_dice)
    roll_button.configure(state = DISABLED)
    roll_again.configure(state = NORMAL)
    end_turn.configure(state = NORMAL)
##    pair = pairs()
##    if pair == True:
##        print(roll)
##        dice_button1.grid_forget()
##        dice_button2.grid_forget()
##        dice_button3.grid_forget()
##        dice_button4.grid_forget()
##        dice_button5.grid_forget()
##        dice_button6.grid_forget()
####        if turnCheck % 2 == 0:
##            p1points += 1500
##        else:
##            p2points += 1500
##        for number in pair_numbers:
##            if number == 1:
##                point_label = Label(root, image = one)
##                point_label2 = Label(root, image = one)
##                if count == 0:
##                    point_label.grid(row = 2, column = 3)
##                    point_label2.grid(row = 2, column = 4)
##                    count += 2
##                elif count == 2:
##                    point_label.grid(row = 2, column = 5)
##                    point_label2.grid(row = 2, column = 6)
##                    count += 2
##                elif count == 4:
##                    point_label.grid(row = 2, column = 7)
##                    point_label2.grid(row = 2, column = 8)
##                    count = 0
##            elif number == 2:
##                point_label = Label(root, image = two)
##                point_label2 = Label(root, image = two)
##                if count == 0:
##                    point_label.grid(row = 2, column = 3)
##                    point_label2.grid(row = 2, column = 4)
##                    count += 2
##                elif count == 2:
##                    point_label.grid(row = 2, column = 5)
##                    point_label2.grid(row = 2, column = 6)
##                    count += 2
##                elif count == 4:
##                    point_label.grid(row = 2, column = 7)
##                    point_label2.grid(row = 2, column = 8)
##                    count = 0
##            elif number == 3:
##                point_label = Label(root, image = three)
##                point_label2 = Label(root, image = three)
##                if count == 0:
##                    point_label.grid(row = 2, column = 3)
##                    point_label2.grid(row = 2, column = 4)
##                    count += 2
##                elif count == 2:
##                    point_label.grid(row = 2, column = 5)
##                    point_label2.grid(row = 2, column = 6)
##                    count += 2
##                elif count == 4:
##                    point_label.grid(row = 2, column = 7)
##                    point_label2.grid(row = 2, column = 8)
##                    count = 0
##            elif number == 4:
##                point_label = Label(root, image = four)
##                point_label2 = Label(root, image = four)
##                if count == 0:
##                    point_label.grid(row = 2, column = 3)
##                    point_label2.grid(row = 2, column = 4)
##                    count += 2
##                elif count == 2:
##                    point_label.grid(row = 2, column = 5)
##                    point_label2.grid(row = 2, column = 6)
##                    count += 2
##                elif count == 4:
##                    point_label.grid(row = 2, column = 7)
##                    point_label2.grid(row = 2, column = 8)
##                    count = 0
##            elif number == 5:
##                point_label = Label(root, image = five)
##                point_label2 = Label(root, image = five)
##                if count == 0:
##                    point_label.grid(row = 2, column = 3)
##                    point_label2.grid(row = 2, column = 4)
##                    count += 2
##                elif count == 2:
##                    point_label.grid(row = 2, column = 5)
##                    point_label2.grid(row = 2, column = 6)
##                    count += 2
##                elif count == 4:
##                    point_label.grid(row = 2, column = 7)
##                    point_label2.grid(row = 2, column = 8)
##                    count = 0
##            elif number == 6:
##                point_label = Label(root, image = six)
##                point_label2 = Label(root, image = six)
##                if count == 0:
##                    point_label.grid(row = 2, column = 3)
##                    point_label2.grid(row = 2, column = 4)
##                    count += 2
##                elif count == 2:
##                    point_label.grid(row = 2, column = 5)
##                    point_label2.grid(row = 2, column = 6)
##                    count += 2
##                elif count == 4:
##                    point_label.grid(row = 2, column = 7)
##                    point_label2.grid(row = 2, column = 8)
##                    count = 0
        
        ####end of three pairs
                    

def pairs():  ##function to determine if there are 3 pairs
    pass
##    global roll, pair_numbers
##    x = 0
##    for number in roll:
##        if roll.count(number) == 2:
##            x += 1
##            pair_numbers.append(number)
##    if x > 3:
##        return True
##    else:
##        return False

def addPoints(label):
    pass
    
def farkle():
    pass

def rollAgain():
    global roll, number_of_dice, roll_turns, count
    if number_of_dice == 0:
        number_of_dice = 6
    if number_of_dice == 6:
        dice_button1.grid(row = 1, column = 1)
        dice_button2.grid(row = 1, column = 2)
        dice_button3.grid(row = 1, column = 3)
        dice_button4.grid(row = 1, column = 4)
        dice_button5.grid(row = 1, column = 5)
        dice_button6.grid(row = 1, column = 6)
    elif number_of_dice == 5:
        dice_button1.grid(row = 1, column = 1)
        dice_button2.grid(row = 1, column = 2)
        dice_button3.grid(row = 1, column = 3)
        dice_button4.grid(row = 1, column = 4)
        dice_button5.grid(row = 1, column = 5)
        dice_button6.grid_forget()
    elif number_of_dice == 4:
        dice_button1.grid(row = 1, column = 1)
        dice_button2.grid(row = 1, column = 2)
        dice_button3.grid(row = 1, column = 3)
        dice_button4.grid(row = 1, column = 4)
        dice_button5.grid_forget()
        dice_button6.grid_forget()
    elif number_of_dice == 3:
        dice_button1.grid(row = 1, column = 1)
        dice_button2.grid(row = 1, column = 2)
        dice_button3.grid(row = 1, column = 3)
        dice_button4.grid_forget()
        dice_button5.grid_forget()
        dice_button6.grid_forget()
    elif number_of_dice == 2:
        dice_button1.grid(row = 1, column = 1)
        dice_button2.grid(row = 1, column = 2)
        dice_button3.grid_forget()
        dice_button4.grid_forget()
        dice_button5.grid_forget()
        dice_button6.grid_forget()
    elif number_of_dice == 1:
        dice_button1.grid(row = 1, column = 1)
        dice_button2.grid_forget()
        dice_button3.grid_forget()
        dice_button4.grid_forget()
        dice_button5.grid_forget()
        dice_button6.grid_forget()

    roll = dice_roll(number_of_dice)
    roll_turns += 1
    count = 0
    
    

def keep_dice(button):
    global count, number_of_dice, labels
    if roll_turns == 0:
        if button["text"] == "1" and count == 0:
            point_label = Label(root, image = one, text = "1")
            point_label.grid(row = 2, column = 3)
            labels.append(point_label)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label = Label(root, image = two, text = "2")
            point_label.grid(row = 2, column = 3)
            labels.append(point_label)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label = Label(root, image = three, text = "3")
            point_label.grid(row = 2, column = 3)
            labels.append(point_label)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label = Label(root, image = four, text = "4")
            point_label.grid(row = 2, column = 3)
            labels.append(point_label)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label = Label(root, image = five, text = "5")
            point_label.grid(row = 2, column = 3)
            labels.append(point_label)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label = Label(root, image = six, text = "6")
            point_label.grid(row = 2, column = 3)
            labels.append(point_label)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label2 = Label(root, image = one, text = "1")
            point_label2.grid(row = 2, column = 4)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label2 = Label(root, image = two, text = "2")
            point_label2.grid(row = 2, column = 4)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label2 = Label(root, image = three, text = "3")
            point_label2.grid(row = 2, column = 4)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label2 = Label(root, image = four, text = "4")
            point_label2.grid(row = 2, column = 4)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label2 = Label(root, image = five, text = "5")
            point_label2.grid(row = 2, column = 4)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label2 = Label(root, image = six, text = "6")
            point_label2.grid(row = 2, column = 4)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label3 = Label(root, image = one, text = "1")
            point_label3.grid(row = 2, column = 5)
            labels.append(point_label3)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label3 = Label(root, image = two, text = "2")
            point_label3.grid(row = 2, column = 5)
            labels.append(point_label3)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label2 = Label(root, image = three, text = "3")
            point_label2.grid(row = 2, column = 5)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label2 = Label(root, image = four, text = "4")
            point_label2.grid(row = 2, column = 5)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label = Label(root, image = five, text = "5")
            point_label.grid(row = 2, column = 5)
            labels.append(point_label)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label2 = Label(root, image = six, text = "6")
            point_label2.grid(row = 2, column = 5)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label2 = Label(root, image = one, text = "1")
            point_label2.grid(row = 2, column = 6)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label2 = Label(root, image = two, text = "2")
            point_label2.grid(row = 2, column = 6)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label2 = Label(root, image = three, text = "3")
            point_label2.grid(row = 2, column = 6)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label2 = Label(root, image = four, text = "4")
            point_label2.grid(row = 2, column = 6)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label2 = Label(root, image = five, text = "5")
            point_label2.grid(row = 2, column = 6)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label2 = Label(root, image = six, text = "6")
            point_label2.grid(row = 2, column = 6)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label2 = Label(root, image = one, text = "1")
            point_label2.grid(row = 2, column = 7)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label2 = Label(root, image = two, text = "2")
            point_label2.grid(row = 2, column = 7)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label2 = Label(root, image = three, text = "3")
            point_label2.grid(row = 2, column = 7)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label2 = Label(root, image = four, text = "4")
            point_label2.grid(row = 2, column = 7)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label2 = Label(root, image = five, text = "5")
            point_label2.grid(row = 2, column = 7)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label2 = Label(root, image = six, text = "6")
            point_label2.grid(row = 2, column = 7)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label2 = Label(root, image = one, text = "1")
            point_label2.grid(row = 2, column = 8)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label2 = Label(root, image = two, text = "2")
            point_label2.grid(row = 2, column = 8)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label2 = Label(root, image = three, text = "3")
            point_label2.grid(row = 2, column = 8)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label2 = Label(root, image = four, text = "4")
            point_label2.grid(row = 2, column = 8)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label2 = Label(root, image = five, text = "5")
            point_label2.grid(row = 2, column = 8)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label2 = Label(root, image = six, text = "6")
            point_label2.grid(row = 2, column = 8)
            labels.append(point_label2)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
            #####end of first roll
    elif roll_turns == 1:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 3, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 3, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 3, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 3, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 3, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 3, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 3, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 3, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 3, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 3, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 3, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 3, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 3, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 3, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 3, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 3, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 3, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 3, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 3, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 3, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 3, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 3, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 3, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 3, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 3, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 3, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 3, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 3, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 3, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 3, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 3, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 3, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 3, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 3, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 3, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 3, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
             #####end of second roll
            ####start of third roll
    elif roll_turns == 2:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 4, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 4, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 4, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 4, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 4, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 4, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 4, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 4, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 4, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 4, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 4, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 4, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 4, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 4, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 4, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 4, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 4, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 4, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 4, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 4, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 4, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 4, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 4, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 4, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 4, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 4, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 4, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 4, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 4, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 4, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 4, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 4, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 4, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 4, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 4, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 4, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
            ####end of third roll
    elif roll_turns == 3:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 5, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 5, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 5, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 5, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 5, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 5, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 5, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 5, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 5, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 5, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 5, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 5, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 5, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 5, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 5, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 5, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 5, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 5, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 5, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 5, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 5, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 5, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 5, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 5, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 5, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 5, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 5, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 5, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 5, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 5, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 5, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 5, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 5, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 5, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 5, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 5, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
    ####end of fourth roll
            ###start of fifth roll
    elif roll_turns == 4:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 6, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 6, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 6, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 6, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 6, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 6, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 6, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 6, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 6, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 6, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 6, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 6, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 6, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 6, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 6, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 6, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 6, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 6, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 6, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 6, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 6, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 6, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 6, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 6, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 6, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 6, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 6, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 6, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 6, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 6, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 6, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 6, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 6, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 6, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 6, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 6, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
    ####end of fifth roll
    elif roll_turns == 5:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 7, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 7, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 7, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 7, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 7, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 7, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 7, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 7, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 7, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 7, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 7, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 7, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 7, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 7, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 7, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 7, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 7, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 7, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 7, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 7, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 7, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 7, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 7, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 7, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 7, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 7, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 7, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 7, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 7, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 7, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 7, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 7, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 7, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 7, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 7, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 7, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
            ####end of sixth roll
            ###beginning of seventh roll
    elif roll_turns == 6:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 8, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 8, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 8, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 8, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 8, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 8, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 8, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 8, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 8, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 8, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 8, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 8, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 8, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 8, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 8, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 8, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 8, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 8, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 8, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 8, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 8, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 8, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 8, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 8, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 8, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 8, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 8, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 8, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 8, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 8, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 8, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 8, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 8, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 8, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 8, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 8, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
            ####end of 7th roll
            ###beginning of 8th roll
    elif roll_turns == 7:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 9, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 9, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 9, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 9, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 9, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 9, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 9, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 9, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 9, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 9, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 9, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 9, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 9, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 9, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 9, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 9, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 9, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 9, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 9, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 9, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 9, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 9, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 9, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 9, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 9, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 9, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 9, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 9, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 9, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 9, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 9, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 9, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 9, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 9, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 9, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 9, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
    ###end of eighth roll
            ##beginning of 9th roll
    elif roll_turns == 8:
        if button["text"] == "1" and count == 0:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 10, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 0 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 10, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 0 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 10, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 0 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 10, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 0:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 10, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 0 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 10, column = 3)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 1:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 10, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 1 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 10, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 1 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 10, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 1 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 10, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 1:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 10, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 1 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 10, column = 4)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 2:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 10, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 2 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 10, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 2 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 10, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 2 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 10, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 2:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 10, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 2 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 10, column = 5)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 3:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 10, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 3 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 10, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "3" and count == 3 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 10, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 3 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 10, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 3:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 10, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 3 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 10, column = 6)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 4:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 10, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "2" and count == 4 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 10, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 4 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 10, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 4 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 10, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 4:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 10, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 4 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 10, column = 7)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "1" and count == 5:
            point_label4 = Label(root, image = one, text = "1")
            point_label4.grid(row = 10, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
        elif button["text"] == "2" and count == 5 and roll.count(2) >= 3:
            point_label4 = Label(root, image = two, text = "2")
            point_label4.grid(row = 10, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "3" and count == 5 and roll.count(3) >= 3:
            point_label4 = Label(root, image = three, text = "3")
            point_label4.grid(row = 10, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "4" and count == 5 and roll.count(4) >= 3:
            point_label4 = Label(root, image = four, text = "4")
            point_label4.grid(row = 10, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "5" and count == 5:
            point_label4 = Label(root, image = five, text = "5")
            point_label4.grid(row = 10, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        elif button["text"] == "6" and count == 5 and roll.count(6) >= 3:
            point_label4 = Label(root, image = six, text = "6")
            point_label4.grid(row = 10, column = 8)
            labels.append(point_label4)
            count += 1
            number_of_dice -= 1
            button.grid_forget()
        else:
            messagebox.showerror("Farkle", "Remember the point system. You can only keep dice of numbers 1 and 5, unless the number has more than 2 of a kind")
    ####end of ninth roll
    points()

def EndTurn():
    global count, roll_turns, labels, rolls, number_of_dice
    for label in labels:
        label.destroy()
    count = 0
    roll_turns = 0
    number_of_dice = 6
    dice_button1.configure(image = mystery_dice)
    dice_button2.configure(image = mystery_dice)
    dice_button3.configure(image = mystery_dice)
    dice_button4.configure(image = mystery_dice)
    dice_button5.configure(image = mystery_dice)
    dice_button6.configure(image = mystery_dice)
    dice_button1.grid(row = 1, column = 1)
    dice_button2.grid(row = 1, column = 2)
    dice_button3.grid(row = 1, column = 3)
    dice_button4.grid(row = 1, column = 4)
    dice_button5.grid(row = 1, column = 5)
    dice_button6.grid(row = 1, column = 6)
    roll_button.configure(state = NORMAL)
    roll_again.configure(state = DISABLED)
    end_turn.configure(state = DISABLED)
    rolls = []
    labels = []
    
    
def dice_roll(number):
    for rolls in range(number):
        roll[rolls] = random.randint(1, 6)
        change_images()
    return roll

def change_images():
    for number in roll:
        if roll[0] == 1:
            dice_button1.configure(image = one)
            dice_button1.configure(text = "1")
        elif roll[0] == 2:
            dice_button1.configure(image = two)
            dice_button1.configure(text = "2")
        elif roll[0] == 3:
            dice_button1.configure(image = three)
            dice_button1.configure(text = "3")
        elif roll[0] == 4:
            dice_button1.configure(image = four)
            dice_button1.configure(text = "4")
        elif roll[0] == 5:
            dice_button1.configure(image = five)
            dice_button1.configure(text = "5")
        elif roll[0] == 6:
            dice_button1.configure(image = six)
            dice_button1.configure(text = "6")
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
dice_button1 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button1))
dice_button2 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button2))
dice_button3 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button3))
dice_button4 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button4))
dice_button5 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button5))
dice_button6 = Button(root, text = " ", image = mystery_dice, command = lambda : keep_dice(dice_button6))
points_box = Entry(root, width = 20,text = " ")

roll_button.grid(row = 2, column = 1, columnspan = 2)
roll_again.grid(row = 3, column = 1, columnspan = 2)
end_turn.grid(row = 4, column = 1, columnspan = 2)
dice_button1.grid(row = 1, column = 1)
dice_button2.grid(row = 1, column = 2)
dice_button3.grid(row = 1, column = 3)
dice_button4.grid(row = 1, column = 4)
dice_button5.grid(row = 1, column = 5)
dice_button6.grid(row = 1, column = 6)
points_box.grid(row = 2, column = 10)

dice = [1, 2, 3, 4, 5, 6]



