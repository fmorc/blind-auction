from replit import clear
from art import logo

print(logo)

bidders = {}
other_bidders = 'yes'
while other_bidders == 'yes' or other_bidders == 'y':
    name = input("What is your name: ")
    bid = int(input("What's your bid? $"))
    other_bidders = input("Are there any other bidders? ")

    bidders[name] = bid
    clear()

max_bidder = ""
max_value = 0
for key in bidders:
    if bidders[key] > max_value:
        max_value = bidders[key]
        max_bidder = key

print(f"The winner is {max_bidder} who made a bid of ${max_value}")
