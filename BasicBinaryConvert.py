from tkinter import *

#Root Window Setup
rootWindow = Tk()
rootWindow.title("Basic Binary Converter")
rootWindow.iconbitmap("HarryICON1.ico")

#Functions
def toBinary():
    
    entry = inputBox.get()

    if entry.isnumeric():

        entryInt = int(entry)

        entryBinary = bin(entryInt)

        resultLabel.config(text=str(entryBinary))


def toDecimal():
    
    entry = inputBox.get()

    entryIsBinary = True

    for eachDigit in entry:

        if eachDigit != "0" and eachDigit != "1":

            entryIsBinary = False

    if entryIsBinary:

        entryInt = int(entry,2)

        resultLabel.config(text=str(entryInt))

#Object Creation
inputBox = Entry(rootWindow, width=50)
toBinaryButton = Button(rootWindow,text= "Convert to Binary", command=toBinary)
toDecimalButton = Button(rootWindow,text= "Convert to Decimal", command=toDecimal)
resultFrame = LabelFrame(rootWindow, padx=5, pady=5, text="Result", labelanchor= N)
resultLabel = Label(resultFrame,text="")

#Object Display
inputBox.grid(row=0,column=0,columnspan=2,padx=10, pady=5)
toBinaryButton.grid(row=1,column=0, pady=5)
toDecimalButton.grid(row=1,column=1, pady=5)

resultFrame.grid(row=2,column=0,columnspan=2,sticky=W+E, padx=10, pady=10)
resultLabel.pack()


rootWindow.mainloop()