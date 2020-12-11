from django.contrib import admin

# Register your models here.
from pridesport_work.pridesport_auth.models import UserProfile

admin.site.register(UserProfile)