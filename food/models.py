from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    def __str__(self) -> str:
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    item_image = models.CharField(max_length=500 , default="https://nanilovestocook.com/wp-content/uploads/2022/08/placeholder.png")
    
    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})
    

