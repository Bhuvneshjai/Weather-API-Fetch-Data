import requests
from datetime import datetime

def fetch_data_from_api():
    api_key = 'b6907d289e10d714a6e88b30761fae22'  # Given API Key
    location = 'London,us'  # Given Location
    complete_api_link = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={location}&appid={api_key}"
    
    api_link = requests.get(complete_api_link)
    return api_link.json()

def get_weather_data(api_data, date_time, attribute):
    for entry in api_data['list']:
        if entry['dt_txt'] == date_time:
            if attribute == 'temp':
                return entry['main']['temp'] - 273.15  # Convert Kelvin to Celsius
            elif attribute == 'wind':
                return entry['wind']['speed']
            elif attribute == 'pressure':
                return entry['main']['pressure']
    return None

def main():
    api_data = fetch_data_from_api()
    
    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '0':
            break
        elif choice in ['1', '2', '3']:
            date_time = input("Enter the date and time in the format 'YYYY-MM-DD HH:00:00': ")

            if choice == '1':
                temp = get_weather_data(api_data, date_time, 'temp')
                if temp:
                    print(f"Temperature at {date_time}: {temp:.2f} deg C")
                else:
                    print(f"No data available for {date_time}")

            elif choice == '2':
                wind_speed = get_weather_data(api_data, date_time, 'wind')
                if wind_speed:
                    print(f"Wind Speed at {date_time}: {wind_speed} KMPH")
                else:
                    print(f"No data available for {date_time}")

            elif choice == '3':
                pressure = get_weather_data(api_data, date_time, 'pressure')
                if pressure:
                    print(f"Pressure at {date_time}: {pressure} hPa")
                else:
                    print(f"No data available for {date_time}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
