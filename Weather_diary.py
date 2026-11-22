import requests
import json


def getParams(city="Москва"):
    params = {
        "q": city,
        "appid": "f31276ae6f2a23242f06dbf7ba0e021a",
        "units": "metric",
        "lang": "ru",
    }
    return params


def save_weather(response, history):

    if response.status_code == 200:
        data = response.json()
        history.append(
            {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "pressure": data["main"]["pressure"],
            }
        )
        with open("weather_history.json", "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    return history


def printHistory(history):
    for i in history:
        print(f"Город {i['city']}, температура {i['temp']}, давление {i['pressure']}")


def main():
    try:
        with open("weather_history.json", "r", encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    while True:
        print("1 - Записать погоду")
        print("2 - Посмотреть историю")
        print("3 - Выйти")
        try:
            num = int(input("Введите число: "))
            if num == 1:
                city = input("Введите название города ")
                city = city[0].strip().upper() + city[1:]
                response = requests.get(
                    "https://api.openweathermap.org/data/2.5/weather",
                    params=getParams(city),
                )
                history = save_weather(response, history)
            elif num == 2:
                printHistory(history)
            elif num == 3:
                break
        except ValueError:
            print("Введено не число")
            continue


main()
