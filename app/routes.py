from app import app

import requests
from requests.packages import urllib3
import re
import json
from flask import Response

def getData():
  #https://www.sma.de/en/company/pv-electricity-produced-in-germany.html
  
  r = requests.get('https://pvd.sunny-portal.com/powermapapi/powermap/Latest/?callback=jQuery&token=test&_=', headers={'Content-type': 'application/json'})
  
  data_in = r.text
  data_in = data_in.replace("/**/ typeof jQuery === 'function' && jQuery(","")
  data_in = data_in.replace(");","")
  
  
  
  #print(data_in)
  
  return data_in    

    
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  path = path.upper()
  power = getData()
  #if path in air_map:
  #    return Response(json.dumps(air_map[path]), mimetype='application/json')
      
  #else:
  return Response(power, mimetype='application/json')
