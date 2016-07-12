import sys, time, json, requests

categories = {"Some Category": "@SomeCategoryBroadcast", "Some Other Category": "@SomeOtherCategoryBroadcast"}

# replace with your own logic, this is a very simple solution that works for our extractor
def extractDataFromJSON(json, category):
  return json['extractorData']['data'][0]['group'][0][category]

# replace with your own logic, this returns whether the value starts with "dd.mm." of today's date, e.g. 21.03.
def fulfillsCriteria(value):
  today = time.strftime("%d.%m.")
  return value.startswith(today)
  
EXTRACTOR_ID = sys.argv[1]
EXTRACTOR_API_KEY = sys.argv[2]
BOT_ID = sys.argv[3]
BOT_TOKEN = sys.argv[4]
TARGET_URL = sys.argv[5]

importUrl = "https://extraction.import.io/query/extractor/" + EXTRACTOR_ID + "?_apikey=" + EXTRACTOR_API_KEY + "&url=" + TARGET_URL
try:
    response = requests.get(importUrl)
    print(response.status_code)
    data = response.json()
    
    for category, broadcast in categories.items():
        entries = extractDataFromJSON(data, category)
        for entry in entries:
            value = entry["text"]
            if fulfillsCriteria(value):
                postUrl = "https://api.telegram.org/bot" + BOT_ID + ":" + BOT_TOKEN + "/sendmessage?chat_id=" + broadcast + "&text=" + value
                requests.get(postUrl)
except requests.ConnectionError:
    print("failed to connect")
    sys.exit(0)
