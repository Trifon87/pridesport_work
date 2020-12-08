from django.urls import path

from gears.views import gear_list, gear_details, gear_like, edit, delete, create, about

urlpatterns = [
    path('', gear_list, name='gears'),
    path('details/<int:pk>/', gear_details, name='gear detail'),
    path('like/<int:pk>/', gear_like, name='like gear'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create/', create, name='create'),
    path('about/', about, name='about'),
]
