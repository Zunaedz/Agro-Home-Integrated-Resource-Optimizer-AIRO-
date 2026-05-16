# main.py

from weather_data import WeatherData


def main():

    # ---------------- USER SETTINGS ---------------- #

    API_KEY = "YOUR_API_KEY"
    CITY = "Dhaka"

    # ---------------- CREATE OBJECT ---------------- #

    weather = WeatherData(API_KEY, CITY)

    # ---------------- GET WEATHER DATA ---------------- #

    temperature = weather.get_temperature()
    humidity = weather.get_humidity()
    condition = weather.get_weather_condition()

    # ---------------- DISPLAY OUTPUT ---------------- #

    print("\n====== AIRO WEATHER SYSTEM ======\n")

    print(f"City: {CITY}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Condition: {condition}")

    print("\n=================================\n")


# ---------------- RUN PROGRAM ---------------- #

if __name__ == "__main__":
    main()