from django.urls import path

from sportgoods.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing page')
]