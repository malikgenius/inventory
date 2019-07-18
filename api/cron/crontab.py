
from django.core.mail import send_mail


# class MyCronJob():

def MyCronJob():
    print("CronJob is running")
    send_mail(
        'this mail is from django schedule cron',
        'This is body',
        'malikgen2010@gmail.com',
        ['malik@zeenah.com', 'malikgen2010@gmail.com'],
        fail_silently=False
    )
