import requests
try:
    city=input("Enter your City Name : ")
    url=f"https://wttr.in/{city}?format=j1"
    response=requests.get(url)
    data=response.json()
    print(data)
    current = data["current_condition"][0]

    temp = current["temp_C"]

    weather = current["weatherDesc"][0]["value"]

    humidity = current["humidity"]
    print(f"""
    City: {city}
    Temperature: {temp}°C
    
    Weather: {weather}
    Humidity: {humidity}%
    """)
except:
    print('something went wrong ')