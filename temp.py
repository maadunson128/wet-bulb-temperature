import urllib.request
import sys

import json
                
try: 
  ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chennai/1992-01-02/2024-05-30?unitGroup=metric&include=days&key=99R86NJY7AMLXNWS3VHLGADN5&contentType=json")
  
  # Parse the results as JSON
  jsonData = json.load(ResultBytes)
        
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()