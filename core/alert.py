from models import *
from heatwave.passwords import *

import requests

#For now, use the Pushover API (as Twilio Costs money)

#range = 0.75

#Sends the text alert to Volunteer
def sendAlert(theVulnerable):
    #print pushoverKey()
    print theVulnerable.id
    
    #Find Volunteer
    
    theVolunteers = Volunteer.objects.all()
    for vol in theVolunteers:
        if abs(vol.geo_lat - theVulnerable.geo_lat) <= 0.3:
            if not Alert.objects.filter(regarding = theVulnerable):
	            theAlert = Alert()
	            theAlert.to = vol
	            theAlert.regarding = theVulnerable
	            theAlert.save()
	            print "Sending.."
	            the_push_data = {
	                "token": pushoverKey(),
	                "user": vol.number,
	                "message": vol.name + ", Could you go check on " + theVulnerable.name + " at " + theVulnerable.address,
	                "title": "Alert!",
	                "url": "http://beta.thisisthechris.co.uk/heatwave/alert/" + str(theAlert.id) + "/",
	                "url_title": "Complete Check",
	                "sound": "siren",
	            }
	            the_push = requests.post("https://api.pushover.net/1/messages.json", data=the_push_data)