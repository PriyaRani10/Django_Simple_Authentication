from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    '''
    This class is for customized user model
    '''
    def create_user(self, email, password=None):
        '''
        This class is for customized user model
        '''
        if not email:
            raise ValueError("Email is required!")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        '''
        This class is for customized user model
        '''
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

class LoginUser(AbstractUser):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=100)
    username=None #because I want  user to login through email id
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects = UserManager()

    def __str__(self):
        return self.email

