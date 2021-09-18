from django import forms

from datetime import datetime, timedelta

from prompt_toolkit.validation import ValidationError


class EmailModelForm(forms.Form):
    text = CharField(label='Please, enter the reminder you wish.')
    time = forms.DateTimeField(label='Enter reminder time you interested in.', format={'%D-%m-%Y %H:%M'})
    email = forms.EmailField(label='Enter email for reminding.')

    def validation(self):
        data = self.time
        if (datetime.today()) > data > (datetime.utcnow() + timedelta(days=2)):
            raise ValidationError('You entered invalid data')
        return data
