from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_drink = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class MealTime(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='image')
    is_drink = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    meal_time = models.ForeignKey(MealTime,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    image = models.ImageField(upload_to='image')
    price = models.DecimalField(max_digits=6,decimal_places=3)
    def __str__(self):
        return self.name