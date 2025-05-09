from django.urls import path
from Nutritionapp import views

urlpatterns = [
    path('',views.food_list,name='food_list'),
    path('details/<int:id>/',views.food_detail,name='food_detail'),
    path('tracker/',views.caloriTracker,name='tracker'),
]