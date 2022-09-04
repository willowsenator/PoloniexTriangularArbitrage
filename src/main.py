"""
    Step 0: Finding coins which can be traded
    Poloniex Exchange
    https://docs.legacy.poloniex.com/
"""
import arbitrage


def step_0():
    # Extract coins from exchange
    url = "https://poloniex.com/public?command=returnTicker"
    coins_json = arbitrage.get_coin_tickers(url)

    # Find the tradeable coins
    coins_list = arbitrage.collect_tradeable_coins(coins_json)

    return coins_list


if __name__ == "__main__":
    coin_list = step_0()
    print(coin_list)
