#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
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

html = urllib.request.urlopen('http://www.solarvu.net/green/solarvu/performSInverter.php?ac=101948').read()
Inverter_data=text_from_html(html)
print(Inverter_data)

def convert_to_json(Inverter_data):

	Inverter_datavalue = [
	int(float(Inverter_data)) if '.' in Inverter_data else (int(Inverter_data) if ',' in Inverter_data else int(Inverter_data)) for Inverter_data in re.findall(r'-?\d+\.?\d*',Inverter_data) ]	
		
	#Weather_raw = Weather_data.split()
	#print(Weather_raw)

	#remove_comma =[i.replace(',','') if ',' in i else i for i in Weather_raw]
	#print(remove_comma)
	#Weather_datavalue = []
	#for num in remove_comma:
	#	try:
	#		if '.' in num:
	#			Weather_datavalue.append(float(num))
	#		elif num.isdigit():
	#			Weather_datavalue.append(float(num))
	#		else:
	#			None
	#	except:
			
	#		None

	print(Inverter_datavalue)

	Inverter_values = {
		"Device_ID_1": Inverter_datavalue[5],
		"Power_Now_1" : Inverter_datavalue[6],
		"DC_Input_Power_1": Inverter_datavalue[7],
		"DC_Input_Voltage_1": Inverter_datavalue[8],
		"DC_Input_Current_1": 'N/A',
		"AC_Output_Power_1" : Inverter_datavalue[10],
		"AC_Output_Voltage_1" : Inverter_datavalue[11],
		"AC_Output_Current_1":Inverter_datavalue[12],
		"Frequency_1": Inverter_datavalue[13],
		"Lifetime_Enery_1": Inverter_datavalue[14],
		"Phase_Current_A_1": Inverter_datavalue[15],
		"Phase_Current_B_1": Inverter_datavalue[16],
		"Phase_Current_C_1": Inverter_datavalue[17],
		"Phase_Voltage_A-B_1": Inverter_datavalue[18],
		"Phase_Voltage_B-C_1": Inverter_datavalue[19],
		"Phase_Volatage_C-A_1": Inverter_datavalue[20],
		"Phase_Voltage_A-N_1": Inverter_datavalue[21],
		"Phase_Voltage_B-N_1": Inverter_datavalue[22],
		"Phase_Voltage_C-N_1": Inverter_datavalue[23],	
	# Inverter 2
		"Device_ID_2": Inverter_datavalue[39],
		"Power_Now_2" : Inverter_datavalue[40],
		"DC_Input_Power_2": Inverter_datavalue[41],
		"DC_Input_Voltage_2": Inverter_datavalue[42],
		"DC_Input_Current_2": 'N/A',
		"AC_Output_Power_2" : Inverter_datavalue[44],
		"AC_Output_Voltage_2" : Inverter_datavalue[45],
		"AC_Output_Current_2":Inverter_datavalue[46],
		"Frequency_2": Inverter_datavalue[47],
		"Lifetime_Enery_2": Inverter_datavalue[48],
		"Phase_Current_A_2": Inverter_datavalue[49],
		"Phase_Current_B_2": Inverter_datavalue[50],
		"Phase_Current_C_2": Inverter_datavalue[51],
		"Phase_Voltage_A-B_2": Inverter_datavalue[52],
		"Phase_Voltage_B-C_2": Inverter_datavalue[53],
		"Phase_Volatage_C-A_2": Inverter_datavalue[54],
		"Phase_Voltage_A-N_2": Inverter_datavalue[55],
		"Phase_Voltage_B-N_2": Inverter_datavalue[56],
		"Phase_Voltage_C-N_2": Inverter_datavalue[57],	
	#Inverter 3
		"Device_ID_3": Inverter_datavalue[75],
		"Power_Now_3" : Inverter_datavalue[76],
		"DC_Input_Power_3": Inverter_datavalue[77],
		"DC_Input_Voltage_3": Inverter_datavalue[78],
		"DC_Input_Current_3": 'N/A',
		"AC_Output_Power_3" : Inverter_datavalue[80],
		"AC_Output_Voltage_3" : Inverter_datavalue[81],
		"AC_Output_Current_3":Inverter_datavalue[82],
		"Frequency_3": Inverter_datavalue[83],
		"Lifetime_Enery_3": Inverter_datavalue[84],
		"Phase_Current_A_3": Inverter_datavalue[85],
		"Phase_Current_B_3": Inverter_datavalue[86],
		"Phase_Current_C_3": Inverter_datavalue[87],
		"Phase_Voltage_A-B_3": Inverter_datavalue[88],
		"Phase_Voltage_B-C_3": Inverter_datavalue[89],
		"Phase_Volatage_C-A_3": Inverter_datavalue[90],
		"Phase_Voltage_A-N_3": Inverter_datavalue[91],
		"Phase_Voltage_B-N_3": Inverter_datavalue[92],
		"Phase_Voltage_C-N_3": Inverter_datavalue[93],	
	# Inverter 4
		"Device_ID_4": Inverter_datavalue[111],
		"Power_Now_4" : Inverter_datavalue[112],
		"DC_Input_Power_4": Inverter_datavalue[113],
		"DC_Input_Voltage_4": Inverter_datavalue[114],
		"DC_Input_Current_4": 'N/A',
		"AC_Output_Power_4" : Inverter_datavalue[116],
		"AC_Output_Voltage_4" : Inverter_datavalue[117],
		"AC_Output_Current_4":Inverter_datavalue[118],
		"Frequency_4": Inverter_datavalue[119],
		"Lifetime_Enery_4": Inverter_datavalue[120],
		"Phase_Current_A_4": Inverter_datavalue[121],
		"Phase_Current_B_4": Inverter_datavalue[122],
		"Phase_Current_C_4": Inverter_datavalue[123],
		"Phase_Voltage_A-B_4": Inverter_datavalue[124],
		"Phase_Voltage_B-C_4": Inverter_datavalue[125],
		"Phase_Volatage_C-A_4": Inverter_datavalue[126],
		"Phase_Voltage_A-N_4": Inverter_datavalue[127],
		"Phase_Voltage_B-N_4": Inverter_datavalue[128],
		"Phase_Voltage_C-N_4": Inverter_datavalue[129]
			
		}

			
	return json.dumps(Inverter_values)

