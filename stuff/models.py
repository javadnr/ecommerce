from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=255)
    discription = models.TextField()
    image = models.ImageField(upload_to='products/',null=True, blank = True, default='basket.png')
    price =models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):    
        return reverse("item_detail", args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
  



class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,through='CartItem')
    
    def __str__(self):
        return f'cart for {self.user.username}'
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cartitem',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name} in {self.cart}'
    


class Comment(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Product,related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(null=True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)
