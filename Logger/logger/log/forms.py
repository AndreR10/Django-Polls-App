from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import DateTimeInput
from .models import Record
from django import forms


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ('technician', 'client', 'subject', 'start_date_time',
                  'end_date_time', 'end_date_time', 'total_hours',
                  'service_type', 'category', 'description', 'status')
        widgets = {
            'start_date_time':
            DateTimeInput(
                attrs={
                    # 'class': 'form-control',
                    # 'id': 'start_date_time',
                    'type': 'datetime-local'
                }),
            'end_date_time':
            DateTimeInput(
                attrs={
                    # 'class': 'form-control datetimepicker-input',
                    # 'class': 'form-control',
                    # 'id': 'end_date_time',
                    # 'data-target': '#datetimepicker1'
                    'type': 'datetime-local'
                }),
        }

        # def clean_end_date_time(self):
        #     start_date_time = self.cleaned_data.get('start_date_time')
        #     end_date_time = self.cleaned_data.get('end_date_time')
        #     if start_date_time > end_date_time:
        #         raise forms.ValidationError("Check your start and end date!")
        #     return end_date_time