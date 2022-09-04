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
        print(a_base, a_quote)
