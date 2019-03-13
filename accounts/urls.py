from django.urls import path, include
from . import views
from django.contrib.auth.views import password_reset, password_reset_done

app_name='accounts'

urlpatterns = [
    path('',views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.edit_profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name="change_password")
]