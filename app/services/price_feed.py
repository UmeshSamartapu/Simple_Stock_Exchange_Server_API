import asyncio
import random

stock_prices = {"AAPL": 150.0, "GOOG": 2700.0, "TSLA": 600.0}
subscribers = set()

async def simulate_prices():
    while True:
        for stock in stock_prices:
            stock_prices[stock] += random.uniform(-1, 1)
            stock_prices[stock] = round(stock_prices[stock], 2)
        for ws in list(subscribers):
            try:
                await ws.send_json(stock_prices)
            except Exception:
                subscribers.remove(ws)
        await asyncio.sleep(2)
