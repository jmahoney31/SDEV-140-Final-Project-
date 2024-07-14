from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Cupcake Ordering")
root.geometry("400x300")

def myReset():
    quantityChocolateCUP.delete(0)
    quantityVanillaCUP.delete(0)
    quantityStrawberryCUP.delete(0)
    quantityFunfettiCUP.delete(0)

totalBill = StringVar()

myLabel1 = Label(root, text = "Welcome to this Cupcake Ordering Servies")
myLabel1.grid(row= 1, column=0)

myLabel2= Label(root, text = "Menue")
myLabel2.grid (row = 2, column= 0)

myLabel3= Label(root, text = "Start you order below:")
myLabel3.grid (row = 7, column= 0, sticky= W)

myCupcakeLabelC = Label(root, text ="Chocolate Cupcake 5.00 /per dozen")
myCupcakeLabelC.grid(row= 3, column=0)

myCupcakeLabelV = Label(root, text ="Vanilla Cupcake 5.00 /per dozen")
myCupcakeLabelV.grid(row= 4, column=0)

myCupcakeLabelS = Label(root, text ="Strawberry Cupcake 7.00 /per dozen")
myCupcakeLabelS.grid(row= 5, column=0)

myCupcakeLabelF = Label(root, text ="Funfetti Cupcake 6.00 /per dozen")
myCupcakeLabelF.grid(row= 6, column=0)

itemChocolateCUP = Label(root, text="Chocolate Cupcake")
itemChocolateCUP.grid(row= 8, column=0, sticky= W)
quantityChocolateCUP = Entry(root, width=5)
quantityChocolateCUP.grid(row=8, column=1)

itemVanillaCUP = Label(root, text="Vanilla Cupcake")
itemVanillaCUP.grid(row= 9, column=0, sticky= W)
quantityVanillaCUP = Entry(root, width=5)
quantityVanillaCUP.grid(row=9, column=1)

itemStrawberryCUP = Label(root, text="Strawberry Cupcake")
itemStrawberryCUP.grid(row=10, column=0,sticky= W)
quantityStrawberryCUP = Entry(root, width=5)
quantityStrawberryCUP.grid(row=10, column=1)

itemFunfettiCUP = Label(root, text="Funfetti Cupcake")
itemFunfettiCUP.grid(row=11, column=0,sticky= W)
quantityFunfettiCUP = Entry(root, width=5)
quantityFunfettiCUP.grid(row=11, column=1)

myResetButton = Button(root, text = "Reset", state = NORMAL, command= myReset)
myResetButton.grid(row=13, column= 0)

def myExit():
    quitExit = messagebox.askyesno("Cupcake Orderning", "Do you want to quit?")
    if quitExit > 0:
        root.destroy()
        return

myExitButton = Button(root, text= "EXIT", command= myExit)
myExitButton.grid(row=1, column=5)

def checkOut():
    window2 = Toplevel()
    window2.title("Order Recipt")
    window2.geometry("200x200")
    chocolateCup = int(quantityChocolateCUP.get())
    vanillaCup = int(quantityVanillaCUP.get())
    strawberryCup = int(quantityStrawberryCUP.get())
    funfettiCup = int(quantityFunfettiCUP.get())
    totalChocoCUP = 5 * chocolateCup
    totalVanilCUP = 5 * vanillaCup
    totalStrawCUP = 7 * strawberryCup
    totalFunCUP = 6 * funfettiCup
    totalLabel = Label(window2, text = "total")
    totalEntry = Label(window2,textvariable=totalBill)
    totalEntry.grid(row=16, column= 0)
    totalLabel.grid(row = 15, column=0)
    totalcost = (totalChocoCUP + totalVanilCUP + totalStrawCUP + totalFunCUP)
    stringBill = (totalcost)
    totalBill.set(stringBill)

myOrderButton = Button(root, text = "Order Now", command = checkOut)
myOrderButton.grid(row=13, column=1)

root.mainloop()