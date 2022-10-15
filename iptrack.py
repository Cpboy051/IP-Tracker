import os,sys
import json
import time
from urllib import request
os.system("clear")
print(" IP TRACKER ".center(25,"="),"\n")

url = "https://ipapi.co/"
ip = input("Input the IP Address : ")
request = request.urlopen(url + ip + "/json")
data_json = json.loads(request.read())

print("\nIP : " + str(data_json['ip']))
print("Country : " + str(data_json['country_name']))
print("Country Code : " + str(data_json['country_code']))
print("Country Iso : " + str(data_json['country_code_iso3']))
print("Country Capital : " + str(data_json['country_capital']))
print("Country tld : " + str(data_json['country_tld']))
print("Region : " + str(data_json['region']))
print("Region Code : " + str(data_json['region_code']))
print("City : " + str(data_json['city']))
print("Continent Code : " + str(data_json['continent_code']))
print("InEu : " + str(data_json['in_eu']))
print("Postal Code : " + str(data_json['postal']))
print("Latitude : " + str(data_json['latitude']))
print("Longitude : " + str(data_json['longitude']))
print("Timezone : " + str(data_json['timezone']))
print("Utc offset : " + str(data_json['utc_offset']))
print("Country Calling Code " + str(data_json['country_calling_code']))
print("Currency : " + str(data_json['currency']))
print("Currency Name : " + str(data_json['currency_name']))
print("Languages : " + str(data_json['languages']))
print("ASN : " + str(data_json['asn']))
print("ISP : " + str(data_json['org']))
print("Google Maps : https://maps.google.com/?q=" + str(data_json['latitude'])+','+str(data_json['longitude']))
print("\n\n\33[31;1m[!]\33[0m \33[33;1mWait for 10 seconds to open google maps automatically")
time.sleep(10)
os.system(f"xdg-open https://maps.google.com/?q={data_json['latitude']},{data_json['longitude']}")
