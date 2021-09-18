from django.shortcuts import render

from django import forms

from notifications.forms import EmailModelForm

from django.http import HttpResponse

from datetime import datetime, timedelta


def send_reminder(request):
    if request.method == 'POST':
        form = EmailModelForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            time = form.cleaned_data['time']
            email = form.cleaned_data['email']
            today = datetime.utcnow()
            #max_day = datetime.utcnow() + timedelta(days=2)
            send_reminder_task.apply_async((text, email), eta=today)
            return redirect('send_reminder')
    else:
        form = EmailModelForm()
    return render(request, 'notifications/reminder.html', {'form': form})