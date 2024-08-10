from django.contrib import admin
from .models import Item,Category,MealTime  
# Register your models here.
class ModelCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class ModelMealtime(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,ModelCategory)
admin.site.register(MealTime,ModelMealtime)
admin.site.register(Item)
