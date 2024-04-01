import requests


def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data


def calculate_coziness(temperature, humidity, wind_speed, weather_condition):
    # 날씨 상태에 따라 포근함 가중치 설정
    weather_weight = {'Clear': 1, 'Clouds': 0.8, 'Rain': 0.5, 'Snow': 0.3, 'Mist': 0.7, 'Fog': 0.6}

    # 기온이 높을수록, 습도가 높을수록, 바람이 약할수록 포근함이 느껴진다고 가정
    coziness = (temperature * 0.6) + (humidity * 0.3) + ((10 - wind_speed) * 0.1)

    # 날씨 상태에 따른 가중치 적용
    if weather_condition in weather_weight:
        coziness *= weather_weight[weather_condition]

    return coziness


api_key = '6c856b2262f7a9c67c5fcff9b0196376'
city = ''

weather_data = get_weather(api_key, city)

if 'main' in weather_data and 'wind' in weather_data and 'weather' in weather_data:
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    weather_condition = weather_data['weather'][0]['main']

    coziness_index = calculate_coziness(temperature, humidity, wind_speed, weather_condition)
    print(f"The coziness index in {city} is {coziness_index}")
else:
    print("Failed to fetch weather data.")
