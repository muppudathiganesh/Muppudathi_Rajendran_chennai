<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
     path('success/', views.success_page, name='thankyou'),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
     path('success/', views.success_page, name='thankyou'),
>>>>>>> 9283bda8974f6b64c7b05e78e21b2fca59cb27fe
]