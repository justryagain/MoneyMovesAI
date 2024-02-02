from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PK7SH0BR08VROD2LH39F"
API_SECRET = ""
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MMStrat(Strategy):
    
    def initialize(self, symbol: str = "LEN"):
       self.symbol = symbol
       self.sleep = "24H"
       self.last_trade = None

    def on_trading_iteration(self):
       if self.last_trade == None:
           order = self.create_order(
               self.symbol,
               5,
               "buy",
               type="market"
           )
           self.submit_order(order)
           self.last_trade = "buy"

start_date = datetime(2024,1,1)
end_date = datetime(2024,1,31)
broker = Alpaca(ALPACA_CREDS)
strategy = MMStrat(name='triplemstrat', broker=broker,
                   parameters={"symbol":"LEN"})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={}
    )

