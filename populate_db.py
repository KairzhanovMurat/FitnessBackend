import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import random
from faker import Faker
from django.utils import timezone
from core.models import BaseUser, Regular, Trainer, Gym, Schedule

fake = Faker()


def create_users(num_users):
    for _ in range(num_users):
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        second_name = fake.last_name()
        phone_number = fake.phone_number()
        gender = random.choice(['Male', 'Female'])
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
        is_trainer = random.choice([True, False])

        if is_trainer:
            user = Trainer.objects.create_user(
                email=email,
                first_name=first_name,
                second_name=second_name,
                last_name=last_name,
                phone_number=phone_number,
                gender=gender,
                date_of_birth=date_of_birth
            )
        else:
            user = Regular.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                gender=gender,
                date_of_birth=date_of_birth
            )

        gyms = Gym.objects.all()
        for _ in range(random.randint(1, 3)):
            gym = random.choice(gyms)
            gym.members.add(user)


def create_gyms(num_gyms):
    for _ in range(num_gyms):
        name = fake.company()
        address = fake.address()
        city = fake.city()
        Gym.objects.create(
            name=name,
            address=address,
            city=city
        )


def create_schedules(num_schedules):
    trainers = Trainer.objects.all()
    gyms = Gym.objects.all()
    for _ in range(num_schedules):
        trainer = random.choice(trainers)
        gym = random.choice(gyms)
        day = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        start_time = fake.time(pattern='%H:%M:%S', end_datetime=None)
        end_time = (timezone.datetime.strptime(start_time, '%H:%M:%S') + timezone.timedelta(
            hours=random.randint(1, 3))).time()

        schedule = Schedule.objects.create(
            trainer=trainer,
            gym=gym,
            day=day,
            start_time=start_time,
            end_time=end_time
        )

        regular_users = Regular.objects.all()
        for _ in range(random.randint(5, 15)):
            regular_user = random.choice(regular_users)
            schedule.members.add(regular_user)


def populate_dummy_data():
    if not Gym.objects.exists():
        create_gyms(5)
    if not BaseUser.objects.exists():
        create_users(20)
    if not Schedule.objects.exists():
        create_schedules(10)
    if not BaseUser.objects.filter(email='admin@mail.com', is_staff=True, is_superuser=True).exists():
        BaseUser.objects.create_superuser(email='admin@mail.com', password='123')


if __name__ == '__main__':
    populate_dummy_data()
