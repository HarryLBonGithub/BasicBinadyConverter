from tkinter import *

#Root Window Setup
rootWindow = Tk()
rootWindow.title("Basic Binary Converter")
rootWindow.iconbitmap("BasicBinaryConverter\HarryICON1.ico")

#Functions
def toBinary():
    return

def toDecimal():
    pass

#Object Creation
inputBox = Entry(rootWindow, width=50)
toBinaryButton = Button(rootWindow,text= "Convert to Binary", command=toBinary)
toDecimalButton = Button(rootWindow,text= "Convert to Binary", command=toDecimal)
resultFrame = LabelFrame(rootWindow, padx=5, pady=5, text="Result", labelanchor= N)
resultLabel = Label(resultFrame,text="")

#Object Display
inputBox.grid(row=0,column=0,columnspan=2,padx=10, pady=5)
toBinaryButton.grid(row=1,column=0, pady=5)
toDecimalButton.grid(row=1,column=1, pady=5)

resultFrame.grid(row=2,column=0,columnspan=2,sticky=W+E, padx=10, pady=10)
resultLabel.pack()


rootWindow.mainloop()