from tkinter import *
from tkinter import messagebox

#Root Window Setup
rootWindow = Tk()
rootWindow.title("Basic Binary Converter")
iconInmage = PhotoImage(file="HarryICON1.png")
rootWindow.iconphoto(False, iconInmage)

#Functions
def toBinary():
    
    entry = inputBox.get()

    if entry.isnumeric():

        entryInt = int(entry)

        entryBinary = bin(entryInt)

        resultLabel.config(text=str(entryBinary[2:]))

    else:
        messagebox.showerror(title="BAD INPUT", message="Input must be a positive integer.")

        inputBox.delete(0,END)
        
        resultLabel.config(text="")

def toDecimal():

    entry = inputBox.get()

    entryIsBinary = True

    for eachDigit in entry:

        if eachDigit != "0" and eachDigit != "1":

            entryIsBinary = False

    if entryIsBinary:

        entryInt = int(entry,2)

        resultLabel.config(text=str(entryInt))
    
    else:
        messagebox.showerror(title="BAD INPUT", message="Input must be only 1s and 0s.")

        inputBox.delete(0,END)

        resultLabel.config(text="")

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