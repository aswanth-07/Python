# Vending Machine

## Overview

The **Vending Machine** project is a simple Python-based simulation of a vending machine. The program allows the owner to set up and update items in the vending machine, and allows customers to purchase items by inserting money. The machine tracks the total money gained from transactions and handles the process of dispensing items and giving change.

## Features

- **Owner Mode**: 
  - Add or update items and their prices.
  - Check the total amount of money gained by the vending machine.
  
- **Customer Mode**: 
  - View available items and their prices.
  - Select an item to purchase.
  - Insert money and receive change if applicable.
  - Cancel a transaction at any point before the item is dispensed.

## How It Works

1. **Owner Setup**:
   - When the program starts, the owner is prompted to set up the vending machine by adding items and their respective prices.

2. **Customer Interaction**:
   - After setup, customers can view the available items and choose one to purchase.
   - The customer inserts money, and the machine checks if the amount is sufficient to purchase the selected item.
   - If the customer inserts more money than required, the machine provides change.
   - Customers can cancel the transaction at any time before the item is dispensed.

3. **Hidden Owner Mode**:
   - A hidden option allows the owner to re-enter the setup mode by typing "OWNER" at the item selection prompt.

## Code Structure

### Global Variables

- `items`: A dictionary that stores the available items and their prices.
- `money_gained`: A variable that tracks the total amount of money collected by the vending machine.

### Functions

- `owner_window()`: 
  - Allows the owner to add or update items and check the money gained.


### Main Loop

- Continuously runs to simulate the vending machine operation, allowing for owner setup, customer transactions, and exit from the program.

## Usage

1. **Run the program**.
2. **Set up the vending machine** by adding items and prices.
3. **Interact as a customer**:
   - View available items.
   - Select an item to purchase.
   - Insert money and complete the transaction.
4. **Exit** the program by typing "EXIT" at any prompt.

## Requirements

- Python 3.x

## Notes

- The program is text-based and runs in the terminal/command prompt.
- Future enhancements could include additional features like inventory management, multiple currencies, or a graphical interface.

## License

This project is open-source and available under the [MIT License](LICENSE).
