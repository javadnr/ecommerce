from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from extensions.utils import jalali_converter


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='اسم')
    discription = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='products/', null=True, blank=True,
                              default='basket.png', verbose_name='تصویر')
    price = models.FloatField(verbose_name='قیمت')
    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name='تاریخ ایجاد')
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالا ها'

    def __str__(self):
        return self.name
    
    def jdate_added(self):
        return jalali_converter(self.date_added)

    def get_absolute_url(self):    
        return reverse("item_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name='کاربر')
    products = models.ManyToManyField(Product, through='CartItem',
                                      verbose_name='کالاها')

    class Meta:
        verbose_name = 'کارت'
        verbose_name_plural = 'کارت ها'

    def __str__(self):
        return f'کارت برای {self.user.username}'
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             verbose_name='کارت')
    product = models.ForeignKey(Product, related_name='cartitem',
                                on_delete=models.CASCADE, verbose_name='کالا')
    quantity = models.PositiveIntegerField(default=1, verbose_name='مقدار')

    class Meta:
        verbose_name = 'کالا در کارت'
        verbose_name_plural = 'کالا های در کارت'

    def __str__(self):
        return f'{self.quantity} x {self.product.name} در {self.cart}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='نویسنده')
    post = models.ForeignKey(Product, related_name='comments',
                             on_delete=models.CASCADE, verbose_name='پست')
    body = models.TextField(null=True, blank=True, verbose_name='بدنه')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        
    def jdate_added(self):
        return jalali_converter(self.date_added)
