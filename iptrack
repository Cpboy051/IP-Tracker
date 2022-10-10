import os,sys
import json
from urllib import request
os.system("clear")
print("\n== IP TRACKER ==\n")

url = "https://ipapi.co/"
ip = input("Input the IP Address : ")
request = request.urlopen(url + ip + "/json")
data_json = json.loads(request.read())

print("IP : " + str(data_json['ip']))
print("Country : " + str(data_json['country_name']))
print("Region : " + str(data_json['region']))
print("City : " + str(data_json['city']))
print("Postal Code : " + str(data_json['postal']))
print("Latitude : " + str(data_json['latitude']))
print("Longitude : " + str(data_json['longitude']))
print("ISP : " + str(data_json['org']))
