import csv
import os

# Define the CSV file path (ensure it's in the same directory as the Python file)
CSV_FILE = "coins.csv"

# Function to get available countries from the CSV file
def get_available_countries():
    try:
        countries = []
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ignore empty rows
                    countries.append(row[0].strip())  # Add country name
        return countries
    except FileNotFoundError:
        print(f"Error: The file '{CSV_FILE}' was not found.")
        return []

# Function to load coin denominations for the selected country
def load_coin_denominations(country):
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0].strip().lower() == country.strip().lower():
                    # Parse the coin names and their values
                    coins = {}
                    for coin_data in row[1:]:
                        name, value = coin_data.split('-')
                        coins[name.strip()] = int(value.strip())
                    return coins
        print(f"Error: Country '{country}' not found in the CSV file.")
        return {}
    except FileNotFoundError:
        print(f"Error: The file '{CSV_FILE}' was not found.")
        return {}

# Function to solve the Coin Change problem
def coin_change(target, coins):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 coins needed for target 0
    coin_used = [-1] * (target + 1)  # To track coins used

    # Dynamic Programming to calculate minimum number of coins
    for i in range(1, target + 1):
        for coin, value in coins.items():
            if i >= value and dp[i - value] + 1 < dp[i]:
                dp[i] = dp[i - value] + 1
                coin_used[i] = coin
    
    # Backtrack to find which coins were used
    coins_used = []
    if dp[target] == float('inf'):  # No solution
        return dp[target], coins_used
    
    current_amount = target
    while current_amount > 0:
        coin = coin_used[current_amount]
        coins_used.append(coin)
        current_amount -= coins[coin]
    
    return dp[target], coins_used[::-1]  # Return coins used in reverse order

def main():
    print("Welcome to the Coin Change Solver!")

    # Step 1: Display available countries
    countries = get_available_countries()
    if not countries:
        print("No countries available. Exiting.")
        return
    
    print("Please choose a country from the following options:")
    for i, country in enumerate(countries, 1):
        print(f"{i}. {country}")

    # Step 2: Get user's country choice
    try:
        country_choice = int(input("Enter the number corresponding to your chosen country: ")) - 1
        if country_choice < 0 or country_choice >= len(countries):
            print("Invalid choice. Exiting.")
            return
    except ValueError:
        print("Invalid input. Exiting.")
        return

    country = countries[country_choice]

    # Step 3: Load the coin denominations for the selected country
    coins = load_coin_denominations(country)
    if not coins:
        print(f"Error loading coin denominations for {country}. Exiting.")
        return

    print(f"Available coin denominations for {country}: {coins}")

    # Step 4: Get the target amount from the user
    try:
        target = int(input("Enter the target amount: "))
        if target <= 0:
            print("Target amount must be positive. Exiting.")
            return
    except ValueError:
        print("Invalid target amount. Please enter a valid number. Exiting.")
        return

    # Step 5: Solve the Coin Change problem and display results
    num_coins, coins_used = coin_change(target, coins)
    
    if num_coins == float