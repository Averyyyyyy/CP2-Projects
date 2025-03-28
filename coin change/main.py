# Avery bowman, coin change

import csv
import os


def get_available_countries():
   # Reads the 'coins.csv' file and extracts a list of available countries.
   # Returns a list of country names.
   try:
       with open("coins.csv", mode="r") as file:
           reader = csv.reader(file)
           countries = [row[0].strip() for row in reader if row]  # Get first column (country names)
       return countries if countries else []
   except FileNotFoundError:
       print("Error: 'coins.csv' file not found.")
       return []


def load_coin_denominations(country):
   # Loads coin denominations for a given country from the 'coins.csv' file.
   # Returns a sorted list of (coin_name, coin_value) tuples.
   try:
       with open("coins.csv", mode="r") as file:
           reader = csv.reader(file)
           for row in reader:
               if row[0].strip().lower() == country.lower():
                   coins = row[1:]  # Extract coin denominations
                   denominations = []
                   for coin in coins:
                       try:
                           name, value = coin.split("-")
                           denominations.append((name.strip(), int(value.strip())))
                       except ValueError:
                           print(f"Invalid format in file for {country}: {coin}")
                           return []
                   return sorted(denominations, key=lambda x: x[1], reverse=True)  # Sort by value (descending)
       print(f"Country '{country}' not found in the file.")
       return []
   except FileNotFoundError:
       print("Error: 'coins.csv' file not found.")
       return []


def coin_change(target_amount, denominations):
   # Solves the Coin Change Problem using a greedy approach.
   # Returns the minimum number of coins needed and their names.
   if target_amount <= 0:
       return 0, []


   min_coins = 0
   coins_used = []


   for coin_name, coin_value in denominations:
       count = target_amount // coin_value
       if count > 0:
           min_coins += count
           coins_used.extend([coin_name] * count)
           target_amount -= count * coin_value


       if target_amount == 0:
           break


   if target_amount > 0:
       print("Exact change cannot be made with the available denominations.")
       return -1, []
  
   return min_coins, coins_used


def main():
   # Main function to interact with the user and execute the coin change logic.
   print("Welcome to the Coin Change Solver!")
  
   # This might be the problem beacuse it cant grab the names form the csv
   # List available countries
   countries = get_available_countries()
   if not countries:
       print("No countries found in 'coins.csv'. Exiting...")
       return


   print("\nAvailable countries:")
   for country in countries:
       print(f" - {country}")


   # Ask user for input
   country = input("\nEnter the country from the list above: ").strip()
   if country not in countries:
       print("Invalid country. Please restart and select from the available options.")
       return


   denominations = load_coin_denominations(country)


   if not denominations:
       print("No valid denominations found. Exiting...")
       return


   try:
       target_amount = int(input("Enter the target amount: ").strip())
       if target_amount < 0:
           print("Please enter a non-negative target amount.")
           return
   except ValueError:
       print("Invalid input. Please enter a valid number.")
       return


   min_coins, coins_used = coin_change(target_amount, denominations)


   if min_coins == -1:
       print("No valid combination found for the given amount.")
   else:
       print(f"Minimum number of coins needed: {min_coins}")
       print(f"Coins used: {', '.join(coins_used)}")


if __name__ == "__main__":
   main()