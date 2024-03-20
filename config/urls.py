from django.contrib import admin
from django.urls import path, include
from oauthapp.views import profile

urlpatterns = [
    path("admin/", admin.site.urls),
    path('oauth/', include('oauthapp.urls')),
    path('accounts/profile/', profile, name='profile'),
    path('social_auth/', include('social_django.urls', namespace='social')),
]
