class InvalidWithdrawalAmount(Exception):
    pass


class AccountAlreadyExists(Exception):
    pass


class InvalidDepositAmount(Exception):
    pass


class AccountNotFound(Exception):
    pass


class ClientDoNotExist(Exception):
    pass


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}

    def add_client(self, client_name):
        if client_name not in self.clients:
            self.clients[client_name] = Client(client_name)
            print(f"New Client added {client_name}")
        return self.clients[client_name]

    def remove_client(self, client_name):
        if client_name in self.clients:
            del self.clients[client_name]
            print(f"Client {client_name} has been removed successfully")
        else:
            raise ClientDoNotExist("Client do not exist in the system")

    def transfer(self, sender, sender_currency, receiver, receiver_currency, amount):
        if sender_currency != receiver_currency:
            raise ValueError("Transaction failed. Currencies do not match")

        sender_acc = sender.get_account(sender_currency)
        receiver_acc = receiver.get_account(receiver_currency)
        sender_acc.withdraw(amount)
        receiver_acc.deposit(amount)
        print(
            f"Transfer {amount} {sender_currency} from {sender.name} to {receiver.name} has completed successfully."
        )

    pass


class Account:
    def __init__(self, currency):
        self.currency = currency
        self.balance = 0

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(
                f"Your account was deposited by {amount}{self.currency}. Current balance is {self.balance} "
            )
        else:
            raise InvalidDepositAmount("Deposit amount can only be positive value")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InvalidWithdrawalAmount("You have insufficient funds on your account")
        else:
            self.balance -= amount
            print(
                f"You have withdrawn {amount} {self.currency}. Current balance is {self.balance}"
            )
        pass


class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def open_account(self, currency):
        if currency in self.accounts:
            raise AccountAlreadyExists(f"You already have Account in {currency}")
        self.accounts[currency] = Account(currency)
        print(f"{self.name} opened account in {currency}.")

    def close_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound(f"Account {currency} is not found")
        del self.accounts[currency]
        print(f"{self.name} closed account in {currency}.")

    def get_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound(f"Account in {currency} is not found.")
        return self.accounts[currency]

    pass
