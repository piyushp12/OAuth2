from django.db import models
from django.core.files import File
import qrcode
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import os
from django.core.management.base import BaseCommand
from django.conf import settings
# Create your models here.

class Command(BaseCommand):
    def handle(self, *args, **options):
        physical_files = set()
        db_files = set()

        media_root = getattr(settings, 'MEDIA_ROOT', None)
        if media_root is not None:
            for relative_root, dirs, files in os.walk(media_root):
                for file_ in files:
                    relative_file = os.path.join(os.path.relpath(relative_root, 
                    media_root), file_)
                    physical_files.add(relative_file)

        deletables = physical_files - db_files
        if deletables:
            for file_ in deletables:
                os.remove(os.path.join(media_root, file_))


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.is_superuser = True
        if user.is_superuser: user.user_type = "Admin"
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    avatar = models.ImageField("Avatar", upload_to="Profile/%Y/%m/%d/", blank=True, null=True)
    username = models.CharField(max_length=100, null=False,blank=False)
    email = models.CharField(max_length=100, null=False,blank=False,unique=True)
    phone_number = models.CharField(max_length=10, null=False,blank=False)
    address = models.CharField("Address", max_length=100, null=False, blank=False,default='')
    is_superuser = models.BooleanField("Super User", default=False)
    is_staff = models.BooleanField(default=False)
    otp = models.CharField("Otp",max_length=10,null=False,blank=False,default='')
    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def create_otp(self):
        otp = random.randint(1000, 9999)
        self.otp = otp
        self.otp_varify = False
        self.save()
        return otp