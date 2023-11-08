from django.db import models
from django.contrib.auth.models import User

#database part

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    #by order and smth else
    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

    #this to show name of category not just 'category 1 , etc'
    def __str__(self):   
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category , related_name='items' , on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images' , blank=True , null=True)
    descrip = models.TextField(blank=True , null=True)
    price = models.FloatField()
    is_sold=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User , related_name='items' , on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name_plural='Items'

    def __str__(self):
        return self.name
