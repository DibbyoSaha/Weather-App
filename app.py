import requests

api_key = '18395fb8882b590090ce06f571744796'
user_input = input("Enter City: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)
if weather_data.json()['cod'] == '404':
    print("City not found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {round((temp-32)*(5/9))}°C")
