import schedule
import time
import algorithm

def job():
    print("Submitting a random order...")
    try:
        order = algorithm.submit_random_order()
        print("Order submitted:", order)
    except Exception as e:
        print("An error occurred:", e)

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)