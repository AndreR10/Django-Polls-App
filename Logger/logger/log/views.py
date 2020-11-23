from log.models import Record
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Record
# Create your views here.


def HomeListView(request):
    if request.user.is_authenticated:
    # Do something for authenticated users.
        current_user = request.user
    
    else:
    # Do something for anonymous users.
    context = {'record': Record.objects.all()}
