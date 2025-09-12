monthly_income = float(input("Enter your monthly income: "))
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) # type: ignore

print(f"Your monthly savings are ${monthly_savings:.0f}.") 