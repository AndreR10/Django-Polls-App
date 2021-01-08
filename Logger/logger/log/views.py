# from log.models import Record
from log.models import Log
from django.shortcuts import render, redirect
from .models import *
from .forms import LogForm
# Create your views here.


def HomeListView(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        current_user = request.user
        logs = Log.objects.filter(technician=current_user)
        return render(request, 'log/home.html', {'logs': logs})
    else:
        return render(request, 'sign/login.html')


def CreateLogView(request):
    title = "Create Log"
    form = LogForm(initial={'technician': request.user})
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            form = LogForm(initial={'technician': request.user})
            return redirect('/')

    context = {'form': form, 'title': title}
    return render(request, 'log/create_log.html', context)


def DetailLogView(request, pk):
    log = Log.objects.get(id=pk)
    context = {'log': log}

    return render(request, 'log/log.html', context)


def UpdateLogView(request, pk):
    title = "Update Log"

    log = Log.objects.get(id=pk)
    form = LogForm(instance=log)
    if request.method == 'POST':
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'title': title}
    return render(request, 'log/create_log.html', context)
