import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

auction_info = []
auction = True

def add_new_bidder(bidder_name, bidder_amount):
    new_bidder = {"bid": bidder_amount, "name": bidder_name}
    auction_info.append(new_bidder)

while auction:
    print('''
▀█▀ █░█ █▀▀   █▀█ █▀█ █ █░█ ▄▀█ ▀█▀ █▀▀   █▄▄ █ █▀▄ █▀▄ █ █▄░█ █▀▀   ▄▀█ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█
░█░ █▀█ ██▄   █▀▀ █▀▄ █ ▀▄▀ █▀█ ░█░ ██▄   █▄█ █ █▄▀ █▄▀ █ █░▀█ █▄█   █▀█ █▄█ █▄▄ ░█░ █ █▄█ █░▀█
''')

    print("Welcome to the private bidding auction")
    name = input("What is your name?: ").title()
    bid = float(input("How much would you like to bid?: $"))
    add_new_bidder(bidder_name=name, bidder_amount=bid)

    others = input("Are there any other bidders for this auction? Type 'yes' or 'no'.\n")
    if others.lower() == 'no':
        auction = False
        highest_bidder = max(auction_info, key=lambda x: x['bid'])
        winner = highest_bidder['name']
        highest_bid = highest_bidder['bid']
        print(f"The highest bidder is {winner} with a bid of ${highest_bid:.2f}")
        print("Thank you for your participation.")
    else:
        clear()
