from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Coupon(models.Model):
	coupon_code = models.CharField(max_length=50)
	package = models.CharField(max_length=50, choices=[
		('All','All'),
		('Ultimate Executive','Ultimate Executive'),
		('Ultimate','Ultimate'),
		('Bitcoin Blast','Bitcoin Blast')
	])
	percent = models.FloatField()
	expiry = models.DateField(blank=True)
	frequency = models.IntegerField(default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return f'Code : {self.coupon_code} | Package : {self.package} | Discount Percent : {self.percent}% | Assigned User : {self.user} | Expiry Date : {self.expiry} | Frequency : {self.frequency}'

class History(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	email = models.EmailField()
	package = models.CharField(max_length=50)
	quantity = models.IntegerField()
	manager = models.CharField(max_length=50)
	coin = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	amount = models.CharField(max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	createdAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'Name : {self.first_name} {self.last_name} | Company : {self.company} | Package : {self.package} | Coin : {self.coin}'

class Extra_Info(models.Model):
	email = models.EmailField()
	company = models.CharField(max_length=50)