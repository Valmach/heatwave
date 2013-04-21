import requests
import json
import datetime, math, time

data = {
    "deviceId": "901",
    "sensorName": "TEMP",
    "dataFloat": 29
}

the_data = {
    "data": json.dumps(data)
}

send = requests.get('http://www.smartcities.switchsystems.co.uk/api/reading/send/' + json.dumps(data))

print send.text

print 'sleeping.'
time.sleep(10)
print 'sleeping..'
time.sleep(10)
print 'sleeping...'

data = {
    "deviceId": "902",
    "sensorName": "TEMP",
    "dataFloat": 29
}

send = requests.get('http://www.smartcities.switchsystems.co.uk/api/reading/send/' + json.dumps(data))

print send.text

data = {
    "deviceId": "904",
    "sensorName": "TEMP",
    "dataFloat": 29
}

send = requests.get('http://www.smartcities.switchsystems.co.uk/api/reading/send/' + json.dumps(data))

print send.text

print 'sleeping.'
time.sleep(10)
print 'sleeping..'
time.sleep(10)
print 'sleeping...'

data = {
    "deviceId": "903",
    "sensorName": "TEMP",
    "dataFloat": 29
}

send = requests.get('http://www.smartcities.switchsystems.co.uk/api/reading/send/' + json.dumps(data))

print send.text

data = {
    "deviceId": "905",
    "sensorName": "TEMP",
    "dataFloat": 29
}

send = requests.get('http://www.smartcities.switchsystems.co.uk/api/reading/send/' + json.dumps(data))

print send.text