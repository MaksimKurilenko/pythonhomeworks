import datetime


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


# deposit/withdraw


class Account:
    def __init__(self, currency):
        self.currency = currency
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.log_history("Deposit", amount)
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
            self.log_history("Withdraw", amount)
            print(
                f"You have withdrawn {amount} {self.currency}. Current balance is {self.balance}"
            )

    def log_history(self, operation, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"[{timestamp}] {operation}: {amount} {self.currency}")

    pass


# transfer


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

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sender_acc.history.append(
            f"[{timestamp}] Transfer to {receiver.name}: -{amount} {sender_currency}"
        )
        receiver_acc.history.append(
            f"[{timestamp}] Transfer from {sender.name}: +{amount} {receiver_currency}"
        )

        print(
            f"Transfer {amount} {sender_currency} from {sender.name} to {receiver.name} has completed successfully."
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


# Terminal
bank = Bank("Your bank")
print("Welcome to Bank Terminal")

while True:
    print("\nSelect option:")
    print("1. Login")
    print("2. Register")
    print("0. Exit")

    user_choice = input("Enter your choice: ").strip()

    if user_choice == "0":
        print("Bye!")
        break
    user_name = input("Enter your user name: ").strip()
    if user_choice == "2":
        client = bank.add_client(user_name)

    elif user_choice == "1":
        if user_name not in bank.clients:
            print("Client not found.")
            continue
        else:
            print(f"Welcome, {user_name}")
            client = bank.clients[user_name]

    else:
        print("Invalid choice")
        continue

    while True:
        print(f"\nClient: {client.name}")
        print("1. Open Bank Account")
        print("2. Close Bank Account")
        print("3. Deposit Funds")
        print("4. Withdraw Funds")
        print("5. Transfer Funds")
        print("6. Show your Accounts")
        print("7. Save account history to file")
        print("8. Show operations history")
        print("0. Logout")

        choice = input("Select option: ").strip()

        try:
            if choice == "1":
                currency = input("Currency: ").upper()
                client.open_account(currency)

            elif choice == "2":
                for cur, acc in client.accounts.items():
                    print(f"{cur}: {acc.balance}")
                currency = input("Which to close? ").upper()
                client.close_account(currency)

            elif choice == "3":
                for cur, acc in client.accounts.items():
                    print(f"{cur}: {acc.balance}")
                currency = input("Currency: ").upper()
                amount = float(input("Amount: "))
                client.get_account(currency).deposit(amount)

            elif choice == "4":
                for cur, acc in client.accounts.items():
                    print(f"{cur}: {acc.balance}")
                currency = input("Currency: ").upper()
                amount = float(input("Amount: "))
                client.get_account(currency).withdraw(amount)

            elif choice == "5":
                target_name = input("Receiver Name: ").strip()
                if target_name == client.name:
                    print("Can't transfer to yourself.")
                    continue

                target_client = bank.clients.get(target_name)
                if not target_client:
                    print("Client not found.")
                    continue

                currency = input("Currency: ").upper()
                amount = float(input("Amount: "))
                bank.transfer(client, currency, target_client, currency, amount)

            elif choice == "6":
                for cur, acc in client.accounts.items():
                    print(f"{cur}: {acc.balance}")

            elif choice == "7":
                with open("balance.txt", "w") as fh:
                    fh.write(f"{user_name} balance status")
                    total = 0
                    for cur, acc in client.accounts.items():
                        fh.write(f"{cur}: {acc.balance}\n")
                        total += acc.balance
                    fh.write(f"Total balance: {total}\n")
            #
            elif choice == "0":
                print("Logging out...")
                break

            elif choice == "8":
                print(f"History of operations for {client.name}")

                if not client.accounts:
                    print("No account")
                    continue

                for currency, account in client.accounts.items():
                    print(f"{currency}")
                    if not account.history:
                        print("No history for Account")
                    else:
                        for record in account.history:
                            print(record)

            else:
                print("Invalid option. Try again.")
        except Exception as e:
            print(f"Error: {e}")
