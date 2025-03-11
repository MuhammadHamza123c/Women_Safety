import requests
import time
import smtplib
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

ESP_IP = "ESP8266 IP ADRESS"
SENDER_EMAIL = "your_email@example.com"
APP_PASSWORD = "your_app_password"
LOCATIONIQ_API_KEY = "your_locationiq_api_key"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, APP_PASSWORD)

data = pd.read_csv("police_station_data.csv")
locations = data[['Latitude', 'Longitude']].to_numpy()
nbrs = NearestNeighbors(n_neighbors=1, metric='haversine').fit(np.radians(locations))

def get_location_name(lat, lon):
    url = f"https://us1.locationiq.com/v1/reverse.php?key={LOCATIONIQ_API_KEY}&lat={lat}&lon={lon}&format=json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json().get("display_name", "Unknown Location")
    except requests.exceptions.RequestException:
        return "Unknown Location"

while True:
    try:
        response = requests.get(ESP_IP, timeout=5)
        if response.status_code == 200:
            data_json = response.json()
            lat, lon = data_json['Latitude'], data_json['Longitude']
            distances, indices = nbrs.kneighbors(np.radians([[lat, lon]]))
            nearest_index = indices[0][0]
            nearest_station = data.iloc[nearest_index]['Police Station']
            receiver_email = data.iloc[nearest_index]['Email']
            place_name = get_location_name(lat, lon)
            subject = "EMERGENCY ALERT"
            body = f"""
            URGENT HELP NEEDED
            Current Location: {place_name}
            Nearest Police Station: {nearest_station} ({distances[0][0] * 6371:.2f} km away)
            """
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(SENDER_EMAIL, receiver_email, message)
            time.sleep(5)
    except requests.exceptions.RequestException:
        pass
    time.sleep(1)
