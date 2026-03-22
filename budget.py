#project: Budget Calculator
#purpose: learn functions and calculations
#---SECTION 1: FUNCTION---
print("Welcome to the Budget Calculator!")
print("Please enter your monthly income and expenses.")
def calculate_budget(income, rent, food, transport, other):
    total_expenses = rent + food + transport + other
    remaining_budget = income - total_expenses
    savings_rate = (remaining_budget/income) * 100
    print(f"Total Expenses: £{total_expenses:.2f}")
    print(f"Remaining Budget: £{remaining_budget:.2f}")
    print(f"Savings Rate: {savings_rate:.2f}%")
    return total_expenses, remaining_budget, savings_rate
#---SECTION 2: BUDGET HEALTH CHECK---
def budget_health_check(savings_rate):
    if savings_rate >= 20:
        print("Your budget is healthy! Keep up the good work.")
    elif savings_rate >= 10:
        print("Your budget is okay, but there's room for improvement.")
    else:
        print("Your budget is tight. Consider reducing expenses or increasing income.")
#---SECTION 3: RUN EVERYTHING---
# Calculate the budget and get the savings rate
total_expenses, remaining_budget, savings_rate = calculate_budget(
    income=3000,
    rent=1000,
    food=500,
    transport=200,
    other=300
)        
budget_health_check(savings_rate)
