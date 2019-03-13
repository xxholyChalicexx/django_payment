from django.contrib import admin
from .models import Coupon, History

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user','first_name', 'last_name', 'company', 'email', 'package', 'quantity', 'manager', 'coin', 'status','amount', 'createdAt')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
	list_display = ('coupon_code','percent','expiry','frequency','user')