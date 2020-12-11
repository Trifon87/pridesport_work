from django.urls import path

from pridesport_work.sportgoods.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing page')
]