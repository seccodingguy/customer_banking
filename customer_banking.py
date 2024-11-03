# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    menu = """You will receive prompts to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    The program will calculate and display the interest earned and the new balance for the savings 
    and CD accounts."""

    divider = "----------------------------------------------"

    print(menu)
    print(divider)

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("You'll now be prompted to enter the current balance, interest rate, and lenght of months for the savings account.")
    savings_balance = float(input("Current savings account balance:"))
    savings_interest = float(input("Current savings account interest rate:"))
    savings_maturity = int(input("Enter number of months the savings account matures:"))
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Updated savings balance is ${"{:.2f}".format(updated_savings_balance)} and interest earned is ${"{:.2f}".format(interest_earned)}.')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print(divider)

    print("You'll now be prompted to enter the current balance, interest rate, and lenght of months for the savings account.")
    cd_balance = float(input("Current CD account balance:"))
    cd_interest = float(input("Current CD account interest rate:"))
    cd_maturity = int(input("Enter number of months the CD account matures:"))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Updated CD balance is ${"{:.2f}".format(updated_cd_balance)} and interest earned is ${"{:.2f}".format(interest_earned)}.')

if __name__ == "__main__":
    # Call the main function.
    main()
