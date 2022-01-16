logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

bids = {}
onwards = "yes"


def winner(bidding_record):
    """Thanks to this program, you can arrange secret auctions with your friends."""
    winner_bid = 0
    winner_name = ""
    for i in bidding_record:
        if bidding_record[i] > winner_bid:
            winner_bid = bidding_record[i]
            winner_name = i
    print(f"The winner is {winner_name} a bid of ${winner_bid}.")


while onwards == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid
    onwards = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if onwards == "no":
        winner(bids)





