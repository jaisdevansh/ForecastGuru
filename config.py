import pyttsx3
import datetime

import requests
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)
engine.setProperty('volume',10.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def day():
        now = datetime.datetime.now().weekday()
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_name = days[now]
        speak(f"Today day  is {day_name}")
        print(day_name)
#        

def wishMe():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    current_date = datetime.datetime.now().date()
    

    
    
    if hour>=0 and hour<12:
        speak("Good Morning sir !")
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good evening sir!")  
    speak(f"Today date is {current_date}")
    print(current_date)
    #speak(f"Today is {day_name}")
    day()
    
    speak(f"the time is {hour%12} o clock")
    print(hour%12)
    speak(f"and{minute}minute")
    print(minute)       
    
def get_weather(city, api_key):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        print(f"City: {data['name']}")
        speak(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        speak(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        speak(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description'].capitalize()}")
        speak(f"Weather: {weather['description'].capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")
        speak(f"Wind Speed: {wind['speed']} meter per second")
        print ("thankyou")
        speak("thank you")
    else:
        print("City not found or API request failed.")
        speak("City not found ...")

def main():
    api_key = '6ecc274e99616f35408f89dbf5509dd9'
      # Replace with your OpenWeatherMap API key
    wishMe()  
    speak("enter your city name and country name")
    city = input("Enter the city name and countryname : ")
   
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
    