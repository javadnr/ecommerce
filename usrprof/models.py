from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile (models.Model):
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.CASCADE,verbose_name='کاربر')
    profile_pic = models.ImageField(upload_to="image/", default='default.jpg',
                                    null=True, blank=True, verbose_name='عکس پروفایل')
    first_name = models.CharField(max_length=50, verbose_name='اسم ')
    last_name = models.CharField(max_length=50, verbose_name='فامیل')
    phone_number = models.IntegerField(null=True, blank=True, verbose_name='شماره تلفن')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ورود')

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروقایل ها'

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):    
        return reverse("profile", args=[str(self.id)])
