# Paste your code into this box
balance = int(raw_input("Enter Balance. "))
annualInterestRate = float(raw_input("Enter Annual Interest Rate. "))

lowPay = 0
remBal = balance
totalAmountPaid = 0.0
interest = 0.0

while True:
    if (remBal <= 0):
        break
    else:
        remBal = balance
        lowPay = lowPay + 10
        for month in range(1,13):   
            remBal = remBal - lowPay
            interest = annualInterestRate * remBal /  12.0
            remBal = remBal + interest
            totalAmountPaid = totalAmountPaid + lowPay
print("Lowest Payment: " + str(lowPay))