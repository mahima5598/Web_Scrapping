#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
from bs4.element import Comment
from influxdb_client import InfluxDBClient, Point, WriteOptions
import numpy as np
import influxdb_client
import json
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

while True:

	def tag_visible(element):
	    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
		return False
	    if isinstance(element, Comment):
		return False
	    return True


	def text_from_html(body):
	    soup = BeautifulSoup(body, 'html.parser')
	    texts = soup.findAll(text=True)
	    visible_texts = filter(tag_visible, texts)  
	    return u" ".join(t.strip() for t in visible_texts)

	html = urllib.request.urlopen('http://www.solarvu.net/green/solarvu/performWeatherTrak.php?ac=101948&wt=1').read()
	Weather_data=text_from_html(html)
	#print(Weather_data)


	def convert_to_json(Weather_data):
		
		
		Weather_raw = Weather_data.split()
		#print(Weather_raw)

		remove_comma =[i.replace(',','') if ',' in i else i for i in Weather_raw]
		#print(remove_comma)
		Weather_datavalue = []
		for num in remove_comma:
			try:
				if '.' in num:
					Weather_datavalue.append(float(num))
				elif num.isdigit():
					Weather_datavalue.append(float(num))
				else:
					None
			except:
				
				None
			
		print(Weather_datavalue)
	#At night most values turn to N/A, the program is not efficient enough to input N/A i.e. string and integer paralelly to InfluxDB
		Weather_values = {}	
		while (Weather_datavalue[2] != 0.0)
			Weather_values = {
				"Solar_Irradiance": Weather_datavalue[2],
				"Peak_Solar_Irradiance" : Weather_datavalue[3],
				"Insolation": Weather_datavalue[4],
				"Full_Sun_Hours": Weather_datavalue[5],
				"Ambient_temperature" : Weather_datavalue[6],
				"Peak_Ambient_Temperature": Weather_datavalue[7],
				"Panel_temperature" : Weather_datavalue[8],
				"Peak_Panel_Temperature": Weather_datavalue[9],
				"Peak_Irradiance" : Weather_datavalue[10],
				"Max_Insolation": Weather_datavalue[11],
				"Max_Ambient_temperature" : Weather_datavalue[12],
				"Min_Ambient_Temperature": Weather_datavalue[13],
				"Max_Panel_temperature" : Weather_datavalue[14],
				"Min_Panel_Temperature": Weather_datavalue[15],
				"DC_Input_Capacity": Weather_datavalue[16],
				"AC_Output_Capacity" : Weather_datavalue[17]
				}
		return json.dumps(Weather_values)

	Weather = convert_to_json(Weather_data)
	Json_Weather = json.loads(Weather)

	print(Json_Weather)
	
	try:
		# You can generate an API token from the "API Tokens Tab" in the UI
		token = "UQ9CBHaU8JXRxx8Qwp9YVR_7yjE-kNnju_YtcCwBO27QAsqmnqeJxrU0fnoStTA4iOyiMM9qZv0qH9pjrwP_nA=="
		org = "Volpow"
		bucket = "Client_lib_test"

		client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

		write_api = client.write_api(write_options=SYNCHRONOUS)

		p = (
			influxdb_client.Point("Weather_test3")
			.tag("SolarVu_Weather","SolarVu_Weather")
			.field("Solar_Irradiance", Json_Weather["Solar_Irradiance"])
			.field("Peak_Solar_Irradiance", Json_Weather["Peak_Solar_Irradiance"])
			.field("Insolation", Json_Weather["Insolation"])
			.field("Full_Sun_Hours", Json_Weather["Full_Sun_Hours"])
			.field("Ambient_temperature", Json_Weather["Ambient_temperature"])
			.field("Peak_Ambient_Temperature", int(Json_Weather	["Peak_Ambient_Temperature"]))
			.field("Panel_temperature", Json_Weather["Panel_temperature"])
			.field("Peak_Panel_Temperature", Json_Weather["Peak_Panel_Temperature"])
			.field("Peak_Irradiance", Json_Weather["Peak_Irradiance"])
			.field("Max_Insolation", Json_Weather["Max_Insolation"])
			.field("Max_Ambient_temperature", Json_Weather["Max_Ambient_temperature"])
			.field("Min_Ambient_Temperature", Json_Weather["Min_Ambient_Temperature"])
			.field("Max_Panel_temperature", Json_Weather["Max_Panel_temperature"])
			.field("DC_Input_Capacity", Json_Weather["DC_Input_Capacity"])
			.field("AC_Output_Capacity", Json_Weather["AC_Output_Capacity"])
					        
		)	
	     
		write_api.write(bucket, org, record=p)

		query = 'from(bucket: "Client_lib_test") |> range(start: -1h)'
		tables = client.query_api().query(query, org=org)

		for table in tables:
		    for record in table.records:
			print(record)

		client.close()
	except:
		None
	time.sleep(600)

