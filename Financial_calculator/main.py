#Avery Financial Calculator

def main():
    print("Welcome to the Financial Calculator!")
    while True:
        print("\nChoose an option:")
        print("1. Savings Goal Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        #The user picks what option they want to continue with
        if choice == "1":
            savings_goal_calculator()
        elif choice == "2":
            compound_interest_calculator()
        elif choice == "3":
            budget_allocator()
        elif choice == "4":
            sale_price_calculator()
        elif choice == "5":
            tip_calculator()
        elif choice == "6":
            print("Thank you for using the Financial Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#This will print if the user prints 1
def savings_goal_calculator():
    goal = float(input("\nEnter your savings goal: $"))
    deposit = float(input("Enter your weekly or monthly deposit: $"))
    frequency = input("Is this a 'weekly' or 'monthly' deposit?").strip().lower()
    
    if frequency == "weekly":
        time_needed = goal / deposit / 4
    elif frequency == "monthly":
        time_needed = goal / deposit
    else:
        print("Invalid input for frequency.")
        return

    print(f"\nIt will take approximately {time_needed:.2f} months to reach your goal.")

#This will print if the user picks 2
def compound_interest_calculator():
    principal = float(input("\nEnter the initial amount (principal): $"))
    rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    times_per_year = int(input("Enter the number of times interest is compounded per year: "))
    years = float(input("Enter the number of years: "))
    
    amount = principal * (1 + rate / times_per_year) ** (times_per_year * years)
    print(f"\nThe total amount after {years} years will be: ${amount:.2f}")

#This will print if the user picks 3
def budget_allocator():
    income = float(input("\nEnter your total income: $"))
    savings = income * 0.2
    entertainment = income * 0.1
    food = income * 0.3
    other = income - (savings + entertainment + food)
    
    print(f"\nBudget Allocation:")
    print(f"Savings: ${savings:.2f}")
    print(f"Entertainment: ${entertainment:.2f}")
    print(f"Food: ${food:.2f}")
    print(f"Other: ${other:.2f}")

#This will print if the user picks 4
def sale_price_calculator():
    original_price = float(input("\nEnter the original price: $"))
    discount = float(input("Enter the discount percentage: ")) / 100
    
    sale_price = original_price * (1 - discount)
    print(f"\nThe sale price is: ${sale_price:.2f}")

#This will print if the user picks 5
def tip_calculator():
    bill = float(input("\nEnter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage you want to give: ")) / 100
    
    tip_amount = bill * tip_percentage
    total = bill + tip_amount
    print(f"\nTip Amount: ${tip_amount:.2f}")
    print(f"Total Bill (with tip): ${total:.2f}")

if __name__ == "__main__":
    main()