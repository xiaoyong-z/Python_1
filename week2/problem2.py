monthly_interest_rate = annualInterestRate / 12.0
def month_balance(previous_balance):
    monthly_unpaid_balance = previous_balance - minimum_fixed_monly_payment
    updated_balance_each_month = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
    return updated_balance_each_month


temp = balance
i = 1
while True:
    balance = temp
    minimum_fixed_monly_payment = i * 10
    for j in range(12):
        balance = month_balance(balance)
    if balance > 0:
        i = i + 1
    else:
        break
print("Lowest Payment: ", i * 10)
