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
