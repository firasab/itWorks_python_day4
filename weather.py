import argparse
import json
import requests
import re

parser=argparse.ArgumentParser()
parser.add_argument('xDate')
args=parser.parse_args()


url="http://api.weatherapi.com/v1/current.json?key=ca906cb4997343508e7165953202010"


regex = re.compile('[/.:]')
if(regex.search(args.xDate) == None):
        print("the weather in  ",args.xDate)
        url+="&q="
        url+=args.xDate
else:
    print("The date you entered :  ",args.xDate)
    user_location=input("please enter the city : ")
    url+="&dt="
    url+=args.xDate
    url+="&q="
    url+=user_location


response = requests.get(url)
data = json.loads(response.text)
print("current temp: ",data['current']['temp_c'])

    
    