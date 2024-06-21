from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
import os
import sqlite3
from dotenv import load_dotenv
from datetime import datetime
from dataclasses import dataclass

# import requests

city_list = [
  "Cumbria",
  "Corfe Castle",
  "The Cotswolds",
  "Cambridge",
  "Bristol",
  "Oxford",
  "Norwich",
  "Stonehenge",
  "Watergate Bay",
  "Birmingham"
]

load_dotenv()

@dataclass
class MinMaxTemperature:
    date: str
    max: float
    min: float

class WeatherInCityAdapter(LogicAdapter):
  
    def __init__(self, chatbot):
        super().__init__(chatbot)
        self.city_list = city_list

    def can_process(self, statement) -> bool:
        # Check if the statement includes "what is the weather in"
        if hasattr(statement, 'text'):
          statement = statement.text
        can_process = "weather in" in statement.lower() or "temperature in" in statement.lower()

        return can_process

    def process(self, statement, additional_response_selection_parameters) -> Statement:
        # Extract the city name from the statement
        if hasattr(statement, 'text'):
            statement = statement.text
        
        if "temperature in" in statement.lower():
            city_name = statement.lower().split("temperature in")[-1].strip().split("?")[0]
        else:
            city_name = statement.lower().split("weather in")[-1].strip().split("?")[0]

        self.db = WeatherDB()

        self.db.populateWeatherForCityIfLessThanFiveRecords(city_name)

        # check if the city has a recent record in the database
        data = self.db.getNextWeatherRecordForCity(city_name)
        if data is None:
            exists = self.db.isCityInDB(city_name)
            city_found = True

            if not exists:
                city_found = self.db.populateDBWithCityData(city_name)
            
            if city_found:
              self.db.getWeatherForCity(city_name)
              data = self.db.getNextWeatherRecordForCity(city_name)
        
        future_data_table = ""
        future_data = self.db.getMinMaxTemperatureForCity(city_name)
        if future_data is not None:
            future_data_table += "The next few days will be:<br />"
            for day in future_data:
                future_data_table += f"Date: {day[0]} - Max: {str(day[1])} - Min: {str(day[2])}<br />"
        if data is None:
            response_statement = Statement(text = f"Sorry, information for {city_name} is not available.")
            response_statement.confidence = 0.1
            return response_statement
    
        date, desc, min, max, cloud_cover, humidity, pressure, precipitation, wind  = data
        response_statement = Statement(text = f"The weather in {city_name} is {desc} with a temperature of {max}°C. Cloud cover is {cloud_cover}%. Rainfall is {precipitation} mm. Wind is {wind} m/s. Pressure is {pressure} hPa. Humidity is {humidity}%. {future_data_table}")
        response_statement.confidence = 1




        # if city_name in [city.lower() for city in self.city_list]:

        #     data = self.getCityWeather(city_name)
            
        #     if data['cod'] == 200:
        #         response_statement = Statement(text = f"The weather in {city_name} is {data['weather'][0]['description']} with a high of {data['main']['temp_max']}°C and a low of {data['main']['temp_min']}°C.")
        #         response_statement.confidence = 1
        #     else:
        #         response_statement = Statement(text = f"Sorry, I cannot access real-time information for {city_name}.")
        #         response_statement.confidence = 0.1
        # else:
        #     # get the data for the city
        #     self.db.populateDBWithCityData(city_name)
        #     self.db.getWeatherForCity(city_name)


        #     response_statement = Statement(text = f"Sorry, information for {city_name} is not available.")
        #     response_statement.confidence = 0.1
            
        return response_statement
  
    # def getCityWeather(self, city):
    #     response = requests.get(base_url, params={"q": city, "appid": weather_api_key, "units":"metric"})
    #     return response.json()

