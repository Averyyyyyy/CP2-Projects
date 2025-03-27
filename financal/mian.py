#Avery bowman (group project, move to new project) finance project

import csv


USER_FILE = "user_finances.csv"


# Function to sign in or log in the user
def sign_in_or_log_in():
   username = input("Enter username: ")
   password = input("Enter password: ")


   # Validate credentials (for simplicity, assume username is unique)
   user_data = load_user_data(username)
  
   if user_data is None:
       print("Invalid login. Try again.")
       return None
   else:
       print("Login successful!")
       return username


# Function to load user data from CSV
def load_user_data(username):
   user_data = {"goals": [], "expenses": [], "incomes": []}


   try:
       with open(USER_FILE, mode="r", newline="") as file:
           reader = csv.DictReader(file)
           for row in reader:
               if row["username"] == username:
                   user_data["goals"] = eval(row["goals"]) if row["goals"] else []
                   user_data["expenses"] = eval(row["expenses"]) if row["expenses"] else []
                   user_data["incomes"] = eval(row["incomes"]) if row["incomes"] else []
                   return user_data
   except FileNotFoundError:
       print("User file not found. Creating a new one on save.")
  
   return None


# Function to save user data back to CSV
def save_user_data(username, user_data):
   updated_data = []
   user_found = False


   try:
       with open(USER_FILE, mode="r", newline="") as file:
           reader = csv.DictReader(file)
           for row in reader:
               if row["username"] == username:
                   row["goals"] = str(user_data["goals"])
                   row["expenses"] = str(user_data["expenses"])
                   row["incomes"] = str(user_data["incomes"])
                   user_found = True
               updated_data.append(row)
   except FileNotFoundError:
       pass  # If file doesn't exist, create a new one later


   # If user was not found, add new entry
   if not user_found:
       updated_data.append({
           "username": username,
           "goals": str(user_data["goals"]),
           "expenses": str(user_data["expenses"]),
           "incomes": str(user_data["incomes"])
       })


   # Write updated data back to CSV
   with open(USER_FILE, mode="w", newline="") as file:
       fieldnames = ["username", "goals", "expenses", "incomes"]
       writer = csv.DictWriter(file, fieldnames=fieldnames)
       writer.writeheader()
       writer.writerows(updated_data)


# Function to add an expense
def add_expense(user_data):
   name = input("Enter expense name: ")
   amount = float(input("Enter amount: "))
   category = input("Enter category: ")
   date = input("Enter date (YYYY-MM-DD): ")
  
   user_data["expenses"].append({"name": name, "amount": amount, "category": category, "date": date})
   print("Expense added successfully!")


# Function to add an income
def add_income(user_data):
   source = input("Enter income source: ")
   amount = float(input("Enter amount: "))
   date = input("Enter date (YYYY-MM-DD): ")


   user_data["incomes"].append({"source": source, "amount": amount, "date": date})
   print("Income added successfully!")


# Function to update goals
def update_goal(user_data):
   new_goal = input("Enter new goal description: ")
   amount = float(input("Enter target amount: "))


   user_data["goals"] = [{"goal": new_goal, "amount": amount}]
   print("Goal updated successfully!")


# Main program loop
def main():
   username = sign_in_or_log_in()
   if not username:
       return


   user_data = load_user_data(username) or {"goals": [], "expenses": [], "incomes": []}


   while True:
       print("\nMenu:")
       print("1. View Goals")
       print("2. Add Expense")
       print("3. Add Income")
       print("4. Update Goal")
       print("5. Save & Exit")


       choice = input("Enter your choice: ")


       if choice == "1":
           print("\nCurrent Goals:", user_data["goals"])
           print("Expenses:", user_data["expenses"])
           print("Incomes:", user_data["incomes"])
       elif choice == "2":
           add_expense(user_data)
       elif choice == "3":
           add_income(user_data)
       elif choice == "4":
           update_goal(user_data)
       elif choice == "5":
           save_user_data(username, user_data)
           print("Data saved. Logging out...")
           break
       else:
           print("Invalid choice. Please try again.")


if __name__ == "__main__":
   main()