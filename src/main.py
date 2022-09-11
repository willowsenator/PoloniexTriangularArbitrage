import json
import time

import arbitrage

coin_price_url = "https://poloniex.com/public?command=returnTicker"
json_file_path = "structured_triangular_pairs.json"

"""
    Step 0: Finding coins which can be traded
    Poloniex Exchange
    https://docs.legacy.poloniex.com/
"""


def step_0():
    # Extract coins from exchange
    coins_json = arbitrage.get_coin_tickers(coin_price_url)

    # Find the tradeable coins
    coins_list = arbitrage.collect_tradeable_coins(coins_json)

    return coins_list


"""
    Step 1: Structuring Triangular pairs
    Calculation only
"""


def step_1(coin_list):
    structured_list = arbitrage.structure_triangular_arbitrage(coin_list)

    # Save structure list to JSON
    with open(json_file_path, "w") as file:
        json.dump(structured_list, file)


"""
    Step 2: Calculate Surface Arbitrage Opportunities
"""


def step_2():
    # Get Structured pairs
    with open(json_file_path) as json_file:
        structured_pairs = json.load(json_file)
    # Get Latest Surface Prices
    prices_json = arbitrage.get_coin_tickers(coin_price_url)

    # Structure price Info
    for t_pair in structured_pairs:
        time.sleep(0.3)
        prices_dict = arbitrage.get_price_for_t_pair(t_pair, prices_json)
        surface_arb = arbitrage.calc_triangular_arb_surface_rate(t_pair, prices_dict)
        if len(surface_arb) > 0:
            real_rate_arb = arbitrage.get_depth_from_orderbook(surface_arb)
            print(real_rate_arb)
            time.sleep(20)


if __name__ == "__main__":
    # coin_list = step_0()
    # step_1(coin_list)
    while True:
        step_2()
