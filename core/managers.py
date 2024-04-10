from django.contrib.auth.models import BaseUserManager


class CustomBaseUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('email must be provided.')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class TrainerManager(CustomBaseUserManager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(type=self.model.UserTypes.TRAINER)


class RegularManager(CustomBaseUserManager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(type=self.model.UserTypes.REGULAR)
