from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from coinpayment.models import Coupon
import datetime
from django.db.models import Q

def login_view(request):
	today = datetime.datetime.now().date()
	print(today)
	coupon = Coupon.objects.filter(Q(expiry__lte=today) | Q(frequency__lt=1))
	for code in coupon:
		code.delete()

	valuenext = request.POST.get('next')
	if(request.method == 'POST'):
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log the user in
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			login(request, user)

			if valuenext=='':
				return redirect('submitform/')
			else:
				return redirect(valuenext)
	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})

def logout_view(request):
	logout(request);
	return redirect('accounts:login')

def register_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('coinpayment:submitform')
	else:
		form = RegistrationForm()
	return render(request, 'registration.html', {'form':form})

@login_required(login_url="/")
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			return redirect('accounts:login')
		else:
			return redirect('accounts:change_password')

	else:
		form = PasswordChangeForm(user=request.user)
		return render(request, 'change_password.html', {'form': form})

@login_required(login_url="/")
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('accounts:profile')
	else:
		form = EditProfileForm(instance=request.user)
	return render(request,'profile_edit.html',{'form':form})