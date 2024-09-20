monthly_income = input('Enter your monthly income:')
total_monthly_expenses = input('Enter your total monthly expenses:')

print(monthly_income, total_monthly_expenses)

monthly_savings = int(monthly_income) - int(total_monthly_expenses)

principal = monthly_savings * 12
rate = 0.05
time = 1
interest =  principal * rate * time

#projected_savings = principal + interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print(f'Projected savings after one year, with interest, is: ${projected_savings}')