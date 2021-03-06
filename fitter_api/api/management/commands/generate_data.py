from ...models import *
from faker import Faker
import random
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand

fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_users()
        create_activities()
        create_stats()


def create_users():
    for _ in range(10):
        new_user = User.objects.create_user(username=fake.user_name(),
                                            password='password',
                                            email='')
        new_user.save()


def create_activities():
    for _ in range(50):
        new_activity = Activity(title=fake.bs(),
                                units=fake.text(max_nb_chars=9),
                                user=random.choice(User.objects.all()))
        new_activity.save()


def create_stats():
    for _ in range(500):
        while True:
            try:
                new_stat = Stats(activity=random.choice(Activity.objects.all()),
                                 number_of=random.randint(1, 20),
                                 date=fake.date_time_between(start_date="-1y", end_date="now").date())
                new_stat.save()
                break
            except:
                continue
