from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pridesport_work.sportgoods.urls')),
    path('gears/', include('pridesport_work.gears.urls')),
    path('auth/', include('pridesport_work.pridesport_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)