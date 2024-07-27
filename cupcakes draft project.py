"""
Author: Jade Mahoney
Date: 7/26/2024
Assignemnt: Module 08 Final Project 
This program is a GUI program that will display a cupcake ordering system for the user to input how many dozen of each flavor of cupcake they want. After the user is finished ordering and they click check out so they can see the total price for the cupcakes they ordered. 
"""
from tkinter import * # This line will take the all the built in function from tkinter and allow this program to use them.
from tkinter import messagebox # This line takes the built in messagebox function from tkinter.
from tkinter import PhotoImage # This line will take the build in photoimage function from tkinter.
from PIL import Image, ImageTk # This line takes the image function from PIL.
root = Tk() # Purpose of the root variable is to create a window.
root.title("Cupcake Ordering") # This line titles the window.
root.geometry("700x700") # This line is how big the window will be when the program is opened.

myWelcomeLabel = Label(root, text = "Welcome to this Cupcake Ordering Servies") # Purpose of the myWelcomeLabel variable is to hold the value of the welcome text.  
myWelcomeLabel.grid(row = 1, column = 0) # This line puts the welcome text to be displayed on the screen.

myMenuLabel= Label(root, text = "Menu") # Purpose of the myMenuLabel variable is to hold the value of the menu text.
myMenuLabel.grid (row = 2, column = 0) # This line puts the menu text to be displayed on the screen.

myCupcakeLabelC = Label(root, text = "Chocolate Cupcake $5.00 /per dozen") # Purpose of the myCupcakeLabelC variable is to hold the chocolate cupcake and the price text.
myCupcakeLabelC.grid(row = 3, column = 0) # This line puts the chocolate cupcake and the price for this to be displayed on the screen.

myCupcakeLabelV = Label(root, text = "Vanilla Cupcake $5.00 /per dozen") # Purpose of the myCupcakeLabelV variable is to hold the vanilla cupcake and the price text.
myCupcakeLabelV.grid(row = 4, column = 0) # This line puts the vanilla cupcake and the price for this to be displayed on the screen.
  
myCupcakeLabelS = Label(root, text = "Strawberry Cupcake $7.00 /per dozen") # Purpose of the myCupcakeLabelS variable is to hold the strawberry cupcake and the price text.
myCupcakeLabelS.grid(row = 5, column = 0) # This line puts the strawberry cupcake and the price text to be displayed on the screen.

myCupcakeLabelF = Label(root, text = "Funfetti Cupcake $6.00 /per dozen") # Purpose of the myCupcakeLabelF variable is to hold the funfetti cupcake and the price text.
myCupcakeLabelF.grid(row = 6, column = 0) # This line puts the funfetti cupcake and the price for this to be displayed on the screen.

myStartLabel= Label(root, text = "Start you order below:") # Purpose of the myStartLabel variable is to hold the value of the start order text.
myStartLabel.grid (row = 7, column = 0, sticky = W) # This line puts the start order text to be displayed on the screen.

itemChocolateCUP = Label(root, text = "Chocolate Cupcake") # Purpose of the itemChocolateCUP variable is to hold the text chocolate cupcake for the ordering section.
itemChocolateCUP.grid(row = 8, column = 0, sticky = W) # This line puts the chocolate cupcake text to be displayed on the screen.

quantityChocolateCUP = Entry(root, width = 5) # Purpose of the quantityChocolateCUP variable is to hold the entry box for the quanity of chocolate cupcake for the ordering section.
quantityChocolateCUP.grid(row = 8, column = 1) # This line puts the enrty box to be displayed on the screen for the chocolate cupcakes.

itemVanillaCUP = Label(root, text = "Vanilla Cupcake") # Purpose of the itemVanillaCUP variable is to hold the text vanilla cupcake for the ordering section.
itemVanillaCUP.grid(row = 9, column = 0, sticky = W) # This line puts the vanilla cupcake text to be displayed on the screen.

quantityVanillaCUP = Entry(root, width = 5) # Purpose of the quantityVanillaCUP variable is to hold the entry box for the quanity of vanilla cupcake for the ordering section.
quantityVanillaCUP.grid(row = 9, column = 1) # This line puts the enrty box to be displayed on the screen for the vanilla cupcakes.

itemStrawberryCUP = Label(root, text = "Strawberry Cupcake") # Purpose of the itemStrawberryCUP variable is to hold the text strawberry cupcake for the ordering section.
itemStrawberryCUP.grid(row = 10, column = 0,sticky = W) # This line puts the strawberry cupcake text to be displayed on the screen.

