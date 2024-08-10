from django.urls import path
from . import views

urlpatterns = [
    path('food/',views.food,name='food'),
    path('drink/',views.drink,name='drink'),
    path('food/<slug:slug>',views.foodDetail,name='food-detail'),
    path('drink/<slug:slug>',views.drinkDetail,name='drink-detail'),
    path('add-menu/',views.AddMenu.as_view(),name='add-menu'),
    path('updata/<int:id>',views.updata,name='updata'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search',views.search,name='search')

]
