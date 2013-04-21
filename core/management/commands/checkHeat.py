from django.core.management.base import BaseCommand, CommandError
from core.models import *
from core.alert import *
import requests
import json
import time

from heatwave.passwords import *

class Command(BaseCommand):
    help = 'Checks Heat levels around Vulnerable people'
    
    

    def handle(self, *args, **options):
        theVulnerables = Vulnerable.objects.all()
        
        while True:
            for vun in theVulnerables:
                details = {
                    "sensors":["TEMP"],
                    "startLng":float(vun.geo_long)-0.5,
                    "endLng":float(vun.geo_long)+0.5,
                    "startLat":float(vun.geo_lat)-0.5,
                    "endLat":float(vun.geo_lat)+0.5,
                    "mode":"real"
                }
                the_options = {
                    "options": json.dumps(details)
                }
                theData = requests.get('http://www.smartcities.switchsystems.co.uk/api/reading/data', params=the_options)
                
                #print theData.json()
                print theData.text
                
                #loadedData = json.loads(theData.json())
                
                #print loadedData
                
                for sensor in theData.json()["readings"]:
                    if not (sensor["device_lat"] == None):
                        if not (sensor["device_lng"] == None): 
                           print sensor["device_lat"] + "," + sensor["device_lng"] + ":" + sensor["sensorValue"]
                           if float(sensor["sensorValue"]) >= 28:
                               print "Alert!"
                               sendAlert(vun)
                               
                               
                               
            print 'sleeping.'
            time.sleep(10)
            print 'sleeping..'
            time.sleep(10)
            print 'sleeping...'