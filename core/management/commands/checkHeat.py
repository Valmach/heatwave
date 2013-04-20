from django.core.management.base import BaseCommand, CommandError
from core.models import *
import requests
import json

class Command(BaseCommand):
    help = 'Checks Heat levels around Vulnerable people'

    def handle(self, *args, **options):
        theVulnerables = Vulnerable.objects.all()
        
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
            
            print theData.json()
            #print theData.text
            
            #loadedData = json.loads(theData.json())
            
            #print loadedData
            
            for sensor in theData.json()["readings"]:
                print sensor["sensorValue"]