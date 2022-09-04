import requests


# Get list of coins and prices
def get_coin_tickers(url):
    req = requests.get(url)
    return req.json()


# Find the tradeable coins
def collect_tradeable_coins(coins_json):
    coins_list = []
    for coin in coins_json:
        is_frozen = coins_json[coin]['isFrozen']
        post_only = coins_json[coin]['postOnly']

        if is_frozen == "0" and post_only == "0":
            coins_list.append(coin)
    return coins_list


# Structure Arbitrage pairs
def structure_triangular_arbitrage(coin_list):
    triangular_pair_list = []
    remove_duplicates_list = []
    pairs_list = []

    # Pair A
    for pair_a in coin_list:
        pair_a_split = pair_a.split('_')
        a_base = pair_a_split[0]
        a_quote = pair_a_split[1]

        # Assign A to a box
        a_pair_box = [a_base, a_quote]

        # Pair B
        for pair_b in coin_list:
            pair_b_split = pair_b.split('_')
            b_base = pair_b_split[0]
            b_quote = pair_b_split[1]
            if pair_b != pair_a:
                if b_base in a_pair_box or b_quote in a_pair_box:
                    pass
