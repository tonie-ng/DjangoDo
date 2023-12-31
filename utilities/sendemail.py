from todo_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_email(esubject, emessage, ereceiver):
    try:
        send_mail(esubject,
                  emessage,
                  EMAIL_HOST_USER,
                  ereceiver)
        return (0)
    except Exception as e:
        return (e)
