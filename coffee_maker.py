chance = 0
def coins():
    print("Please insert coins.")
    pennies = int(input("How many pennies? "))*0.1
    dimes = int(input("How many dimes? "))*0.5
    nickels = int(input("How many nickels? "))*0.10
    quarters = int(input("How many quarters? "))*0.25
    return pennies+ dimes+ nickels+ quarters


def reporting():
    print("---Current resources:---")
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${resources['cost']:.2f}")

def check_resources(user_choice):
    
#         print("Water: 50ml")
#         print("Milk: 100ml")
#         print("Coffee: 76g")

def making_coffee(resources, ingredients):
    for item in ingredients:
        if item in resources and resources[item] >= ingredients[item]:
            resources[item] -= ingredients[item]
        else:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
def coffee_machine():
    coffee_making = True
    while coffee_making:

        print("COFFEE MACHINE")

        menu = {
            "espresso": {
                "ingredients": {
                    "water" : 50,
                    "coffee" : 18
                },
                "cost": 1.5
            },
            "latte" :{
                "ingredients":
                {
                    "water" : 200,
                    "milk" : 150,
                    "coffee" : 24
                },
                "cost": 2.5
            },
            "cappuccino" : {
                "ingredients":
                {
                    "water" : 250,
                    "milk" : 100,
                    "coffee" : 24
                },
                "cost": 3.0
            }
        }

        user_choice = input("What would you like to order?\n(espresso/latte/cappuccino) or report: ")
        if user_choice == "report":
            making_coffee(user_choice, menu[user_choice]['ingredients'])
            

        check_resources(user_choice)
        
        if user_choice in menu:
            print(f"You have ordered {user_choice}.\nPlease insert ${menu[user_choice]['cost']:.2f}")
        else:
            print("Sorry, we don't have that option.")
        inserted_coins = coins()
        total_coins_inserted = (inserted_coins[0] * 0.01) + (inserted_coins[1] * 0.10) + (inserted_coins[2] * 0.05) + (inserted_coins[3] * 0.25)
        print(f"You have inserted ${total_coins_inserted:.2f}.")
        if total_coins_inserted > menu[user_choice]['cost']:
            change = total_coins_inserted - menu[user_choice]['cost']
            print(f"Here is your change: ${change:.2f}.")
            print(f"Here is your {user_choice}. Enjoy!")
    
        elif total_coins_inserted < menu[user_choice]['cost']:
            print("sorry, that's not enough money. Money refunded.")
            print("Please insert coins again.")
        elif total_coins_inserted == menu[user_choice]['cost']:
            print(f"Here is your {user_choice}. Enjoy!")
        # if user_choice == "report":
        #     making_coffee(user_choice, menu[user_choice]['ingredients'])
            
        elif user_choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            coffee_making = False



coffee_machine()