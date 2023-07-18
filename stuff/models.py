from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField()
    image = models.ImageField(upload_to='image/',null=True, blank = True, default='default.jpg')
    price =models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):    
        return reverse("item_detail", args=[str(self.id)])