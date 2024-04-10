
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import CustomBaseUserManager, RegularManager, TrainerManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    class UserTypes(models.TextChoices):
        TRAINER = "Trainer", "Trainer"
        REGULAR = "Regular", "Regular"

    class Genders(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    second_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    gender = models.CharField(max_length=255, choices=Genders.choices, null=True, blank=True)
    type = models.CharField(max_length=255, choices=UserTypes.choices, null=True, blank=True)

    date_of_birth = models.DateField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomBaseUserManager()

    @property
    def initials(self):
        return f'{self.first_name} {self.second_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Regular(BaseUser):
    class Meta:
        proxy = True
        verbose_name = 'Regular'

    def save(self, *args, **kwargs):
        self.type = self.UserTypes.REGULAR
        return super().save(*args, **kwargs)

    objects = RegularManager()


class Trainer(BaseUser):
    class Meta:
        proxy = True
        verbose_name = 'Trainer'

    def save(self, *args, **kwargs):
        self.type = self.UserTypes.TRAINER
        return super().save(*args, **kwargs)

    objects = TrainerManager()


class Gym(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    members = models.ManyToManyField(BaseUser, related_name='gyms')

    def __str__(self):
        return f'{self.name} - {self.city}'


class Schedule(models.Model):
    class DAYS(models.TextChoices):
        monday = 'Monday', 'Monday'
        tuesday = 'Tuesday', 'Tuesday'
        wednesday = 'Wednesday', 'Wednesday'
        thursday = 'Thursday', 'Thursday'
        friday = 'Friday', 'Friday'
        saturday = 'Saturday', 'Saturday'
        sunday = 'Sunday', 'Sunday'

    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    day = models.CharField(max_length=255, choices=DAYS.choices, null=True, blank=True)

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="trainer_schedules")
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name="gym_schedules")
    members = models.ManyToManyField(Regular, related_name="users_schedules")

    def __str__(self):
        return f"{self.trainer} - {self.gym.name} - {self.start_time} - {self.end_time}"
