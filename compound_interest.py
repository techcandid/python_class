# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time):
    # Convert rate to decimal and calculate the number of compounding periods per year (assuming annual compounding)
    rate = rate / 100
    n = 1  # Assuming annual compounding

    # Calculate compound interest
    amount = principal * (1 + rate/n)**(n*time)
    interest = amount - principal
    return interest

# Input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period (in years): "))

# Calculate compound interest
compound_interest = calculate_compound_interest(principal, rate, time)

# Display the result
print(f"Compound interest after {time} years: {compound_interest:.2f}")
