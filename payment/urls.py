from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('submitform/',include('coinpayment.urls')),
    path('reset/', include('django.contrib.auth.urls'))
]