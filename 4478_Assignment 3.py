## Author: Nguyen Cao Ho Dang
## Date created: 28/03/2022
## Date last changed: 05/04/2022
## This program helps users to choose which bank to deposit their money for the highest final balance
## Input: interest rates for the first bank, interest rates for the second bank, interest rates for third bank, compounded periods of the first, second and third bank, and deposited money

# Opening a file
f = open("intro.txt", "r")
content = f.readlines()
print (content)

# Showing menu
def menu():
    print("\nPress 1 to start")
    print("\nPress 2 to exit\n")

    while True:
        choice = input()
        if choice == "1":
            return True
        else:
            print("Program has ended")
            exit()
menu()
if True:
    P = int(input("Please enter the deposited amount: "))
    r_1, m_1 = (input("Please enter interest rate and compounded period of the first bank: ")).split()
    r_1, m_1 = [float(r_1), float(m_1)]
    r_2, m_2 = input("Please enter interest rate and compounded period of the second bank: ").split()
    r_2, m_2 = [float(r_2), float(m_2)]
    r_3, m_3 = input ("Please enter interest rate and compounded period of the third bank: ").split()
    r_3, m_3 = [float(r_3), float(m_3)]
# Calculate the annual yield percentage and final balance in three banks
    m1 = m_1/100
    m2 = m_2/100
    m3 = m_3/100

if m1 == m2 == m3:
    BA_1 = round(P * (1 + r_1 / m1) ** m1)
    BA_2 = round(P * (1 + r_2 / m2) ** m2)
    BA_3 = round(P * (1 + r_3 / m3) ** m3)
else:
    APY_1 = float((1.0 + r_1 / m1) ** m1 - 1.0)
    APY_2 = float((1.0 + r_2 / m2) ** m2 - 1.0)
    APY_3 = float((1.0 + r_3 / m3) ** m3 - 1.0)
    BA_1 = round(P * APY_1)
    BA_2 = round(P * APY_2)
    BA_3 = round(P * APY_3)

# Displaying results
def showResult():
    bankList = ("Bank 1 has $", "Bank 2 has $", "Bank 3 has $")
    fbList = [BA_1, BA_2, BA_3]
    for i in range(len(fbList)):
            print(bankList[i], fbList[i])
showResult()






    


        

        
        



        

    




    

    


