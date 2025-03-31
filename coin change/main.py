# Avery bowman, coin change

import csv
import os

# Get the absolute path to ensure the file is always found
CSV_FILE = os.path.join(os.path.dirname(__file__), "coins.csv")


def get_available_countries():
  
   #Reads the 'coins.csv' file and extracts a list of available countries.
   #Returns a list of countries that are available in the file.

   try:
       with open(CSV_FILE, mode="r") as file:
           reader = csv.reader(file)
           countries = [row[0].strip() for row in reader if row]  # Get first column (country names)
       return countries if countries else []
   except FileNotFoundError:
       print(f"Error: '{CSV_FILE}' not found.")
       return []


def load_coin_denominations(country):
  
  # Loads the coin denominations for the given country from the CSV file.
  # Returns a dictionary of coin names and their respective values.
  
   try:
       with open(CSV_FILE, mode="r") as file:
           reader = csv.reader(file)
           for row in reader:
               if row and row[0].strip().lower() == country.strip().lower():  # Match country name (case-insensitive)
                   coins = {coin.split('-')[0].strip(): int(coin.split('-')[1].strip()) for coin in row[1:]}
                   return coins
       # If country not found
       print(f"Country '{country}' not found in the CSV file.")
   except FileNotFoundError:
       print(f"Error: '{CSV_FILE}' not found.")
   return {}


def coin_change(target, coins):
  
   # Solves the Coin Change problem: Returns the minimum number of coins and which coins to use.
   # Uses dynamic programming to compute the result.
  
   dp = [float('inf')] * (target + 1)
   dp[0] = 0
   coin_used = [-1] * (target + 1)
  
   for i in range(1, target + 1):
       for coin, value in coins.items():
           if i >= value and dp[i - value] + 1 < dp[i]:
               dp[i] = dp[i - value] + 1
               coin_used[i] = coin
  
   # Backtrack to find the coins used
   coins_used = []
   if dp[target] == float('inf'):
       return dp[target], coins_used  # No solution found
  
   current_amount = target
   while current_amount > 0:
       coin = coin_used[current_amount]
       if coin == -1:
           break
       coins_used.append(coin)
       current_amount -= coins[coin]
  
   return dp[target], coins_used[::-1]  # Return the coins used in correct order


def main():
   print("Welcome to the Coin Change Solver!")
  
   # Display available countries
   countries = get_available_countries()
   if not countries:
       print("No countries found in the coin file.")
       return
  
   print("Please choose a country from the following options:")
   for i, country in enumerate(countries, 1):
       print(f"{i}. {country}")
  
   # Get user input for the country
   try:
       country_choice = int(input("Enter the number corresponding to your chosen country: ")) - 1
       if country_choice < 0 or country_choice >= len(countries):
           print("Invalid choice. Exiting.")
           return
   except ValueError:
       print("Invalid input. Exiting.")
       return
  
   country = countries[country_choice]
  
   # Load the coin denominations for the selected country
   coins = load_coin_denominations(country)
   if not coins:
       print(f"Error loading coin denominations for {country}.")
       return
  
   print(f"Available coin denominations for {country}: {coins}")
  
   # Get user input for the target amount
   try:
       target = int(input("Enter the target amount: "))
       if target <= 0:
           print("Target amount must be positive. Exiting.")
           return
   except ValueError:
       print("Invalid target amount. Please enter a valid number. Exiting.")
       return
  
   # Solve the Coin Change problem
   num_coins, coins_used = coin_change(target, coins)
  
   if num_coins == float('inf'):
       print("It's not possible to make that target amount with the given coins.")
   else:
       print(f"Minimum number of coins needed: {num_coins}")
       print(f"Coins used: {', '.join(coins_used)}")


if __name__ == "__main__":
   main()