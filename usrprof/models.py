from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile (models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="image/", default='default.jpg',null=True, blank=True)
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=True ,blank=True )
    email = models.EmailField(null=True ,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    
    
    def get_absolute_url(self):    
        return reverse("profile", args=[str(self.id)])