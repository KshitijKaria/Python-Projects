from tkinter import *

class CurrencyConvertor:
    def __init__(self):
        window = Tk()
        window.title("Currency Convertor")
        window.configure(bg="yellow")

        Label(window,font="Helvetica 12 bold", bg = "yellow",text = "Amount to convert").grid(row=1, column=1,padx =15, sticky = W)
        Label(window,font="Helvetica 12 bold", bg = "yellow",text = "Conversion Rate").grid(row=2, column=1, padx =15,sticky = W)
        Label(window,font="Helvetica 12 bold", bg = "yellow",text = "Converted Amount").grid(row=3, column=1, padx =15,sticky = W)

        self.amounttoConvertVar = StringVar()
        Entry(window,textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row=1,column=2,pady =15)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable = self.conversionRateVar, justify = RIGHT).grid(row=2,column=2,pady=15)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window,font="Helvetica 12 bold", bg = "yellow",textvariable = self.convertedAmountVar).grid(row=3, column=2,padx=15, sticky = E)

        btConvertedAmount = Button(window, text = "Convert",font = "Helvetica 12 bold", bg = "red", fg='white', command = self.ConvertedAmount).grid(row = 4,column = 2, sticky= E)
        btdelete_all = Button(window, text = "Clear",font = "Helvetica 12 bold", bg = "blue", fg='white', command = self.delete_all).grid(row = 4,column = 3,padx= 25,pady=25, sticky= E)

        window.mainloop()

    def ConvertedAmount(self):
        amt = float(self.conversionRateVar.get())
        convertedAmountVar =float(self.amounttoConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, ' 10.2f'))

    def delete_all(self):
        self.amounttoConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")

CurrencyConvertor()
