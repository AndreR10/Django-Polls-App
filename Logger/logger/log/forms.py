from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput, TimePickerInput
from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import DateTimeInput
from .models import Record
from django import forms

from django import forms


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ('technician', 'client', 'subject', 'date', 'start_time',
                  'end_time', 'total_hours', 'service_type', 'category',
                  'description', 'status')

        labels = {"date": "Date", "start_time": "Start", "end_time": "End"}

        widgets = {
            'date': DatePickerInput(),
            'start_time': TimePickerInput(),
            'end_time': TimePickerInput(),
        }

        # def clean_end_date_time(self):
        #     start_date_time = self.cleaned_data.get('start_date_time')
        #     end_date_time = self.cleaned_data.get('end_date_time')
        #     if start_date_time > end_date_time:
        #         raise forms.ValidationError("Check your start and end date!")
        #     return end_date_time