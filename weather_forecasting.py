import tkinter as tk
import requests
def get_weather(city):
    api_key = '15811823f2b648f8be7133621242304'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    data = response.json()
    return data
def display_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if 'error' in weather_data:
        weather_label.config(text="City not found. Please check the city name and try again.")
    else:
        condition = weather_data['current']['condition']['text']
        temperature_c = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        wind_kph = weather_data['current']['wind_kph']
        emojis = {
            'Sunny': '☀️',
            'Partly cloudy': '⛅',
            'Cloudy': '☁️',
            'Overcast': '☁️',
            'Mist': '🌫️',
            'Patchy rain possible': '🌦️',
            'Patchy snow possible': '🌨️',
            'Patchy sleet possible': '🌨️',
            'Patchy freezing drizzle possible': '🌨️',
            'Thundery outbreaks possible': '⛈️',
            'Blowing snow': '❄️',
            'Blizzard': '❄️',
            'Fog': '🌁',
            'Freezing fog': '🌁',
            'Patchy light drizzle': '🌦️',
            'Light drizzle': '🌧️',
            'Freezing drizzle': '🌧️❄️',
            'Heavy freezing drizzle': '🌧️❄️',
            'Patchy light rain': '🌦️',
            'Light rain': '🌧️',
            'Moderate rain at times': '🌧️',
            'Moderate rain': '🌧️',
            'Heavy rain at times': '🌧️',
            'Heavy rain': '🌧️',
            'Light freezing rain': '🌧️❄️',
            'Moderate or heavy freezing rain': '🌧️❄️',
            'Light sleet': '🌨️',
            'Moderate or heavy sleet': '🌨️',
            'Patchy light snow': '🌨️',
            'Light snow': '🌨️',
            'Patchy moderate snow': '🌨️',
            'Moderate snow': '🌨️',
            'Patchy heavy snow': '🌨️',
            'Heavy snow': '🌨️',
            'Ice pellets': '🌨️❄️',
            'Light rain shower': '🌧️☔',
            'Moderate or heavy rain shower': '🌧️☔',
            'Torrential rain shower': '🌧️☔',
            'Light sleet showers': '🌨️☔',
            'Moderate or heavy sleet showers': '🌨️☔',
            'Light snow showers': '🌨️☔',
            'Moderate or heavy snow showers': '🌨️☔',
            'Light showers of ice pellets': '🌨️☔❄️',
            'Moderate or heavy showers of ice pellets': '🌨️☔❄️',
            'Patchy light rain with thunder': '⛈️🌧️',
            'Moderate or heavy rain with thunder': '⛈️🌧️',
            'Patchy light snow with thunder': '⛈️🌨️',
            'Moderate or heavy snow with thunder': '⛈️🌨️'
        }
        emoji = emojis.get(condition, '')
        weather_info = f"Condition: {condition}{emoji}\nTemperature: {temperature_c}°C\nHumidity: {humidity}%\nWind Speed: {wind_kph} km/h"
        weather_label.config(text=weather_info)
root = tk.Tk()
root.title("Weather App")
frame = tk.Frame(root, width=100, height=100)
frame.pack_propagate(False)  
frame.pack(padx=50, pady=50)
city_entry = tk.Entry(frame)
city_entry.grid(row=0, column=0, columnspan=2)
weather_button = tk.Button(frame, text="Get Weather", command=display_weather)
weather_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))
weather_label = tk.Label(frame, text="", justify=tk.CENTER)
weather_label.grid(row=2, column=0, columnspan=2)
root.mainloop()
