import schedule
import time
import algorithm
import riskmanagement

def job():
    print("Submitting a random order...")
    try:
        order = algorithm.submit_random_order()
        print("Order submitted:", order)
        riskmanagement.sell_dropped_assets()
    except Exception as e:
        print("An error occurred:", e)

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
    print('pending')