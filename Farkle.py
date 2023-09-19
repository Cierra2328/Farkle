import random
from tkinter import *
from tkinter import messagebox



root = Tk()
root.title("Farkle")
mystery_dice = PhotoImage(file = "question mark.png")
count = 0
roll_turns = 0
number_of_dice = 6
roll = [1, 2, 3, 4, 5, 6]
p1points = 0
p2points = 0
turn_point = []
round_points = 0
total = 0
labels = []
turnCheck = 0
numLabels = 0
rolls = []
length = 0
farkleCheck = 0
dice_count = 0
p1Win = 0
p2Win = 0

root.geometry("1300x900")
one = PhotoImage(file = "One.png")
two = PhotoImage(file = "Two.png")
three = PhotoImage(file = "Three.png")
four = PhotoImage(file = "Four.png")
five = PhotoImage(file = "Five.png")
six = PhotoImage(file = "Six.png")
scorecard = PhotoImage(file = "farkle scoring.png")


def points():
    global labels, numLabels, turn_point, length, round_points, total
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0
    total = 0
    points_box.delete(0, END)
    if length <= len(labels):
        for i in range(length, len(labels)):
            if labels[i]["text"] == "1":
                d1 += 1
            elif labels[i]["text"] == "2":
                d2 += 1
            elif labels[i]["text"] == "3":
                d3 += 1
            elif labels[i]["text"] == "4":
                d4 += 1
            elif labels[i]["text"] == "5":
                d5 += 1
            elif labels[i]["text"] == "6":
                d6 += 1
        if straight() == True or pairs() == True or fourPair() == True:
            total += 1500
        elif triplets() == True:
            total += 500
        else:
            if d5 < 3:
                total += d5*50
            if d1 < 4:
                total += d1*100
            if d2 == 3:
                total += 200
            if d3 == 3:
                total += 300
            if d4 == 3:
                total += 400
            if d5 == 3:
                total += 500
            if d6 == 3:
                total += 600
            if d1 == 4 or d2 == 4 or d3 == 4 or d4 == 4 or d5 == 4 or d6 == 4:
                total += 1000
            elif d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 or d5 == 5 or d6 == 5:
                total += 2000
            elif d1 == 6 or d2 == 6 or d3 == 6 or d4 == 6 or d5 == 6 or d6 == 6:
                total += 3000
        points_box.insert(0, round_points + total)
    else:
        length = 0
        round_points = 0
        points()

def win():
    global p1Win, p2Win
    if p1points >= 10000:
        p1Win += 1
    elif p2points >= 10000:
        p2Win += 1

def straight():
    global roll
    roll_sorted = sorted(roll)
    if roll_sorted == [1, 2, 3, 4, 5, 6] and number_of_dice == 6:
        return True
    else:
        return False
        

def triplets():
    global roll
    x = 0
    if number_of_dice < 5:
        return False
    else:
        for numbers in roll:
            if roll.count(numbers) == 3:
                x += 1
    if x == 6:
        return True
    else:
        return False
    

def fourPair():
    global roll
    x = 0
    y = 0
    if number_of_dice < 5:
        return False
    else:
        for numbers in roll:
            if roll.count(numbers) == 4:
                x += 1
            if roll.count(numbers) == 2:
                y += 1
    if x == 4 and y == 2:
        return True
    else:
        return False

    
def turn():
    global roll_turns, number_of_dice, count, farkleCheck, dice_count
    roll = dice_roll(number_of_dice)
    dice_button1.configure(state = NORMAL)
    dice_button2.configure(state = NORMAL)
    dice_button3.configure(state = NORMAL)
    dice_button4.configure(state = NORMAL)
    dice_button5.configure(state = NORMAL)
    dice_button6.configure(state = NORMAL)
    roll_button.configure(state = DISABLED)
    roll_again.configure(state = NORMAL)
    end_turn.configure(state = NORMAL)
    if straight() == True or pairs() == True or fourPair() == True or triplets() == True:
        x = 1
        dice_count += 1
        for i in roll:
            if i == 1:
                point_label = Label(root, image = one, text = "1")
                point_label.grid(row = roll_turns + 2, column = x + 2)
                labels.append(point_label)
            elif i == 2:
                point_label = Label(root, image = two, text = "2")
                point_label.grid(row = roll_turns + 2, column = x + 2)
                labels.append(point_label)
            elif i == 3:
                point_label = Label(root, image = three, text = "3")
                point_label.grid(row = roll_turns + 2, column = x + 2)
                labels.append(point_label)
            elif i == 4:
                point_label = Label(root, image = four, text = "4")
                point_label.grid(row = roll_turns + 2, column = x + 2)
                labels.append(point_label)
            elif i == 5:
                point_label = Label(root, image = five, text = "5")
                point_label.grid(row = roll_turns + 2, column = x + 2)
                labels.append(point_label)
            elif i == 6:
                point_label = Label(root, image = six, text = "6")
                point_label.grid(row = roll_turns + 2, column = x + 2)
                labels.append(point_label)
            x += 1
        points()
    farkle()
    

