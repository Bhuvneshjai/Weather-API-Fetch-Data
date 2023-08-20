# Weather API Fetch Data Based on Location

### Imports:
* import requests
* from datetime import datetime

* requests: A library for making HTTP requests. It's used to fetch data from the provided API.
* datetime: A module for working with dates and times. Used to handle and format date-time related information.

### Fetching Data from the API:
* def fetch_data_from_api():
*     ...
*     return api_link.json()
* This function gets data from the given API and returns the response as a JSON format.

### Extract Weather Data:
* def get_weather_data(api_data, date_time, attribute):
*     ...
*     return None
* This function processes the data fetched from the API to extract specific weather information based on the provided date-time and attribute (temperature, wind speed, or pressure).
* It loops through the list of weather data and checks for a matching date-time. If found, it retrieves the desired attribute.

### Main Interaction Loop:
* def main():
*     ...
* This function implements the main interaction loop, which repeatedly presents options to the user until they decide to exit.

* Fetches the weather data from the API initially.
* Presents a menu to the user with options to retrieve temperature, wind speed, pressure, or exit.
* Reads the user's choice and processes it:
* For choices 1, 2, and 3, it prompts the user for a date-time input.
* It then fetches the corresponding weather data and displays it.
* If no data is found for the given date-time, it informs the user.
* If the user chooses 0, it exits the program.
* Any other choice is treated as invalid, and the user is notified.

### Entry Point of the Script:
* if __name__ == "__main__":
*     main()

* This condition ensures that the main() function (our interaction loop) is executed only when the script is run directly, not when it's * imported as a module into another script.
* In essence, this script provides a simple command-line interface that lets users fetch specific weather attributes (temperature, wind speed, or pressure) for a particular date-time for London, based on data from the OpenWeatherMap API.

![output](https://github.com/Bhuvneshjai/Weather-API-Fetch-Data/assets/82877515/fc5f02f7-3bc4-457e-9a69-4689b573a385)
