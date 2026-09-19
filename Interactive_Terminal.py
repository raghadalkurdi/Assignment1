# Available inventory: Item Name -> Unit Price
catalog = {
    "laptop": 800,
    "mouse": 20,
    "keyboard": 50,
    "monitor": 150
}

# Variable to keep track of the cumulative total
grand_total = 0.0

# Interactive Command Loop
while True:
    # Prompt user for input and convert to lowercase for uniform checking
    user_input = input("Enter item to buy (or 'checkout' / 'exit'): ").strip().lower()

    # Check if user wants to exit without printing a receipt
    if user_input == "exit":
        print("--> Order canceled. Exiting program.")
        break

    # Check if user wants to checkout
    elif user_input == "checkout":
        # Calculate discount rate based on grand_total
        if grand_total >= 500:
            discount_percent = 0.10
        elif grand_total >= 200:
            discount_percent = 0.05
        else:
            discount_percent = 0.00

        # Calculate final bill amounts
        discount_amount = grand_total * discount_percent
        final_total = grand_total - discount_amount

        # Print final receipt
        print("\nCHECKOUT RECEIPT")
        print("========================================")
        print(f"Subtotal:     ${grand_total:.1f}")
        print(f"Discount:     ${discount_amount:.1f}")
        print(f"Final Total:  ${final_total:.1f}")
        print("========================================\n")
        
        break  # Exit the loop after printing the receipt

    # Check if the entered item exists in the catalog
    elif user_input in catalog:
        price = catalog[user_input]
        grand_total += price
        # Print item name capitalized for a clean presentation
        print(f"--> Added {user_input.capitalize()} (${price}) to order.")

    # Handle invalid item inputs
    else:
        print("--> [ERROR] Item not found in catalog. Try again.")