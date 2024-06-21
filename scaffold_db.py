import sqlite3
from ChatterbotAdapters.weather import WeatherDB

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS city")
cur.execute("CREATE TABLE city(city_id INTEGER PRIMARY KEY, name TEXT NOT NULL, lat REAL, lon REAL)")
cur.execute("DROP TABLE IF EXISTS weather_forecast")
cur.execute("CREATE TABLE weather_forecast(forcast_id INTEGER PRIMARY KEY,city, date, desc, min, max, cloud_cover, humidity, pressure, precipitation, wind, UNIQUE(city, date) ON CONFLICT REPLACE)")

db = WeatherDB()
city_list = db.city_list()

for city in city_list:
    city = city.lower()
    db.populateDBWithCityData(city)
    db.getWeatherForCity(city)
con.close()