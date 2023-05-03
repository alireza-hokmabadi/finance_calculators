import math

### =====================================================
### Ask user to choose calculator type and validate input
while True:
    print("investment \t - to calculate the amount of interest you'll earn on your investment")
    print("bond \t\t - to calculate the amount you'll have to pay on a home loan\n")
    cal_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

    # Convert input to lowercase for case-insensitivity
    cal_type = cal_type.lower()

    # Validate input
    if cal_type == "investment" or cal_type == "bond":
        print(f"You've chosen '{cal_type}' calculator \n")
        break
    else:
        print("\n\n*********************************************")
        print("You entered a wrong value!!! Please try again.\n\n")

### =====================================================
### Investment calculator
if cal_type == "investment":
    deposit = float(input("Please enter deposit amount: "))
    interest_rate = float(input("Please enter the interest rate (e.g. 5 for 5%): "))
    years = float(input("Please enter the number of investing years: "))
    interest = input("Please enter the the type of interest calculation ('simple' or 'compound'): ")

    # Convert input to lowercase for case-insensitivity
    interest = interest.lower()

    # Convert annual interest rate to decimal
    interest_rate /= 100

    if interest == "simple":
        total_amount = deposit * (1 + interest_rate * years)  # Simple interest formula
        print(f"\n===> Total amount once the '{interest}' interest has been applied is {total_amount} <===\n")

    elif interest == "compound":
        total_amount = deposit * math.pow((1 + interest_rate), years)  # Compound interest formula
        print(f"\n===> Total amount once the '{interest}' interest has been applied is {total_amount} <===\n")

    else:
        print("\nYou entered a wrong interest type!!! Please try again from beginning.\n")

### Bond calculator
elif cal_type == "bond":
    present_value = float(input("Please enter present value of the house: "))
    interest_rate = float(input("Please enter the interest rate (e.g. 5 for 5%): "))
    months = float(input("Please enter the number of months you plan to take to repay the bond: "))

    # Convert annual interest rate to decimal and monthly interest rate
    interest_rate /= 100
    interest_rate /= 12

    # Calculate monthly repayment using formula
    repayment = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-months))
    print(f"\n===> You will have to repay {repayment} each month <===\n")
