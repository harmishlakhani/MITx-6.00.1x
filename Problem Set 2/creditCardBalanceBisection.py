# Paste your code into this box
def remainingBalance(balance, annualInterestRate, lowPay):
    remBal = balance
    interest = 0.0

    for month in range(1,13):   
        remBal = remBal - lowPay
        interest = annualInterestRate * remBal /  12.0
        remBal = remBal + interest
    
    return remBal
    
balance = int(raw_input("Enter Balance. "))
annualInterestRate = float(raw_input("Enter Annual Interest Rate. "))

epsilon = 0.01
remBal = 0.0

# 0% interest
low = balance / 12.0
# annualInterestRate compound interest
high = balance * ((1 + (annualInterestRate / 12.0)) ** 12) / 12.0
mid = (low + high) / 2
remBal = remainingBalance(balance, annualInterestRate, mid)

while abs(remBal) > epsilon:
    if (remBal > 0):
        low = mid
    elif (remBal < 0):
        high = mid    
    mid = (low + high) / 2            
    remBal = remainingBalance(balance, annualInterestRate, mid)
print("Lowest Payment: " + str(round(mid, 2)))