quantityStrawberryCUP = Entry(root, width = 5) # Purpose of the quantityStrawberryCUP variable is hold the entry box for the quanity of strawberry cupcake for the ordering section.
quantityStrawberryCUP.grid(row = 10, column = 1) # This line puts the enrty box to be displayed on the screen for the strawberry cupcakes.

itemFunfettiCUP = Label(root, text = "Funfetti Cupcake") # Purpose of the itemFunfettiCUP variable is to hold the text funfetti cupcake for the ordering section.
itemFunfettiCUP.grid(row = 11, column = 0,sticky = W) # This line puts the funfetti cupcake text to be displayed on the screen.

quantityFunfettiCUP = Entry(root, width = 5) # Purpose of the quantityFunfettiCUP variable is hold the entry box for the quanity of funfetti cupcake for the ordering section.
quantityFunfettiCUP.grid(row = 11, column = 1) # This line puts the enrty box to be displayed on the screen for the funfetti cupcakes.

photoCupVanilla = PhotoImage(file = "vanillacupcake.png") # Purpose of the photoCupVanilla variable is to hold the image file of the vanilla cupcake.
myphotoCupVanilla = Label(root, text = "Photo of a vanilla cupcake with rainbow sprinkles", image = photoCupVanilla) # Purpose of the myphotoCupVanilla variable is to hold the alternative text for the photo and the varible that holds the photo as well.
myphotoCupVanilla.grid(row = 17, column = 0) # This line diplays the image of the vanilla cupcake on the screen.

myphotoCupVanillaLable = Label(root, text = "Photo of a vanilla cupcake with rainbow sprinkles") # Purpose of the myphotoCupVanillaLable variable is to hold the alternative text for the image above of vanilla cupcake.
myphotoCupVanillaLable.grid(row = 18, column = 0) # This line displays the alternative text for the vanilla cupcake.

photoCupChocolate = PhotoImage(file = "chocolatecupcake.png") # Purpose of the photoCupChocolate variable is to hold the image file of the chocolate cupcake.
myphotoCupChocolate = Label(root, text = "Photo of a chocolate cupcake with rainbow sprinkles", image = photoCupChocolate) # Purpose of the myphotoCupChocolate variable is to hold the alternative text for the photo and the varible that holds the photo as well.
myphotoCupChocolate.grid(row = 17, column = 3) # This line diplays the image of the chocolate cupcake on the screen.

myphotoCupChocolateLable = Label(root, text = "Photo of a chocolate cupcake with rainbow sprinkles") # Purpose of the myphotoCupChocolateLable variable is hold the alternative text for the image above of chocolate cupcake.
myphotoCupChocolateLable.grid(row = 18, column = 3) # This line displays the alternative text for the vanilla cupcake.

