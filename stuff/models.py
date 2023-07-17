from django.db import models
from django.urls import reverse
class Stuff(models.Model):
    tag = models.ForeignKey('Tag',on_delete=models.CASCADE,null =True)
    name = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg',upload_to='image/')
    feature = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # specs = 

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})    
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(Stuff,related_name='comments',on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')
    
    class Meta:
        ordering=['-date_added']
    
    def __str__(self):
        return self.name
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    
class Questions(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(Stuff,related_name='questions',on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')
    
    class Meta:
        ordering=['-date_added']
    
    def __str__(self):
        return self.name
    
    @property
    def children(self):
        return Questions.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    

    