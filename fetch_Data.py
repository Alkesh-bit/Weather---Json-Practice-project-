import requests


def get_weather(city):

    try:

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]

        weather = current["weatherDesc"][0]["value"]

        humidity = current["humidity"]

        print(f"""City: {city}
             Temperature: {temp}°C
             Weather: {weather}

             Humidity: {humidity}%
""")

    except Exception as e:

        print("Error:", e)


while True:

    city = input("Enter city name (or exit): ")

    if city.lower() == "exit":

        print("Goodbye 😄")

        break

    get_weather(city)