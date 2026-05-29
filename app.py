import streamlit as st
import requests
st.title("REALTIME WEATHER APP")
city = st.text_input("Enter city Name :")
if st.button("Get Weather"):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data=response.json()
        current = data["current_condition"][0]
        temp = current["temp_C"]
        humidity = current["humidity"]
        weather = current["weatherDesc"][0]["value"]
        feels_like =current["FeelsLikeC"]
        wind_speed=current["windspeedKmph"]
        st.success(f"Weather of {city}")
        
        col1,col2 =st.columns(2)
        with col1:
            st.metric("Temperature ", f"{temp} c")
            st.metric("Humidity",f"{humidity}%")
            
        with col2:
            st.metric("Feels Like ",f"{feels_like}c")
            st.metric("Wind Speed ",f"{wind_speed} km/h")
            
        st.write(f"Weather Condition ; {weather}")
        if int(temp)> 35:
            st.warning("Too Hot outside")
        elif int(temp) < 20 :
            st.info("Weather is cold")
        else:
            st.success("Weather looks nice today s")

    except Exception as e :
        st.error("Something went Wrong")
        