from django.db import models
from django.urls import reverse
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation

class Product(models.Model):
    name = models.CharField(max_length=255)
    discription = models.TextField()
    image = models.ImageField(upload_to='products/',null=True, blank = True, default='default.jpg')
    price =models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation(Comment)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):    
        return reverse("item_detail", args=[str(self.id)])
    



