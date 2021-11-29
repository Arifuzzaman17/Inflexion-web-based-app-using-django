from django.urls import path

from . import views
app_name = 'gallery'
urlpatterns = [
    path('', views.index, name='index'),
    path('log_in/', views.log_in, name="log_in"),
    path('register/', views.register, name='register'),
    path('log_out/', views.log_out, name='log_out'),
    path('userpage/', views.adminpage, name='userpage')
]