def rollCheck():
    global number_of_dice, roll_turns, dice_count
    if dice_count > 0:
        return True
    else:
        messagebox.showerror("Farkle", "You must take at least one dice from the roll")
        return False

def pairs():  ##function to determine if there are 3 pairs
    global roll
    x = 0
    if number_of_dice < 6:
        return False
    else:
        for number in roll:
            if roll.count(number) == 2:
                x += 1
    if x == 6:
        return True
    else:
        return False

    
def farkle():
    global roll, farkleCheck
    x = 0
    if number_of_dice > 1:
        for numbers in roll[0: number_of_dice]:
            if roll[0: number_of_dice].count(numbers) >= 3:
                x += 1
            elif numbers == 1 or numbers == 5:
                x += 1
            elif pairs() == True or triplets() == True or straight() == True or fourPair() == True:
                x += 1
    else:
         for numbers in roll[0: 1]:
            if numbers == 1 or numbers == 5:
                x += 1
            elif pairs() == True or triplets() == True or straight() == True or fourPair() == True:
                x += 1
    if x > 0:
        return False
    else:
        messagebox.showwarning("Farkle", "Looks like you farkled! Your turn will end and you will receive no points.")
        roll_again.configure(state = DISABLED)
        farkleCheck += 1
        return True
    
    

def rollAgain():
    global roll, number_of_dice, roll_turns, count, length, round_points, turn_points, farkleCheck, dice_count
    length = len(labels)
    round_points += total
    if rollCheck() == True:
        dice_count = 0
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
        
        roll_turns += 1
        count = 0
        turn()
        

        
    


def EndTurn():
    global count, roll_turns, labels, rolls, number_of_dice, turn_points, p1points, p2points, turnCheck, farkleCheck, round_points
    for label in labels:
        label.destroy()
    if farkleCheck == 0:
        if turnCheck % 2 == 0:
            p1points += round_points + total
        else:
            p2points += round_points + total
        points_box.delete(0, END)
        p1points_box.delete(0, END)
        p1points_box.insert(0, p1points)
        p2points_box.delete(0, END)
        p2points_box.insert(0, p2points)
        count = 0
        roll_turns = 0
        number_of_dice = 6
        win()
        if p1Win > 0:
            messagebox.showinfo("Farkle", "Player 1 Wins!")
            dice_button1.configure(image = mystery_dice, state = DISABLED)
            dice_button2.configure(image = mystery_dice, state = DISABLED)
            dice_button3.configure(image = mystery_dice, state = DISABLED)
            dice_button4.configure(image = mystery_dice, state = DISABLED)
            dice_button5.configure(image = mystery_dice, state = DISABLED)
            dice_button6.configure(image = mystery_dice, state = DISABLED)
            roll_again.configure(state = DISABLED)
            end_turn.configure(state = DISABLED)
        elif p2Win > 0:
            messagebox.showinfo("Farkle", "Player 2 Wins!")
            dice_button1.configure(image = mystery_dice, state = DISABLED)
            dice_button2.configure(image = mystery_dice, state = DISABLED)
            dice_button3.configure(image = mystery_dice, state = DISABLED)
            dice_button4.configure(image = mystery_dice, state = DISABLED)
            dice_button5.configure(image = mystery_dice, state = DISABLED)
            dice_button6.configure(image = mystery_dice, state = DISABLED)
            roll_again.configure(state = DISABLED)
            end_turn.configure(state = DISABLED)
        else:
            dice_button1.configure(image = mystery_dice, state = DISABLED)
            dice_button2.configure(image = mystery_dice, state = DISABLED)
            dice_button3.configure(image = mystery_dice, state = DISABLED)
            dice_button4.configure(image = mystery_dice, state = DISABLED)
            dice_button5.configure(image = mystery_dice, state = DISABLED)
            dice_button6.configure(image = mystery_dice, state = DISABLED)
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
            turnCheck += 1
            farkleCheck = 0
            round_points = 0
            length = 0
            dice_count = 0
            if turnCheck % 2 == 0:
                turn_label.configure(text = "Player 1's Turn")
                p1points_label.configure(bg = "cyan")
                p2points_label.configure(bg = "light grey")
            else:
                turn_label.configure(text = "Player 2's Turn")
                p2points_label.configure(bg = "cyan")
                p1points_label.configure(bg = "light grey")
    else:
        points_box.delete(0, END)
        p1points_box.delete(0, END)
        p1points_box.insert(0, p1points)
        p2points_box.delete(0, END)
        p2points_box.insert(0, p2points)
        count = 0
        roll_turns = 0
        number_of_dice = 6
        dice_button1.configure(image = mystery_dice, state = DISABLED)
        dice_button2.configure(image = mystery_dice, state = DISABLED)
        dice_button3.configure(image = mystery_dice, state = DISABLED)
        dice_button4.configure(image = mystery_dice, state = DISABLED)
        dice_button5.configure(image = mystery_dice, state = DISABLED)
        dice_button6.configure(image = mystery_dice, state = DISABLED)
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
        turnCheck += 1
        farkleCheck = 0
        round_points = 0
        length = 0
        dice_count = 0
        if turnCheck % 2 == 0:
            turn_label.configure(text = "Player 1's Turn")
            p1points_label.configure(bg = "cyan")
            p2points_label.configure(bg = "light grey")
        else:
            turn_label.configure(text = "Player 2's Turn")
            p2points_label.configure(bg = "cyan")
            p1points_label.configure(bg = "light grey")
    
    
    
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
dice_button1 = Button(root, text = " ", image = mystery_dice, state = DISABLED, command = lambda : keep_dice(dice_button1))
dice_button2 = Button(root, text = " ", image = mystery_dice, state = DISABLED, command = lambda : keep_dice(dice_button2))
dice_button3 = Button(root, text = " ", image = mystery_dice, state = DISABLED, command = lambda : keep_dice(dice_button3))
dice_button4 = Button(root, text = " ", image = mystery_dice, state = DISABLED, command = lambda : keep_dice(dice_button4))
dice_button5 = Button(root, text = " ", image = mystery_dice, state = DISABLED, command = lambda : keep_dice(dice_button5))
dice_button6 = Button(root, text = " ", image = mystery_dice, state = DISABLED, command = lambda : keep_dice(dice_button6))
points_box = Entry(root, width = 10,text = "0   ", font = ('10'))
p1points_box = Entry(root, width = 9, text = " 0 ", font = ('14'))
p2points_box = Entry(root, width = 9, text = "0 ", font = ('14'))
p1points_label = Label(root, text = "Player 1 Points:", font = ('12'), bg = "cyan")
p2points_label = Label(root, text = "Player 2 Points:", font = ('12'), bg = "light grey")
points_box_label = Label(root, text = "Possible Points:", font = ('10'))
turn_label = Label(root, text = "Player 1's Turn", font = ('12'))
scoring_label = Label(root, image = scorecard)

