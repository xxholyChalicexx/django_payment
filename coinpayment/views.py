from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .coinpayments import CryptoPayments
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import submitForm
from .models import History, Coupon

@login_required(login_url="/")
def submitform_view(request):
	if request.method == 'POST':
		form = submitForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			company = form.cleaned_data['company']
			email = form.cleaned_data['email']
			price = form.cleaned_data['package']
			quantity = form.cleaned_data['quantity']
			manager = form.cleaned_data['manager']
			coin = form.cleaned_data['coin']
			coupon = form.cleaned_data['coupon']

			if price == 4997.0:
				package = "Ultimate Executive"
			elif price == 1997.0:
				package = "Ultimate"
			elif price == 1597.0:
				package = "Bitcoin Blast"

			amount = price * quantity
			if coupon != '':
				coupon_selected = Coupon.objects.filter(coupon_code=coupon)
				frequency = coupon_selected[0].frequency
				Coupon.objects.filter(coupon_code=coupon).update(frequency= frequency-1)
				
				discount_percent = coupon_selected[0].percent
				discount =  (discount_percent * amount) / 100.0
				total_amount = amount - discount
			else:
				total_amount = amount
				discount_percent = 0
			print("AMOUNT")
			print(total_amount)
			#Coinpayment API
			API_KEY = ''
			API_SECRET = ''
			IPN_URL = ''

			post_param = {
				'amount':amount,
				'currency1':'USD',
				'currency2':coin
			}

			client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
			transaction = client.createTransaction(post_param)
			coin_amount = transaction.amount
			status = transaction.status_url
			qrcode = transaction.qrcode_url
			address = transaction.address
			print(transaction)
			#End of coinpayment API
			
			payment_details ={'first_name':first_name,
				'last_name':last_name,
				'company':company,
				'email':email,
				'package':package,
				'quantity':quantity,
				'manager':manager,
				'coin':coin,
				'coupon_amount':discount_percent,
				'amount':total_amount,
				'coin_amount':coin_amount,
				'status':status,
				'qrcode':qrcode,
				'address':address
			}

			History.objects.create(
				first_name = first_name,
				last_name = last_name,
				company = company,
				email = email,
				package = package,
				quantity = quantity,
				manager = manager,
				coin = coin,
				amount = amount,
				user = request.user,
				status = status
			).save()
			return render(request,'payments.html',{'payment_details':payment_details})
	else:
		form = submitForm()

	coupon = Coupon.objects.filter(user=request.user)
	return render(request, 'submitform.html',{'data':form, 'coupon_data':coupon})

@login_required(login_url='/')
def profile_view(request):
	history = History.objects.filter(user=request.user).order_by('-createdAt')
	coupon = Coupon.objects.filter(user=request.user)
	return render(request, 'history.html',{'data':history,'coupon_data':coupon})