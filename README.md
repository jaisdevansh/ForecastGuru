# ForecastGuru
Project Description:

ForecastGuru is an innovative weather forecasting application designed to provide real-time weather updates with the added convenience of spoken alerts. This project leverages the OpenWeatherMap API to fetch current weather data for a specified city and uses the pyttsx3 library to convert the weather information into speech. This ensures users can receive up-to-date weather details, including temperature, humidity, and wind speed, through both text and voice.

Key Features:
Real-Time Weather Data:

The application retrieves live weather data from the OpenWeatherMap API, providing users with the most accurate and current weather information for their selected city.
Comprehensive Weather Reports:

ForecastGuru offers detailed weather reports that include the city name, current temperature in degrees Celsius, humidity percentage, a brief weather description, and wind speed in meters per second.
Text-to-Speech Functionality:

Utilizing the pyttsx3 text-to-speech library, ForecastGuru reads the weather report aloud, making it accessible for users who prefer audio updates or have visual impairments.
User-Friendly Interface:

The application prompts users to input their city name, making it straightforward and easy to use for people of all ages and technical backgrounds.
How It Works:
User Input:

The user is prompted to enter the name of the city for which they want to receive the weather forecast.
Data Retrieval:

ForecastGuru constructs an API request URL using the user-provided city name and an API key for the OpenWeatherMap service.
It sends a GET request to the OpenWeatherMap API and processes the JSON response to extract necessary weather details.
Weather Report Generation:

The application formats the extracted data into a readable weather report string, detailing the city's weather conditions.
Text-to-Speech Conversion:

The weather report string is passed to the pyttsx3 engine, which converts the text into spoken words and reads it aloud to the user.
Output:

The weather report is displayed on the screen and simultaneously spoken, ensuring the user receives the information in both visual and auditory for
