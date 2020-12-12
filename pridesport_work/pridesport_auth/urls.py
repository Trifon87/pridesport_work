from django.urls import path

from pridesport_work.pridesport_auth.views import login_user, logout_user, RegisterView, UserProfileView

urlpatterns = (
    # path('register/', register_user, name='register user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/<int:pk>', login_user, name='user profile'),
    path('profile/', UserProfileView.as_view() , name='user profile'),
)