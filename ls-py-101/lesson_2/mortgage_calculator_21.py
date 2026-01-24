# Ask user for loan amount
# Ask user for APR
# Ask user for loan duration (years and months)

# Give monthly interest rate (APR/12)
# Give loan duration in months
# Give monthly payment

def get_float_input(prompt, allow_blank = False, allow_zero = False):
    while True:
        value = input(prompt)
        if allow_blank and value == "":
            return 0.0
        try:
            num = float(value)
            if num < 0:
                print("No negative numbers.")
                continue
            if not allow_zero and num == 0:
                print("Value cannot be zero.")
                continue
            return num
        except ValueError:
            print("Numbers only.")

def mortgage_calculator():
    loan_amount = get_float_input("Hi. We'll calculate your mortgage. "
                                  "First enter your loan amount: ")

    annual_rate = get_float_input("Now enter your APR (press enter for 0): ",
                                  allow_blank = True, allow_zero = True)

    loan_years = get_float_input("Now enter just the years of your loan "
                                 "(press enter for 0): ", 
                                 allow_blank = True, allow_zero = True)

    loan_months = get_float_input("Now enter just the months of your loan "
                                  " (press enter for 0): ", 
                                  allow_blank = True, allow_zero = True)

    loan_duration_months = (loan_years * 12 + loan_months)
    monthly_int_rate = (annual_rate / 100) / 12

    if loan_duration_months == 0:
        print("Loan duration is zero. Program will exit.")
        return

    if monthly_int_rate == 0:
        monthly_payment = loan_amount / loan_duration_months
    else:
        monthly_payment = loan_amount * (monthly_int_rate /
        (1 - (1 + monthly_int_rate) ** (-loan_duration_months)))

    print("\nLoan Summary:")
    print(f"Loan amount: ${loan_amount:,.2f}")
    print(f"APR: {annual_rate}%")
    print(f"Monthly interest rate: {monthly_int_rate * 100:.3f}%")
    print(f"Loan duration: {int(loan_duration_months)} months")
    print(f"Your monthly loan payment is ${monthly_payment:.2f}")

while True:
    mortgage_calculator()
    again = input("Wanna calculate again? Enter 'y' if yes: ").lower()
    if again != 'y':
        print("Bye!")
        break