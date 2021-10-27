from django.urls import path
from . import views
from task import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.create_profile),
    path('storage/<str:pk>', views.storage),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)