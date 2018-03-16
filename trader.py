'''
Wrapper of the gdax API to perform a quick market operation
'''

from gdax import AuthenticatedClient


class Trader:

    @staticmethod
    def buy(amount, price):
        '''
        Places a limit buy order with the given parameters to the GDAX exchange. 
        '''
        print("Buying {} for {}!".format(amount, price))

    @staticmethod
    def sell(amount, price):
        '''
        Places a limit sell order with the given parameters to the GDAX exchange.ValueError
        '''
        print("Selling {} for {}!".format(amount, price))
