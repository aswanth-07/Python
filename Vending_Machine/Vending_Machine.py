# VENDING MACHINE
"""Setting up empty variables to store the total amount of money gained 
   in the vending machine and the items available in the vending machine"""
items = {}
money_gained = 0

# Defining a function to access the owner window

def owner_window():
    global items,money_gained
    print("Welcome owner \nFeed/update the products for the wending machine")
    while True:
        a = input(
            "Enter item name (type 'done' to quite owner window and 'check' the amount inside the vending machine): "
        ).upper()
        if a == "DONE":
            break
        elif a == "CHECK":
            print(f"The amount in the vending machine is {money_gained}")
            break
        b = int(input("Enter price: "))
        items[a] = b

#MAIN LOOP

while True:
    print("\nWelcome to the Automated Vending Machine!")
    
    # Taking to owner window as the machine is setup for the first time
    if items == {}:  
        owner_window()
        continue
    
    # Printing the availaible items
    print("Available items:")
    for item, price in items.items():
        print(f"Item {item} - Price: ${price}")
    
    # Asking for the users choice
    customer_choice = input("Please select an item or type 'exit' to quit: ").upper()
    
    # Adding an hidden choice to open owner window 
    if customer_choice == "OWNER":  
        owner_window()
        continue
    
    #EXITING LOOP BLOCK
    if customer_choice == "EXIT":
        print("Exiting the vending machine. Have a great day!")
        break

    if customer_choice not in items:
        print("Invalid selection. Please try again.")
        continue

    item_price = items[customer_choice]
    total_money = 0
    
    # using loops to recieve money
    while total_money < item_price:
        money =input(
                f"Item {customer_choice} costs ${item_price}. Insert money (or type 'cancel' to cancel the transaction): "
            )
        
        # Terminating the transaction if the user enters 'cancel'
        if money == "cancel":  
            print("Transaction cancelled.")
            break
        if total_money+float(money) >= item_price:
            total_money += money
            change = total_money - item_price
            print(f"Dispensing item {customer_choice}.")
            if change > 0:
                print(f"Please take your change: ${change:.2f}")
                money_gained += item_price
            break
        
        # To check if the wants to add money or wants to cancel the transaction
        else:
            print(f"Not enough money inserted. You have inserted ${total_money:.2f}.")
            continue_choice = input(
                "Would you like to insert more money? (yes to continue, cancel to cancel the transaction): "
            ).lower()
            if continue_choice == "yes":
                continue
            if continue_choice == "cancel":
                print("Transaction cancelled. Returning inserted money.")
                break
