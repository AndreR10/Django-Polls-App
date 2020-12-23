from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import DateTimeInput
from .models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ('technician', 'client', 'subject', 'start_date_time',
                  'end_date_time', 'end_date_time', 'total_hours',
                  'service_type', 'category', 'description', 'status')
        widgets = {
            'start_date_time':
            DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'end_date_time':
            DateTimeInput(
                attrs={
                    # 'class': 'form-control datetimepicker-input',
                    'class': 'form-control',
                    # 'data-target': '#datetimepicker1'
                    'type': 'datetime-local'
                }),
        }
