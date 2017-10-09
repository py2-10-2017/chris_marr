
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):
    request.session['upper_date'] = "{:%b %d, %Y}".format(datetime.now())
    request.session['lower_date'] = "{:%I:%M %p}".format(datetime.now()) 
    return render(request, "time_display_app/index.html")