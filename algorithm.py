import alpaca_trade_api as tradeapi
import random
import sys
sys.path.append('../')

from config import API_KEY, API_SECRET_KEY, BASE_URL

def submit_random_order():
    # Initialize the API with your credentials
    api = tradeapi.REST(key_id=API_KEY, secret_key=API_SECRET_KEY, base_url=BASE_URL, api_version='v2')
    active_assets = api.list_assets(status='active', asset_class = 'us_equity')

    # Select a random asset
    selected_asset = random.choice(active_assets)

    # Print account details
    order = api.submit_order(
        symbol=selected_asset.symbol,
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'  # Good till cancel
    )

    print(order)

    return order

submit_random_order()