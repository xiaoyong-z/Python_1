monthly_interest_rate = annualInterestRate / 12.0


def month_balance(previous_balance):
    monthly_unpaid_balance = previous_balance - minimum_fixed_monly_payment
    updated_balance_each_month = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
    return updated_balance_each_month


temp = balance
lower = balance // 12
upper = balance * (1 + annualInterestRate) // 12
while upper > lower:
    balance = temp
    middle = (lower + upper) / 2
    minimum_fixed_monly_payment = middle
    for j in range(12):
        balance = month_balance(balance)
    if abs(balance) < 0.99 * 0.99 * 0.99:
        break
    elif balance > 0:
        lower = middle
    elif balance < 0:
        upper = middle
print("Lowest Payment: ", round(middle, 2))