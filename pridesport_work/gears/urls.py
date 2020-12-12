from django.urls import path

from pridesport_work.gears.views import gear_list, gear_details, gear_like, edit, delete, about, CreateGearView

urlpatterns = [
    path('', gear_list, name='gears'),
    path('details/<int:pk>/', gear_details, name='gear detail'),
    path('like/<int:pk>/', gear_like, name='like gear'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create/', CreateGearView.as_view(), name='create'),
    path('about/', about, name='about'),
]
