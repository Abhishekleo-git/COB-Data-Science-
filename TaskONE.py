import pandas as pd
import requests
def get_weather_data(api_key, city):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {city}. Status Code: {response.status_code}")
        return None
def extract_weather_info(weather_data):
    if weather_data and 'main' in weather_data and 'wind' in weather_data:
        return {
            'Temperature (Celsius)': weather_data['main'].get('temp'),
            'Humidity (%)': weather_data['main'].get('humidity'),
            'Wind Speed (m/s)': weather_data['wind'].get('speed')
        }
    else:
        print(f"Error: Invalid data structure in API response.")
        return None
def save_to_csv(data, filename='DELHI_Weather_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}:\n{df}')
def main():
    api_key = 'f1625345f4190f892f4226a27b4138bd'
    city = 'DELHI'  # You can change the city as needed

    weather_data = get_weather_data(api_key, city)

    if weather_data:
        extracted_data = extract_weather_info(weather_data)
        if extracted_data:
            save_to_csv({'City': [city], **extracted_data})
if __name__ == "__main__":
    main()
