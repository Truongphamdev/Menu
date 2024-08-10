from django import forms
from .models import Item, Category, MealTime

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'meal_time', 'name', 'content','image', 'price']

