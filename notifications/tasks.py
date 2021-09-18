from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_reminder_task(text, email):
    send_mail(
        'Your reminder',
        messege=text,
        'admin@admin.com',
        [email],
        fail_silently=False,
    )