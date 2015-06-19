# Paste your code into this box
balance = int(raw_input("Enter Balance. "))
annualInterestRate = float(raw_input("Enter Annual Interest Rate. "))
monthlyPaymentRate = float(raw_input("Enter Monthly Payment Rate. "))

minMonPay = 0.0
remBal = balance
totalAmountPaid = 0.0
interest = 0.0

for month in range(1,13):
    minMonPay = remBal * monthlyPaymentRate
    
    remBal = remBal - minMonPay
    interest = annualInterestRate * remBal /  12.0
    remBal = remBal + interest
    
    totalAmountPaid = totalAmountPaid + minMonPay
    print("Month: " + str(month))
    print("Minimum monthly payment: " + str(round(minMonPay, 2)))
    print("Remaining balance: " + str(round(remBal, 2)))
    
print("Total paid: " + str(round(totalAmountPaid, 2)))
print("Remaining balance: " + str(round(remBal, 2)))