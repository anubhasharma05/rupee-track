import pandas as pd
import matplotlib.pyplot as plt
import os

# STEP 1: INSTALL REQUIRED LIBRARIES
# pip install pandas matplotlib

# STEP 2: SAMPLE DATA FUNCTION (updated to INR)
def create_sample_data():
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'description': ['Grocery shopping', 'Gas station', 'Restaurant dinner', 'Coffee shop'],
        'amount': [500.0, 300.0, 400.0, 100.0]  # In INR
    }
    df = pd.DataFrame(data)
    df.to_csv('sample_expenses.csv', index=False)
    print("Sample data created: sample_expenses.csv (in INR)")

# STEP 3: LOAD AND PROCESS DATA (same as before)
def load_and_process_data(file_path):
    try:
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')
        df['category'] = df['description'].apply(categorize_expense)
        return df
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Starting with empty data.")
        return pd.DataFrame(columns=['date', 'description', 'amount', 'category', 'month'])

# STEP 4: CATEGORIZE EXPENSES (same as before)
def categorize_expense(description):
    desc_lower = description.lower()
    if 'food' in desc_lower or 'restaurant' in desc_lower or 'grocery' in desc_lower or 'coffee' in desc_lower:
        return 'Food'
    elif 'gas' in desc_lower or 'fuel' in desc_lower or 'station' in desc_lower:
        return 'Transportation'
    else:
        return 'Other'

# STEP 5: CALCULATE TOTALS (updated to display in INR)
def calculate_totals(df):
    if df.empty:
        return 0, {}
    total_spending = df['amount'].sum()
    category_totals = df.groupby('category')['amount'].sum().to_dict()
    return total_spending, category_totals

# STEP 6: CREATE VISUALIZATION (updated title to INR)
def create_visualization(df):
    if df.empty:
        print("No data to visualize.")
        return
    category_totals = df.groupby('category')['amount'].sum()
    category_totals.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
    plt.title('Expense Breakdown by Category (in INR)')
    plt.ylabel('')
    plt.savefig('expense_chart.png')
    plt.show()

# STEP 7: SAVE DATA TO CSV (same as before)
def save_data(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

# STEP 8: ADD EXPENSE INTERACTIVELY (updated to INR)
def add_expense(df):
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        description = input("Enter description: ").strip()
        amount = float(input("Enter amount in INR: ").strip())
        # Validate date format
        pd.to_datetime(date)  # Will raise error if invalid
        # Create new row
        new_row = pd.DataFrame({
            'date': [date],
            'description': [description],
            'amount': [amount]
        })
        # Append to df
        df = pd.concat([df, new_row], ignore_index=True)
        # Re-process (add category and month)
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')
        df['category'] = df['description'].apply(categorize_expense)
        print("Expense added successfully!")
        return df
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        return df

# STEP 9: MAIN MENU (updated to display in INR)
def main_menu(df, file_path, budget):
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Total Spending and Categories")
        print("3. Create Visualization (Pie Chart)")
        print("4. Set Budget (in INR)")
        print("5. Check Budget Alert")
        print("6. Save and Exit")
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            df = add_expense(df)
        elif choice == '2':
            total, categories = calculate_totals(df)
            print(f"\nTotal Spending: ₹{total:.2f}")
            print("Category Totals:")
            for cat, amt in categories.items():
                print(f"  {cat}: ₹{amt:.2f}")
        elif choice == '3':
            create_visualization(df)
        elif choice == '4':
            try:
                budget = float(input("Enter new budget in INR: ").strip())
                print(f"Budget set to ₹{budget:.2f}")
            except ValueError:
                print("Invalid budget. Please enter a number.")
        elif choice == '5':
            total, _ = calculate_totals(df)
            if total > budget:
                print(f"Budget alert: You've spent ₹{total:.2f}, exceeding your ₹{budget:.2f} budget!")
            else:
                print(f"You're under budget. Spent: ₹{total:.2f}, Budget: ₹{budget:.2f}")
        elif choice == '6':
            save_data(df, file_path)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

# STEP 10: MAIN FUNCTION (updated default budget to INR)
def main():
    file_path = 'sample_expenses.csv'
    budget = 5000.0  # Default budget in INR
    
    # Create sample data if file doesn't exist
    if not os.path.exists(file_path):
        create_sample_data()
    
    # Load data
    df = load_and_process_data(file_path)
    
    # Start interactive menu
    main_menu(df, file_path, budget)

# Run the program
if __name__ == '__main__':
    main()
