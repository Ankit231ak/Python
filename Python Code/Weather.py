import requests

def weather(city):
    # Get a free API key from https://openweathermap.org/api
    api_key = "YOUR_API_KEY"  #  Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"🌤️ Weather in {city}: {weather}, {temp}°C")
    else:
        print("❌ City not found or error in API request.")

city = input("Enter city name: ")
weather(city)
