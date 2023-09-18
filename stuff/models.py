from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
import random
from django.db.models.signals import pre_save, post_save


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50,blank=True,null=True)
    discription = models.TextField()
    image = models.ImageField(upload_to='products/',null=True, blank = True, default='default.jpg')
    price =models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):    
        return reverse("item_detail", args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
  



def slugify_instance_name(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_name(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance

def product_pre_save(sender, instance, *args, **kwargs):
    
    if instance.slug is None:
        slugify_instance_name(instance, save=False)

pre_save.connect(product_pre_save, sender=Product)


def product_post_save(sender, instance, created, *args, **kwargs):
    
    if created:
        slugify_instance_name(instance, save=True)

post_save.connect(product_post_save, sender=Product)



class comment(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Product,related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
