### Web_Scrapping

##### This repository has python files that fetch data from SolarVu Inverter and Weathertrak web pages. Further, the data is sent to InfluxDB v2.3.0(WebUI Credentials: login id=Volpow, password=Volpow@dmin123).This can be monitored on the Influx Web UI at the location "localhost:8087" in the bucket "Webscrapper", measurements "Inverter"or ("Weather") > "SolarVu_data". 

##### Web_Scrapper_Inverter.py/ Webscrapper_test_inverter.py - It fetches data from the following link : http://www.solarvu.net/green/solarvu/performSInverter.php?ac=101948 
##### Web_Scrapper_Weather.py/ Webscrapper_test.py - It fetches data during the daylight time from the following link: http://www.solarvu.net/green/solarvu/performWeatherTrak.php?ac=101948&wt=1

#### The above files are in MO_VP_UBTU_test. 

#### Note: All the data gets converted to float to make data handling easier.