class WeatherDB():
    def __init__(self):
        self._city_list = city_list
        self.con = sqlite3.connect("db.sqlite3")
        self.cur = self.con.cursor()
    
    def city_list(self):
        return self._city_list

    def populateDBWithCityData(self, city: str) -> bool:
        print('Getting lat/lon for ' + city)
        lat, lon = self.getCityLatLonFromAPI(city)
        if lat is None or lon is None:
            return False
        self.cur.execute("INSERT INTO city (name, lat, lon) VALUES (?, ?, ?)", (city, lat, lon))
        self.con.commit()
        return True
    
    def isCityInDB(self, city: str) -> bool:
        res = self.cur.execute("SELECT name FROM city WHERE name = ?", (city,)).fetchone()
        if res is None:
            return False
        else:
            return True
    
    def getCityLatLonFromAPI(self, city: str):
        import requests
        url = "https://nominatim.openstreetmap.org/search.php?q={city}&format=jsonv2"
        r = requests.get(url.format(city=city), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0 PythonApp-UniAssign-COS60016-02'})

        if r.status_code == 200:
            if len(r.json()) == 0:
                return None, None
            return r.json()[0]["lat"], r.json()[0]["lon"]
        else:
            return None, None
    
    def getCityWeatherFromAPI(self, lat, lon):
        import requests
        api_key = os.getenv('OPENWEATHERMAP_APIKEY')
        weather_url = "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric"
        r = requests.get(weather_url.format(lat=lat, lon=lon, API_key=api_key))
        return r.json()
    
    def validateWeatherData(self, data) -> tuple:
        date = data["dt_txt"]
        desc = data["weather"][0]["description"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        if "clouds" in data:
          cloud_cover = data["clouds"]["all"]
        else:
          cloud_cover = 0
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        if "rain" in data:
          precipitation = data["rain"]["3h"]
        else:
          precipitation = 0
        if "wind" in data:
          wind = data["wind"]["speed"]
        else:
          wind = 0
        return date, desc, temp_min, temp_max, cloud_cover, humidity, pressure, precipitation, wind
    
    def getWeatherForCity(self, city: str) -> None:
        print("Recalling lat/lon for " + city + " from database")
        res = self.cur.execute("SELECT lat, lon FROM city WHERE lower(name) = ?", (city,)).fetchone()
        
        if res is None:
            print("Failed to get lat/lon for " + city)
            return

        lat, lon = res[0], res[1]
        print("Requesting weather for " + city + " - Lat: " + str(lat) + " Lon: " + str(lon))
        
        weather = self.getCityWeatherFromAPI(lat, lon)

        if weather["cod"] == "200":
            for day in weather["list"]:
                date, desc, temp_min, temp_max, cloud_cover, humidity, pressure, precipitation, wind = self.validateWeatherData(day)
                self.cur.execute("INSERT INTO weather_forecast (city, date, desc, min, max, cloud_cover, humidity, pressure, precipitation, wind) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                    city, date, desc, temp_min, temp_max, cloud_cover, humidity, pressure, precipitation, wind))
            self.con.commit()

        else:
            print("Failed to get weather for " + city)

    def getNextWeatherRecordForCity(self, city: str):
        from datetime import timedelta
        now = datetime.now()
        lpad = lambda x, y: str(x).zfill(y)
        date_time = now.strftime("%Y-%m-%d") + " " + lpad(str(now.hour - (now.hour % 3)),2) + ":00:00"
        future_datetime = datetime.fromisoformat(date_time) + timedelta(hours=3)
        res = self.cur.execute("SELECT date, desc, CAST(min as integer), CAST(max as integer), cloud_cover, humidity, pressure, precipitation, wind FROM weather_forecast WHERE city = ? AND date = ?", (city, future_datetime.strftime("%Y-%m-%d %H:%M:%S"))).fetchone()

        if res is None:
            return None
        
        date, desc, min, max, cloud_cover, humidity, pressure, precipitation, wind = res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8] 
        return date, desc, min, max, cloud_cover, humidity, pressure, precipitation, wind
    
    def numberOfFutureWeatherRecordsForCity(self, city: str):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d")
        return self.cur.execute("SELECT COUNT(*) FROM weather_forecast WHERE city = ? AND date(`date`) >= ? GROUP BY date(`date`)", (city, date_time, )).fetchone()[0]

    def populateWeatherForCityIfLessThanFiveRecords(self, city: str):
        if self.numberOfFutureWeatherRecordsForCity(city) < 5:
            print("Less than 5 records - getting more weather data")
            self.getWeatherForCity(city)

    def getMinMaxTemperatureForCity(self, city: str) -> 'list[MinMaxTemperature]':
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d")
        res = self.cur.execute("SELECT date(`date`), CAST(MAX(`max`) as integer), CAST(MIN(`min`) as integer) FROM `weather_forecast` WHERE `city` LIKE ? AND date(`date`) >= ? GROUP BY date(`date`) LIMIT 0,5", (city,date_time,)).fetchall()

        if res is None:
            return None
        
        return res    
    

