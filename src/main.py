import arbitrage

"""
    Step 0: Finding coins which can be traded
    Poloniex Exchange
    https://docs.legacy.poloniex.com/
"""


def step_0():
    # Extract coins from exchange
    url = "https://poloniex.com/public?command=returnTicker"
    coins_json = arbitrage.get_coin_tickers(url)

    # Find the tradeable coins
    coins_list = arbitrage.collect_tradeable_coins(coins_json)

    return coins_list


"""
    Step 1: Structuring Triangular pairs
    Calculation only
"""


def step_1(coin_list):
    arbitrage.structure_triangular_arbitrage(coin_list)


if __name__ == "__main__":
    coin_list = step_0()
    structured_pairs = step_1()
