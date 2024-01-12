import pandas as pd
import requests

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=57&lon=4"


headers = {
    'User-Agent': 'Python'
}

request = requests.get(url, headers=headers)

data =  pd.DataFrame(pd.json_normalize(request.json()['properties']['timeseries']))
print(data)

data.to_csv(f"data/{pd.to_datetime('now', utc=True).strftime('%Y-%m-%d')}_weather_forecast.csv")



