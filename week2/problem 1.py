def month_balance(previous_balance):
    monthly_interest_rate = annualInterestRate / 12.0
    minimum_monthly_payment = monthlyPaymentRate * previous_balance
    monthly_unpaid_balance = previous_balance - minimum_monthly_payment
    updated_balance_each_month = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
    return updated_balance_each_month


for i in range(12):
    balance = month_balance(balance)
print("Remaining balance: ", round(balance, 2))