"""This modules purpose is to take the input that the user entered into the enrty boxes and use thoes vlaues to show the user on another window and the price it is going to cost for their order."""
def checkOut():
    window2 = Toplevel() # Purpose of the window2 variable is to open a secound window.
    window2.title("Order Recipt") # This line titles the window.
    window2.geometry("200x200") # This line makes the window a certain size.

    totalBill = StringVar() # Purpose of the totalBill variable is to calculate the bill as a string varible.

    try: chocolateCup = int(quantityChocolateCUP.get()) # Purpose of the chocolateCup variable is to get the input that the user put in for the chocolate cupcake category.
    except: chocolateCup = 0 # Purpose of the chocolateCup variable is to set the entry to zero if no interger input is given.

    try: vanillaCup = int(quantityVanillaCUP.get()) # Purpose of the vanillaCup variable is to get the input that the user put in for the vanilla cupcake category.
    except: vanillaCup = 0 # Purpose of the vanillaCup is to set the entry to zero if no interger input is given.

    try: strawberryCup = int(quantityStrawberryCUP.get()) # Purpose of the strawberryCup variable is to get the input that the user put in for the strawberry cupcake category.
    except: strawberryCup = 0 # Purpose of the strawberryCup variable is to set the entry to zero if no interger input is given.

    try: funfettiCup = int(quantityFunfettiCUP.get()) # Purpose of the funfettiCup variable is to get the input that the user put in for the funfetti cupcake category.
    except: funfettiCup = 0 # Purpose of the funfettiCup variable is to set the entry to zero if no interger input is given.

    totalChocoCUP = 5 * chocolateCup # Purpose of the totalChocoCUP variable is to hold the price of the chocolate cupcake mutiplied by the interger the user entered.
    totalVanilCUP = 5 * vanillaCup # Purpose of the totalVanilCUP variable is to hold the price of the vanilla cupcake mutiplied by the interger the user entered.
    totalStrawCUP = 7 * strawberryCup # Purpose of the totalStrawCUP variable is to hold the price of the strawberry cupcake mutiplied by the interger the user entered.
    totalFunCUP = 6 * funfettiCup # Purpose of the totalFunCUP variable is to hold the price of the funfetti cupcake mutiplied by the interger the user entered.

    totalLabel = Label(window2, text = "Total Bill") # Purpose of the totalLabel variable is to hold the total text.
    totalLabel.grid(row = 1, column = 0, sticky = W) # This line displays the total text on the screen.

    priceLabel = Label(window2, text = "$") # Purpose of the priceLabel is to hold the dollar sign text.
    priceLabel.grid(row = 2, column = 0, sticky = W) # This line will display the dollar sign on the screen.

    totalEntry = Label(window2,textvariable = totalBill) # Purpose of the totalEntry variable is to hold the text for the total bill.
    totalEntry.grid(row = 2, column = 1) # This line displays what the total bill is.

    totalcost = (totalChocoCUP + totalVanilCUP + totalStrawCUP + totalFunCUP) # Purpose of the totalcost variable is to hold the value of each of the cupcake categories added together.
    stringBill = (totalcost) # Purpose of the stringBill variable is to hold the total cost. 
    totalBill.set(stringBill) # This line sets the total bill as the stringbill varible.

    """This modules purpose is to show an exit button so the user is able to exit the program after getting the recipt"""
    def myExit2():
        quitExit2 = messagebox.askyesno("Cupcake Orderning", "Do you want to quit?") # Purpose of the quitExit2 variable is to hold the text of asking the user if they want to quit and shows a message box with yes or no.
        if quitExit2 > 0: # This line exits the recipt if the user presses yes.
            root.destroy() # This line will completly exit the program.
            return # This line will send the result to the button that called it.

    myExitButton2 = Button(window2, text = "EXIT", command = myExit2 ) # Purpose of the myExitButton2 variable is to hold the button with the exit text that will callback the myExit2 function to run.
    myExitButton2.grid(row = 4, column = 4) # This line displays the exit button on the recipt screen.


myOrderButton = Button(root, text = "Order Now", command = checkOut) # Purpose of the myOrderButton variable is creating the button and holds the text order and callback the checkOut function.
myOrderButton.grid(row = 13, column = 1) # This line displays the order button on the screen.

"""This modules purpose is to reset the vlaues in the entry feild if the user wanted to quickly change the vlaues they entered to put new values into."""
def myReset():
    quantityChocolateCUP.delete(0) # This line deletes what was entered in the entry box for the chocolate cupcakes
    quantityVanillaCUP.delete(0) # This line deletes what was entered in the entry box for vanilla cupcakes
    quantityStrawberryCUP.delete(0) # This line deletes what was entered in the entry box for strawberry cupcakes
    quantityFunfettiCUP.delete(0) # This line deletes what was entered in the entry box for funfetti cupcakes

myResetButton = Button(root, text = "Reset", state = NORMAL, command = myReset) # Purpose of the myResetButton variable is to create the button and the text reset that will callback the myReset function.
myResetButton.grid(row = 13, column = 0) # This line displays the reset button.

"""This modules purpose is to exit the program if the user does not want to order cupcakes and as a way to leave the program."""
def myExit():
    quitExit = messagebox.askyesno("Cupcake Orderning", "Do you want to quit?") # Purpose of the quitExit variable is to hold the text of asking the user if they want to quit and shows a message box with yes or no.
    if quitExit > 0: # This line exits the program if the user presses yes.
        root.destroy() # This line will completly exit the program.
        return # This line will send the result to the button that called it.

myExitButton = Button(root, text = "EXIT", command = myExit ) # Purpose of the myExitButton variable is to hold the button with the exit text that will callback the myExit function to run.
myExitButton.grid(row = 1, column = 5) # This line displays the exit button on the main screen.

root.mainloop() # This line is used to run the program and all the events.
