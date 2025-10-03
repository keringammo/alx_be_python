# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initialize the BankAccount with an optional initial balance.
        Defaults to 0.0 if no value is provided.
        """
        self.__account_balance = float(initial_balance)  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposit a given positive amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a given amount if sufficient funds are available.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
