# Create your views here.
from models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.db.models import Count
from django.utils import timezone

def clear_alert(request, alert_id):
    theAlert = get_object_or_404(Alert, pk=alert_id)
    theAlert.is_okay = True
    theAlert.save()
    
    return return render_to_response('thanks.html',{
               'the_vlun':theAlert.regarding,
           }, context_instance=RequestContext(request))