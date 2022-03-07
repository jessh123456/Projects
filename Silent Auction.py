def integer_checker(question1, low):
    valid = False
    while not valid:
        error = "Whoops! you must enter a positive price/number!"
        try:
            response = float(input(question1))
            if low < response:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


def integer_checker2(question1, low):
    valid = False
    while not valid:
        error = "Whoops! you must enter a positive price/number!"
        try:
            response = float(input(question1))
            if low < response or response == -1:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


item = ""
reserve = ""
low = 0
leave = 0
bid = 0
current_bid = 0

item = input("What is the auction for? \n:").title()
reserve = integer_checker("What is the reserve price?\n:", low)
print(f"The auction for the {item} has started!!")
while leave != -1:
    print(f"The highest bid so far is ${bid}")
    current_bid = integer_checker2("What is your bid? (or press-1 to finish "
                                   "auction)\n:", low)
    if current_bid > bid:
        bid = current_bid
    elif current_bid == -1:
        leave = -1

if bid >= reserve:
    print(f"The auction for the {item}, sold with a price of ${bid}")
else:
    print(f"The reserve for the {item} did not meet the reserve of ${reserve}")
