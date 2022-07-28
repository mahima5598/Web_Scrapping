### Web_Scrapping

##### This repository has python files that fetch data from SolarVu Inverter and Weathertrak web pages.Further, the data is sent to InfluxDB 2.x version.(This can be monitored on the Influx Web UI)

###### Web_Scrapper_Inverter.py - It fetches data from the following link : http://www.solarvu.net/green/solarvu/performSInverter.php?ac=101948 
##### Web_Scrapper_Weather.py - It fetches data during the daylight time from the following link: http://www.solarvu.net/green/solarvu/performWeatherTrak.php?ac=101948&wt=1

#### Note: All the data gets converted to float to make data handling easier.

