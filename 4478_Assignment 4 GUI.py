# Author: Ethan Dang
# Date created: 12/04/2022
# Date last changed: 21/04/2022
# This GUI program helps user to compare and pick the bank with the highest final balance
# Inputs: interest rates from three banks, compounded periods from three banks, and deposited amount


from tkinter import *

window = Tk()
window.title("Final Balance Calculator")
window.geometry("430x278")
window.configure(background="white smoke")


# Function for calculating final balance
def Calculation():
    # Taking input
    P = int(depositedAmount.get())
    r_1 = float(entR1.get())
    m_1 = float(entM1.get())
    r_2 = float(entR2.get())
    m_2 = float(entM2.get())
    r_3 = float(entR3.get())
    m_3 = float(entM3.get())

    # Divide interest rates by 100
    r1 = r_1 / 100 
    r2 = r_2 / 100
    r3 = r_3 / 100

    # Calculating final balance
    BA_1 = round(P * (1 + r1 / m_1) ** m_1)
    BA_2 = round(P * (1 + r2 / m_2) ** m_2)
    BA_3 = round(P * (1 + r3 / m_3) ** m_3)

    B1.set(BA_1)  # Setting values for the readonly entry widgets
    B2.set(BA_2)
    B3.set(BA_3)


def clearAll():
    # Deleting the content from the entry box
    depositedAmount.delete(0, END)
    entR1.delete(0, END)
    entM1.delete(0, END)
    entR2.delete(0, END)
    entM2.delete(0, END)
    entR3.delete(0, END)
    entM3.delete(0, END)


# Label
lbl_depositedAmount = Label(window, text="Enter your deposited amount",
                            bg="white smoke")
lbl_depositedAmount.grid(row=0, column=0, sticky='w')

lblR1 = Label(window, text="Enter interest rate of the 1st bank",
              bg="white smoke")
lblR1.grid(row=4, column=0, sticky='w')

lblM1 = Label(window, text="Enter compounded periods of the 1st bank",
              bg="white smoke")
lblM1.grid(row=5, column=0, sticky='w')

lblR2 = Label(window, text="Enter interest rate of the 2nd bank",
              bg="white smoke")
lblR2.grid(row=9, column=0, sticky='w')

lblM2 = Label(window, text="Enter compounded periods of the 2nd bank",
              bg="white smoke")
lblM2.grid(row=10, column=0, sticky='w')

lblR3 = Label(window, text="Enter interest rate of the 3rd bank",
              bg="white smoke")
lblR3.grid(row=14, column=0, sticky='w')

lblM3 = Label(window, text="Enter compounded periods of the 3rd bank",
              bg="white smoke")
lblM3.grid(row=15, column=0, sticky='w')

lblBank1 = Label(window, text="Bank 1 has ($)", bg="white smoke")
lblBank1.grid(row=20, column=0, sticky='w')

lblBank2 = Label(window, text="Bank 2 has ($)", bg="white smoke")
lblBank2.grid(row=21, column=0, sticky='w')

lblBank3 = Label(window, text="Bank 3 has ($)", bg="white smoke")
lblBank3.grid(row=22, column=0, sticky='w')

# Entry
depositedAmount = Entry(window, width=20)
depositedAmount.grid(row=0, column=1, sticky='e')

entR1 = Entry(window, width=20)
entR1.grid(row=4, column=1)

entM1 = Entry(window, width=20)
entM1.grid(row=5, column=1, sticky='e')

entR2 = Entry(window, width=20)
entR2.grid(row=9, column=1, sticky='e')

entM2 = Entry(window, width=20)
entM2.grid(row=10, column=1, sticky='e')

entR3 = Entry(window, width=20)
entR3.grid(row=14, column=1, sticky='e')

entM3 = Entry(window, width=20)
entM3.grid(row=15, column=1, sticky='e')

# Readonly Entry

B1 = StringVar()
Bank1 = Entry(window, width=20, state='readonly', textvariable=B1, bg="white smoke")
Bank1.grid(row=20, column=1, sticky='e')

B2 = StringVar()
Bank2 = Entry(window, width=20, state='readonly', textvariable=B2, bg="white smoke")
Bank2.grid(row=21, column=1, sticky='e')

B3 = StringVar()
Bank3 = Entry(window, width=20, state='readonly', textvariable=B3, bg="white smoke")
Bank3.grid(row=22, column=1, sticky='e')

# Button for calculating
btnCalculate = Button(window, text='Calculate', bg="light blue",
                      command=Calculation, width=8)
btnCalculate.grid(row=18, column=2, pady=5, sticky='e')

# Clear all button
btnClear = Button(window, text='Clear', command=clearAll, bg="yellow")
btnClear.grid(row=25, column=1, sticky='w')


# Creating a dropdown menu
def showMenu():  # This function is to show the chosen result
    label.config(text=clicked.get())


options = ["Excellent", "Good", "Average", "Fair", "Poor"]

clicked = StringVar()

clicked.set("Rate me!")  # Default display of the menu

dropMenu = OptionMenu(window, clicked, *options)
dropMenu.config(bg="pink")  # Set colour for the menu button
dropMenu["menu"].config(bg="pink")  # Set colour for the menu background
dropMenu.grid(row=25, column=0, sticky='w')


# Quit button

def closeWindow():
    window.destroy()


btnQuit = Button(window, text='Quit', command=closeWindow, width=8, bg='red', fg='white')
btnQuit.grid(row=25, column=2, pady=5, sticky='e')

window.mainloop()
