# Given values
P = 2500  # monthly payment
r = 0.0575  # monthly interest rate
n = 73  # number of payments (months)

# Future Value (FV) calculation using the formula for the future value of an annuity
FV = P * (((1 + r)**n - 1) / r)
# print(FV)
for month in range(n):
    amount = P * (((1 + r)**month -1) / r) 
    print("month: ", month, " = R",round(amount,2))
    if month % 12 == 0:
        print("")
