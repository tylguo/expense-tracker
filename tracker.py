import matplotlib.pyplot as plt

# Function to input monthly expenses
def input_expenses():
    categories = []
    expenses = []

    while True:
        category = input("Enter an expense category (or 'done' to finish): ")
        if category.lower() == 'done':
            break
        expense = float(input(f"Enter the monthly expense for {category}: $"))
        categories.append(category)
        expenses.append(expense)

    return categories, expenses

# Function to create a bar chart
def create_expense_chart(categories, expenses):
    plt.figure(figsize=(8, 5))
    plt.bar(categories, expenses, color='skyblue')
    plt.xlabel('Expense Categories')
    plt.ylabel('Monthly Expenses in USD')
    plt.title('Monthly Expense Chart')
    plt.show()

# Main function
def main():
    print("Monthly Expense Calculator")

    # Input expenses
    categories, expenses = input_expenses()

    if not categories:
        print("No expenses entered. Exiting.")
        return

    # Display expenses
    print("\nYour Monthly Expenses:")
    for category, expense in zip(categories, expenses):
        print(f"{category}: ${expense:.2f}")

    # Create and display the chart
    create_expense_chart(categories, expenses)

if __name__ == "__main__":
    main()
