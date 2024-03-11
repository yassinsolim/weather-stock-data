import urequests
import time
import network
import json

ssid = '(YOUR NETWORK)' # Replace (YOUR NETWORK) with your local wifi
Password = '(YOUR PASSWORD)' # Replace (YOUR PASSWORD) with your local wifi's password

def connect():
    # Connect to WLAN
    # Connect function from https://projects.raspberrypi.org/en/projects/get-started-pico-w/2
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
try:
    connect()
except KeyboardInterrupt:
    machine.reset()
print("Connected.")

def get_stock_change(url):
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                last_record = data[0]
                stock_data = f"Close: {last_record['close']} Open: {last_record['open']} High: {last_record['high']} Low: {last_record['low']}"
                open_price = last_record.get('adjOpen', 0)
                close_price = last_record.get('adjClose', 0)
                percentage_change = ((close_price - open_price) / open_price) * 100
                return {"percent": percentage_change, "data": stock_data}
            else:
                print("No data available.")
        else:
            print("Failed to fetch data, status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))
    print(stock_data)
    return 0.0  # Return 0.0 if there's an error or no data
