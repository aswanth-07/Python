# ATM Machine

## Overview

The **ATM Machine** project is a simple Python program that simulates basic ATM functionalities, including checking balance, withdrawing money, depositing money, and exiting the program. The program allows users to interact with a simulated ATM through a text-based interface.

## Features

- **Check Balance**: 
  - View the current balance in the account.
  
- **Withdraw Money**: 
  - Withdraw a specified amount of money, provided there are sufficient funds in the account.
  
- **Deposit Money**: 
  - Deposit a specified amount of money into the account.

- **Exit**: 
  - Exit the ATM program.

## How It Works

1. **Starting Balance**:
   - The program starts with an initial balance of $500.

2. **User Interaction**:
   - The user is presented with a menu of options to check balance, withdraw money, deposit money, or exit.
   - The user selects an option by entering a number corresponding to the desired action.

3. **Balance Check**:
   - When the user selects the "Check Balance" option, the current account balance is displayed.

4. **Withdraw Money**:
   - When the user selects the "Withdraw Money" option, they are prompted to enter the amount to withdraw.
   - If the amount exceeds the current balance, an error message is displayed.
   - If the amount is within the available balance, the amount is deducted, and the new balance is displayed.

5. **Deposit Money**:
   - When the user selects the "Deposit Money" option, they are prompted to enter the amount to deposit.
   - The amount is added to the current balance, and the new balance is displayed.

6. **Exit**:
   - When the user selects the "Exit" option, the program terminates with a goodbye message.

## Code Structure

### Global Variables

- `balance`: A variable that tracks the current account balance. It is initialized to $500.

### Main Loop

- The main loop continuously runs the program, displaying the menu and processing user input until the user chooses to exit.

### Menu Options

- `Check Balance`: Displays the current balance.
- `Withdraw Money`: Allows the user to withdraw money if sufficient funds are available.
- `Deposit Money`: Allows the user to deposit money into the account.
- `Exit`: Exits the program.

## Usage

1. **Run the program**.
2. **Select an option** from the menu by entering the corresponding number:
   - 1 to check the balance.
   - 2 to withdraw money.
   - 3 to deposit money.
   - 4 to exit the program.
3. **Follow the prompts** to complete the selected transaction.
4. **Exit** the program by selecting option 4.

## Requirements

- Python 3.x

## Notes

- The program is text-based and runs in the terminal/command prompt.
- Future enhancements could include adding PIN authentication, multiple accounts, and transaction history.

## License

This project is open-source and available under the [MIT License](LICENSE).

