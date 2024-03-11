import urequests
import time
import network

ssid = 'airuc-guest' # This should be ‘airuc-guest’ on campus Wi-Fi
def connect():
    # Connect to WLAN
    # Connect function from https://projects.raspberrypi.org/en/projects/get-started-pico-w/2
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid) # Remove password if using airuc-guest
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
try:
    connect()
except KeyboardInterrupt:
    machine.reset()
print("Connected.")

r = urequests.get("https://api.open-meteo.com/v1/forecast?latitude=51.0804&longitude=-114.1319&hourly=temperature_2m,rain,showers,snow_depth,cloud_cover&timezone=auto&forecast_days=1&forecast_hours=1")
# Most APIs will return JSON, which acts like a Python dictionary
def weather_stats():
    if r.status_code == 200:
        response_data = r.json()
        
        hourly_data = response_data.get("hourly", {})
        temperature_list = hourly_data.get("temperature_2m", [])
        rain_list = hourly_data.get("rain", [])
        showers_list = hourly_data.get("showers", [])
        snow_depth_list = hourly_data.get("snow_depth", [])
        cloud_cover_list = hourly_data.get("cloud_cover", [])
        
        return {"stat": f"Rain: {rain_list[0]} mm, Showers: {showers_list[0]} mm, Snow depth: {snow_depth_list[0] * 100} cm, Cloud Cover: {cloud_cover_list[0]}%", "temp": temperature_list}

    else:
        return (f"Error: Unable to fetch data. Status Code: {r.status_code}")

