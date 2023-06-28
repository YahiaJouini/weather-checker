import requests
import datetime
#getting the location
try:
    city=input("What city do you live in : ")
    key='aa6a2250b1d83fd114cfa3f99ee54a6b'
    cordinates_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
    r=requests.get(cordinates_url)
    if r.status_code == 200:
        now=datetime.datetime.now()
        r=r.json()
        print(f"Today's date is  {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Current weather state : {r['weather'][0]['main']},{r['weather'][0]['description']}")
        #converts the temperature from kelvin to celsius
        temperature=r['main']['temp']-273.15
        print(f"Current temperature : {round(temperature,2)}°C")
    else:
        print('City not found')
except:
    print('please connect to the internet!')