roll_button.grid(row = 2, column = 1, columnspan = 2)
roll_again.grid(row = 3, column = 1, columnspan = 2)
end_turn.grid(row = 4, column = 1, columnspan = 2, sticky = N)
dice_button1.grid(row = 1, column = 1)
dice_button2.grid(row = 1, column = 2)
dice_button3.grid(row = 1, column = 3)
dice_button4.grid(row = 1, column = 4)
dice_button5.grid(row = 1, column = 5)
dice_button6.grid(row = 1, column = 6)
points_box.grid(row = 2, column = 11)
p1points_box.grid(row = 0, column = 3, columnspan = 2)
p1points_label.grid(row = 0, column = 1, columnspan = 2)
p2points_box.grid(row = 0, column = 7, columnspan = 3)
p2points_label.grid(row = 0, column = 5, columnspan = 2)
points_box_label.grid(row = 2, column = 10)
turn_label.grid(row = 3, column = 10)
scoring_label.grid(row = 4, rowspan = 4, column = 10, columnspan = 5)


dice = [1, 2, 3, 4, 5, 6]

def keep_dice(button):
    global count, number_of_dice, labels, dice_count
    if button["text"] == "1":
        point_label = Label(root, image = one, text = "1")
        point_label.grid(row = roll_turns + 2, column = count + 3)
        labels.append(point_label)
        count += 1
        number_of_dice -= 1
        button.grid_forget()
    elif button["text"] == "2" and roll.count(2) >= 3:
        point_label = Label(root, image = two, text = "2")
        point_label.grid(row = roll_turns + 2, column = count + 3)
        labels.append(point_label)
        count += 1
        number_of_dice -= 1
        button.grid_forget()
    elif button["text"] == "3" and roll.count(3) >= 3:
        point_label = Label(root, image = three, text = "3")
        point_label.grid(row = roll_turns + 2, column = count + 3)
        labels.append(point_label)
        count += 1
        number_of_dice -= 1
        button.grid_forget()
    elif button["text"] == "4" and roll.count(4) >= 3:
        point_label = Label(root, image = four, text = "4")
        point_label.grid(row = roll_turns + 2, column = count + 3)
        labels.append(point_label)
        count += 1
        number_of_dice -= 1
        button.grid_forget()
    elif button["text"] == "5":
        point_label = Label(root, image = five, text = "5")
        point_label.grid(row = roll_turns + 2, column = count + 3)
        labels.append(point_label)
        count += 1
        number_of_dice -= 1
        button.grid_forget()
    elif button["text"] == "6" and roll.count(6) >= 3:
        point_label = Label(root, image = six, text = "6")
        point_label.grid(row = roll_turns + 2, column = count + 3)
        labels.append(point_label)
        count += 1
        number_of_dice -= 1
        button.grid_forget()
    else:
        messagebox.showerror("Farkle", "You can only choose 1 or 5 unless the number has a count of greater than 2")
    points()
    dice_count += 1
    


