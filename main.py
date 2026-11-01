import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create expenses table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
""")

conn.commit()


# Function to get a valid expense amount
def get_valid_amount():

    while True:
        try:
            amount = float(input("Enter expense amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Invalid input! Please enter a numeric amount.")


# Function to get non-empty text input
def get_valid_text(prompt):

    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("This field cannot be empty. Please try again.")


# Function to add expense
def add_expense():
    amount = get_valid_amount()
    category = get_valid_text("Enter expense category: ")
    description = get_valid_text("Enter expense description: ")

    expense_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, expense_date))

    conn.commit()
    print("\nExpense added successfully!")


# Function to view expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for expense in expenses:
        print("ID:", expense[0])
        print("Amount: ₹", expense[1])
        print("Category:", expense[2])
        print("Description:", expense[3])
        print("Date:", expense[4])
        print("--------------------------------")


# Function for category-wise analysis
def category_analysis():
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    category_totals = cursor.fetchall()

    print("\n========== CATEGORY-WISE EXPENSES ==========")

    if not category_totals:
        print("No expenses recorded yet.")
        return

    for category in category_totals:
        print(category[0], ": ₹", category[1])


# Function to delete an expense
def delete_expense():

    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Invalid ID! Please enter a numeric expense ID.")
        return

    # Check whether expense exists
    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if expense is None:
        print("Expense ID not found!")
        return

    # Confirm before deleting
    confirmation = input(
        "Are you sure you want to delete this expense? (yes/no): "
    ).lower().strip()

    if confirmation in ("YES", "Yes", "yes", "Y", "y"):
        cursor.execute(
            "DELETE FROM expenses WHERE id = ?",
            (expense_id,)
        )

        conn.commit()
        print("\nExpense deleted successfully!")

    elif confirmation in ("NO", "No", "no", "N", "n"):
        print("\nDeletion cancelled.")

    else:
        print("\nInvalid input! Deletion cancelled.")

# Function to update an expense
def update_expense():

    try:
        expense_id = int(input("Enter expense ID to update: "))
    except ValueError:
        print("Invalid ID! Please enter a numeric expense ID.")
        return

    # Check whether expense exists
    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if expense is None:
        print("Expense ID not found!")
        return

    # Get updated details
    amount = get_valid_amount()
    category = get_valid_text("Enter new category: ")
    description = get_valid_text("Enter new description: ")

    # Update database record
    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
    """, (amount, category, description, expense_id))

    conn.commit()

    print("\nExpense updated successfully!")


# Function for monthly summary
def monthly_summary():
    current_month = datetime.now().strftime("%Y-%m")

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE date LIKE ?
    """, (current_month + "%",))

    monthly_total = cursor.fetchone()[0]

    print("\n========== MONTHLY EXPENSE SUMMARY ==========")
    print("Month:", current_month)
    print("Total Expenses: ₹", monthly_total)


# Function to display expense dashboard
def expense_dashboard():

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(amount), 0),
            COALESCE(AVG(amount), 0),
            COALESCE(MAX(amount), 0)
        FROM expenses
    """)

    dashboard = cursor.fetchone()

    print("\n========== EXPENSE DASHBOARD ==========")
    print("Total Expenses Recorded:", dashboard[0])
    print("Total Money Spent: ₹", round(dashboard[1], 2))
    print("Average Expense: ₹", round(dashboard[2], 2))
    print("Highest Expense: ₹", round(dashboard[3], 2))


# Function to display expense chart
def expense_chart():

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    data = cursor.fetchall()

    if not data:
        print("No expenses available to display.")
        return

    categories = [item[0] for item in data]
    amounts = [item[1] for item in data]

    plt.figure(figsize=(8, 5))

    plt.bar(categories, amounts)

    plt.title("Category-wise Expense Analysis")
    plt.xlabel("Expense Categories")
    plt.ylabel("Total Amount (₹)")

    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.show()


# Main menu
while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Category-wise Expense Analysis")
    print("5. Monthly Expense Summary")
    print("6. Delete Expense")
    print("7. Expense Dashboard")
    print("8. Expense Chart")
    print("9. Exit")

    choice = input("\nEnter your choice (1-9): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        category_analysis()

    elif choice == "5":
        monthly_summary()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        expense_dashboard()

    elif choice == "8":
        expense_chart()

    elif choice == "9":
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 9.")

# Close database connection
conn.close()