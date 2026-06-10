# 1. Centralized Data
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# This dictionary tracks the current status of the machine and updates dynamically
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

# 2. Helper Functions
def reporting():
    """Prints the current remaining resources."""
    print("\n--- Current Resources ---")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")
    print("-------------------------\n")

def check_resources(drink_ingredients):
    """Checks if there are enough ingredients for the chosen drink."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Prompts user for coins and returns the total value calculated."""
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        return quarters + dimes + nickels + pennies
    except ValueError:
        print("Invalid input. Assuming 0 coins.")
        return 0

def make_coffee(drink_name, drink_ingredients):
    """Deducts the required ingredients from resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!\n")

# 3. Main Application Loop
def coffee_machine():
    machine_on = True
    
    while machine_on:
        user_choice = input("What would you like to order? (espresso/latte/cappuccino) or type 'report' / 'off': ").lower()
        
        # Action 1: Turn off the machine
        if user_choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            machine_on = False
            
        # Action 2: Show the dynamic report
        elif user_choice == "report":
            reporting()
            
        # Action 3: Process a drink order
        elif user_choice in menu:
            drink = menu[user_choice]
            
            # Step A: Check if resources are available
            if check_resources(drink["ingredients"]):
                print(f"You have ordered {user_choice}. Cost: ${drink['cost']:.2f}")
                
                # Step B: Process payment
                total_paid = process_coins()
                print(f"You inserted: ${total_paid:.2f}")
                
                # Step C: Check payment success
                if total_paid >= drink["cost"]:
                    change = total_paid - drink["cost"]
                    if change > 0:
                        print(f"Here is ${change:.2f} in change.")
                    
                    # Update internal machine revenue
                    resources["money"] += drink["cost"]
                    
                    # Step D: Make coffee and update resources
                    make_coffee(user_choice, drink["ingredients"])
                else:
                    print("Sorry, that's not enough money. Money refunded.\n")
        else:
            print("Sorry, we don't have that option. Please try again.\n")

# Start the machine
coffee_machine()