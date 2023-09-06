from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home, name="Home"),
    path('privacidad', views.privacidad, name="privacidad"),
    path('aviso', views.aviso, name="aviso"),



   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)