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
                "startLng":1,
                "endLng":1,
                "startLat":10,
                "endLat":10,
                "mode":"real"
            }
            the_options = {
                "options": json.dumps(details)
            }
            theData = requests.get('http://www.smartcities.switchsystems.co.uk/api/reading/data', params=the_options)
            
            print theData.url
            print theData.text