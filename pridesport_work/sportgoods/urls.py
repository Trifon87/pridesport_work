from django.urls import path

from pridesport_work.sportgoods.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(), name='landing page')
]