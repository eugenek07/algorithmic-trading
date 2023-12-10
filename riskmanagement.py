import alpaca_trade_api as tradeapi
import sys
sys.path.append('../')

from config import API_KEY, API_SECRET_KEY, BASE_URL

def calculate_original_price(api, symbol):
    # Fetch orders for the given symbol
    orders = api.list_orders(status='all', direction='asc')
    total_cost = 0
    total_shares = 0

    for order in orders:
        if order.symbol == symbol and order.side == 'buy':
            total_cost += float(order.filled_avg_price) * float(order.qty)
            total_shares += float(order.qty)

    if total_shares > 0:
        return total_cost / total_shares  # Return weighted average price
    else:
        return None

def sell_dropped_assets(threshold=0.10):
    # Fetch current positions
    api = tradeapi.REST(key_id=API_KEY, secret_key=API_SECRET_KEY, base_url=BASE_URL, api_version='v2')
    positions = api.list_positions()

    for position in positions:
        original_price = calculate_original_price(api, position.symbol)
        if original_price is None:
            continue  # Skip if no purchase history is found

        current_price = float(position.current_price)
        quantity = int(position.qty)

        # Calculate the percentage drop
        price_drop = (original_price - current_price) / original_price

        if price_drop >= threshold:
            # If the drop is 10% or more, sell the asset
            print(f"Selling {quantity} shares of {position.symbol} due to a drop of {price_drop*100}%")
            api.submit_order(
                symbol=position.symbol,
                qty=quantity,
                side='sell',
                type='market',
                time_in_force='gtc'
            )

sell_dropped_assets()