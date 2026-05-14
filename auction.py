logo = '''                         ___________
                         \\         /
                          )_______(

                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_|_|_             __|_|.-''
                          |_______| '-' '-' ' '-' '-' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def find_highest_bidder(auction_dict):       
    highest_bid =0
    winner = " "
    for bidder in auction_dict:
            bid_amount = int(auction_dict[bidder])
            if bid_amount > highest_bid:
                    highest_bid = bid_amount
                    winner = bidder
        
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    

user_name = input("What is your name?\n")
print(f"Welcome {user_name} to the secret auction program.")
user_bids = int(input("Enter your bid amount : $ "))
auction_dict ={}
auction_dict[user_name] = user_bids

should_repeat = True

while should_repeat:
    user_choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if user_choice == "yes":
        print("\n" * 100)
        user_name = input("What is your name?\n")
        print(f"Welcome {user_name} to the secret auction program.")
        user_bids = int(input("Enter your bid amount : $ "))
        auction_dict[user_name] = user_bids
    else:
        should_repeat = False
        print("\n" * 100)
find_highest_bidder(auction_dict)
print("Hope you enjoyed the blind auction. see you Later !\n Bye!! bye!!")


            