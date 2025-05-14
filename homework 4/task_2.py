from task_1 import Bank

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

            elif choice == "0":
                print("Logging out...")
                break

            else:
                print("Invalid option. Try again.")

        except Exception as e:
            print(f"Error: {e}")
