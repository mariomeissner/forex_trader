'''
A bot that rides the waves of the crypto market. 
'''

import time
from gdax import PublicClient
from enum import Enum
from trader import Trader

# Status enumerate
class Status(Enum):
    STABLE = 0
    ASCENDING = 1
    DESCENDING = 2

# Take price average every X seconds
PERIOD = 1*10
# Take X samples to compute average (evenly distributed in PERIOD)
SAMPLES = 2
# Amount of elements that we want to store in the log
NUM_LOG_ENTRIES = 3
# Amount of money to invest in each ride, in euros
INVESTMENT = 5


# Status of the product
status = Status.DESCENDING
# Store the last NUM_LOG_ENTRIES prices
price_log = list()
# Money this bot has made since it started working
money_made = 0
# API public client
public_agent = PublicClient()
# Price at which we bought last time
last_buy_price = 0

print("GDAX Bot ready for trading!")


# Watch the market for a few iterations to fill the log
for _ in range(NUM_LOG_ENTRIES - 1):
    average_price = 0
    for _ in range(SAMPLES):
        ticker = public_agent.get_product_ticker(product_id='ETH-EUR')
        price = float(ticker['price'])
        average_price += price
        print("Polled price: {}".format(price))
        time.sleep(PERIOD/SAMPLES)
    average_price = average_price / SAMPLES

    # Add new price entry
    price_log.insert(0, price)

while(True):

    # Get new price average
    average_price = 0
    for x in range(SAMPLES):
        ticker = public_agent.get_product_ticker(product_id='ETH-EUR')
        price = float(ticker['price'])
        average_price += price
        print("Polled price: {}".format(price))
        time.sleep(PERIOD/SAMPLES)

    average_price = average_price / SAMPLES


    # Add new price entry and clean log if needed
    price_log.insert(0, price)
    try:
        price_log.pop(NUM_LOG_ENTRIES)
    except IndexError:
        # Log isn't filled yet, omit error
        pass
    

    # Compute behaviour of the last two changes
    current_change = price_log[0] - price_log[1]
    previous_change = price_log[1] - price_log[2]


    # If we were ascending but last two changes are negative, jump out
    if status is Status.ASCENDING and current_change <= 0 and previous_change <= 0:
        status = Status.DESCENDING
        print("Price is falling!")
        Trader.sell(INVESTMENT, price)

        # Compute how much we earned (if any lol)
        money = (price - last_buy_price)/last_buy_price * INVESTMENT
        money_made += money
        print("I made {}€ with the last investment. Total balance is: {}".format(money, money_made))
        if money > 0:
            print("I am a good bot :D")
        else:
            print("I am a total disaster... :(")
        

    # If we are descending, but last two changes were positive, jump in
    if status is Status.DESCENDING and current_change >= 0 and previous_change >= 0:
        status = Status.ASCENDING
        print("Price is going up!")
        Trader.buy(INVESTMENT, price)
        
        # Store buy price
        last_buy_price = price


