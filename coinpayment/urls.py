from django.urls import path, include
from . import views

app_name='coinpayment'

urlpatterns = [
	path('', views.submitform_view, name='submitform'),
    path('history/',views.profile_view, name='history')
]	