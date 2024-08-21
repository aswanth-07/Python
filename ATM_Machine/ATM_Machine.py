# ATM_MACHINE
balance = 500  # Initial balance
while True:
    print("Welcome to the ATM Machine")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    # Taking the input from the user for the option
    user_choice = input("Please select an option (1-4): ")
    # Using conditionals to check which option is selected

    # Checking the balance
    if user_choice == "1":
        print(f"Your current balance is: ${balance:.2f}")
        continue

    #Withdrawing the money     
    elif user_choice == "2":
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print("Insufficient balance. Please enter a smaller amount.")
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            print(f"Your new balance is: ${balance:.2f}")

    # Depositing the money
    elif user_choice == "3":
        amount = float(input("Enter the amount to deposit: $"))
        balance += amount
        print(f"${amount:.2f} deposited successfully.")
        print(f"Your new balance is: ${balance:.2f}")
        continue

    # Exiting the ATM
    elif user_choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break  
    else:
        print("Invalid option. Please select a valid option (1-4).")
        continue  
    
