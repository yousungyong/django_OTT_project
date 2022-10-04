from django.contrib import admin
from django.urls import path, include
from acc import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Main/', include('OTT.urls')),
    path('acc/', include('acc.urls')),
    path('', include('acc.urls')),
    #path('', auth_views.LoginView.as_view(template_name='acc/login.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
