from blind_acution_art import logo

print(logo)

def find_highest_bidder(bidding_record):
    # highest_bid = 0
    winner = ""
    winner = max(bidding_record, key=bidding_record.get)

    # for bidder in bidding_record:
    #     bid_amount = bidding_record[bidder]
    #     if bid_amount > highest_bid:
    #         highest_bid = bid_amount
    #         winner = bidder
    # print(f"The winner is {winner} with a bid of ${highest_bid}")
    print(f"The winner is {winner} with a bid of ${bidding_record[winner]}")

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bid_dict = {}
end_candidate = False

while not end_candidate:
    bid_name = input("What is your name? ")
    bid_price = int(input("What is your price? $ "))

    bid_dict[bid_name] = bid_price
    
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        end_candidate = True
        find_highest_bidder(bid_dict)
    elif should_continue == "yes":
        print("\n" * 1000)