Inverter = convert_to_json(Inverter_data)
Json_Inverter = json.loads(Inverter)

print(Json_Inverter)

# You can generate an API token from the "API Tokens Tab" in the UI
token = "_mEZ0zAHEybHXBbq4d8idJE3PWM68K6EG0PXITwC56-6zOAZ-kyl3I4ONzZFpewquEjUzHZkDAs6vrbEviJO7w=="
org = "Volpow"
bucket = "Webscrapper"

client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = (
	influxdb_client.Point("Inverter")
	.tag("SolarVu_data","SolarVu_data")
	.field("Device_ID", Json_Inverter["Device_ID_1"])
	.field("Power", Json_Inverter["Power_Now_1"])
	.field("DC_Input_Power", Json_Inverter["DC_Input_Power_1"])
	.field("DC_Input_Voltage", Json_Inverter["DC_Input_Voltage_1"])
	.field("DC_Input_Current", Json_Inverter["DC_Input_Current_1"])
	.field("AC_Output_Power", (Json_Inverter["AC_Output_Power_1"]))
	.field("AC_Output_Voltage", Json_Inverter["AC_Output_Voltage_1"])
	.field("AC_Output_Current", Json_Inverter["AC_Output_Current_1"])
	.field("Frequency", Json_Inverter["Frequency_1"])
	.field("Lifetime_Enery", Json_Inverter["Lifetime_Enery_1"])
	.field("Phase_Current_A", Json_Inverter["Phase_Current_A_1"])
	.field("Phase_Current_B", Json_Inverter["Phase_Current_B_1"])
	.field("Phase_Current_C", Json_Inverter["Phase_Current_C_1"])
	.field("Phase_Voltage_A-B", Json_Inverter["Phase_Voltage_A-B_1"])
	.field("Phase_Voltage_B-C", Json_Inverter["Phase_Voltage_B-C_1"])
	.field("Phase_Volatage_C-A", Json_Inverter["Phase_Volatage_C-A_1"])
	.field("Phase_Voltage_A-N", Json_Inverter["Phase_Voltage_A-N_1"])
	.field("Phase_Voltage_B-N", Json_Inverter["Phase_Voltage_B-N_1"])
	.field("Phase_Voltage_C-N", Json_Inverter["Phase_Voltage_C-N_1"])
	.field("Device_ID", Json_Inverter["Device_ID_2"])
	.field("Power", Json_Inverter["Power_Now_2"])
	.field("DC_Input_Power", Json_Inverter["DC_Input_Power_2"])
	.field("DC_Input_Voltage", Json_Inverter["DC_Input_Voltage_2"])
	.field("DC_Input_Current", Json_Inverter["DC_Input_Current_2"])
	.field("AC_Output_Power", (Json_Inverter["AC_Output_Power_2"]))
	.field("AC_Output_Voltage", Json_Inverter["AC_Output_Voltage_2"])
	.field("AC_Output_Current", Json_Inverter["AC_Output_Current_2"])
	.field("Frequency", Json_Inverter["Frequency_2"])
	.field("Lifetime_Enery", Json_Inverter["Lifetime_Enery_2"])
	.field("Phase_Current_A", Json_Inverter["Phase_Current_A_2"])
	.field("Phase_Current_B", Json_Inverter["Phase_Current_B_2"])
	.field("Phase_Current_C", Json_Inverter["Phase_Current_C_2"])
	.field("Phase_Voltage_A-B", Json_Inverter["Phase_Voltage_A-B_2"])
	.field("Phase_Voltage_B-C", Json_Inverter["Phase_Voltage_B-C_2"])
	.field("Phase_Volatage_C-A", Json_Inverter["Phase_Volatage_C-A_2"])
	.field("Phase_Voltage_A-N", Json_Inverter["Phase_Voltage_A-N_2"])
	.field("Phase_Voltage_B-N", Json_Inverter["Phase_Voltage_B-N_2"])
	.field("Phase_Voltage_C-N", Json_Inverter["Phase_Voltage_C-N_2"])
	.field("Device_ID", Json_Inverter["Device_ID_3"])
	.field("Power", Json_Inverter["Power_Now_3"])
	.field("DC_Input_Power", Json_Inverter["DC_Input_Power_3"])
	.field("DC_Input_Voltage", Json_Inverter["DC_Input_Voltage_3"])
	.field("DC_Input_Current", Json_Inverter["DC_Input_Current_3"])
	.field("AC_Output_Power", Json_Inverter["AC_Output_Power_3"])
	.field("AC_Output_Voltage", Json_Inverter["AC_Output_Voltage_3"])
	.field("AC_Output_Current", Json_Inverter["AC_Output_Current_3"])
	.field("Frequency", Json_Inverter["Frequency_3"])
	.field("Lifetime_Enery", Json_Inverter["Lifetime_Enery_3"])
	.field("Phase_Current_A", Json_Inverter["Phase_Current_A_3"])
	.field("Phase_Current_B", Json_Inverter["Phase_Current_B_3"])
	.field("Phase_Current_C", Json_Inverter["Phase_Current_C_3"])
	.field("Phase_Voltage_A-B", Json_Inverter["Phase_Voltage_A-B_3"])
	.field("Phase_Voltage_B-C", Json_Inverter["Phase_Voltage_B-C_3"])
	.field("Phase_Volatage_C-A", Json_Inverter["Phase_Volatage_C-A_3"])
	.field("Phase_Voltage_A-N", Json_Inverter["Phase_Voltage_A-N_3"])
	.field("Phase_Voltage_B-N", Json_Inverter["Phase_Voltage_B-N_3"])
	.field("Phase_Voltage_C-N", Json_Inverter["Phase_Voltage_C-N_3"])
	.field("Device_ID", Json_Inverter["Device_ID_4"])
	.field("Power", Json_Inverter["Power_Now_4"])
	.field("DC_Input_Power", Json_Inverter["DC_Input_Power_4"])
	.field("DC_Input_Voltage", Json_Inverter["DC_Input_Voltage_4"])
	.field("DC_Input_Current", Json_Inverter["DC_Input_Current_4"])
	.field("AC_Output_Power", (Json_Inverter["AC_Output_Power_4"]))
	.field("AC_Output_Voltage", (Json_Inverter["AC_Output_Voltage_4"]))
	.field("AC_Output_Current", Json_Inverter["AC_Output_Current_4"])
	.field("Frequency", Json_Inverter["Frequency_4"])
	.field("Lifetime_Enery", Json_Inverter["Lifetime_Enery_4"])
	.field("Phase_Current_A", Json_Inverter["Phase_Current_A_4"])
	.field("Phase_Current_B", Json_Inverter["Phase_Current_B_4"])
	.field("Phase_Current_C", Json_Inverter["Phase_Current_C_4"])
	.field("Phase_Voltage_A-B", Json_Inverter["Phase_Voltage_A-B_4"])
	.field("Phase_Voltage_B-C", Json_Inverter["Phase_Voltage_B-C_4"])
	.field("Phase_Volatage_C-A", Json_Inverter["Phase_Volatage_C-A_4"])
	.field("Phase_Voltage_A-N", Json_Inverter["Phase_Voltage_A-N_4"])
	.field("Phase_Voltage_B-N", Json_Inverter["Phase_Voltage_B-N_4"])
	.field("Phase_Voltage_C-N", Json_Inverter["Phase_Voltage_C-N_4"])
	        
)
	     
write_api.write(bucket, org, record=p)

query = 'from(bucket: "Webscrapper") |> range(start: -1h)'
tables = client.query_api().query(query, org=org)

for table in tables:
	for record in table.records:
		print(record)

client.close()


