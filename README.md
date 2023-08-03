# Weather API Fetch Data Based on Location

### 1. Imports necessary Python modules:
###### --- requests: to make HTTP requests to the OpenWeatherMap API.
###### --- os: to interact with the OS, in this case, it is no longer used as the API key is now directly placed in the script.
###### --- datetime: to work with dates and times.

### 2. Sets the user_api variable:
###### --- This variable is the OpenWeatherMap API key which is needed to authenticate your requests to the OpenWeatherMap API.

### 3. Prompts the user to input a city name:
###### --- The input() function is used to get input from the user which is stored in the location variable.

### 4. Constructs the API URL:
###### --- The location variable and user_api variable are concatenated with the base URL of the OpenWeatherMap API to form complete_api_link, which is the complete API URL.

### 5. Sends a GET request to the API:
###### --- The requests.get() function is used to send a GET request to the API URL. The response from the API is stored in api_link.
Converts the API response to JSON:
###### --- The json() method is used on api_link to convert the API response into a Python dictionary, which is stored in api_data.

### 6. Checks if the city entered is valid:
###### --- If the 'cod' field in api_data is '404', this means the API could not find the city, so an error message is printed. If 'cod' is not '404', the script continues to extract the weather data.

### 7. Extracts the weather data:
###### --- The script extracts the temperature, weather description, humidity, and wind speed from api_data. The temperature is converted from Kelvin to Celsius. The current date and time is also stored.

### 8. Prints the weather data:
###### --- The extracted weather data and current date/time is printed to the console. The city name is converted to upper case for display.

![output](https://github.com/Bhuvneshjai/Weather-API-Fetch-Data/assets/82877515/fc5f02f7-3bc4-457e-9a69-4689b573a385)
