# forex_trader
A modular trading bot that supports pluggable brokers and experts. 

## Structure: 
- **Trader**: The core of the system.

  Loads an Expert and a Broker and starts to interrogate the Expert about what to do, and then send the requests to the broker.

- **Expert**: Contains the trading strategy.

   Receives knowledge from external sources like brokers and social media, to take a more or less intelligent (if at all) decision. 
   Planned experts for now are:

    - Wave rider bot
    - Social media sentiment bot
    - Expert copy bot

- **Broker**: Connects to an API to trade. 

  Exposes the basic operations like buy and sell, providing an abstraction from the API.
  Planned for now:
    - GDAX for Bitcoin and Ethereum
    - Binance for others
    - Some forex API
