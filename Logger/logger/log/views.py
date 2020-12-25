from log.models import Record
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
from .forms import RecordForm
# Create your views here.


def HomeListView(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        current_user = request.user
        records = Record.objects.filter(technician=current_user)
        return render(request, 'log/home.html', {'records': records})
    else:
        return render('users/login.hmtl')


def CreateRecordView(request):
    title = "Create Record"
    form = RecordForm(initial={'technician': request.user})
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            form = RecordForm(initial={'technician': request.user})
            return redirect('/')

    context = {'form': form, 'title': title}
    return render(request, 'log/create_record.html', context)


def DetailRecordView(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record': record}

    return render(request, 'log/record.html', context)


def UpdateRecordView(request, pk):
    pass