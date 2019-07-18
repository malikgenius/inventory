from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from api.models import Item
from django.contrib.auth.models import User


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.EmailUsercountCronJob'

    def do(self):
        # item = Item.objects.get(pk=2)
        # my_user = User.objects.get(pk=1)
        my_user = User.objects.all()
        try:
            for user in my_user:
                if user.emails:
                    print("user has " + user.email + "in db")
        except:
            print("user has no email in db")

        else:
            print("something went wrong")

        # if my_user.email == 'malik@zeenah.com':
        # if my_user:
        #     # print(item.condition, item.purchased_date)
        #     print(my_user.email)
        #     print("CronJob is running")
        #     # send_mail(
        #     #     'this mail is from django schedule cron',
        #     #     'This is body' + my_user.username + 'is admin',
        #     #     'malikgen2010@gmail.com',
        #     #     [my_user.email, 'malikgen2010@gmail.com'],
        #     #     fail_silently=False
        #     # )
        # else:
        #     print("couldnt find item & its details")

    def all_users(self):
        users = User.objects.all()
        for x in range(5):
            print(x)

        # for user in users:
        #     print(user.email)
