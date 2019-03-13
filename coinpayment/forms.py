from django import forms

PR_CHOICE = [
	(4997.0,'Ultimate Executive - $4997'),
	(1997.0,'Ultimate - $1997'),
	(1597.0,'Bitcoin Blast - $1597'),
]

MANAGER_CHOICE = [
	('Not assigned yet','Not assigned yet'),
	('Alex Thurston','Alex Thurston'),
	('Maximus Green','Maximus Green'),
	('Hugo Billiard','Hugo Billiard'),
	('Wayne Barker','Wayne Barker'),
	('Alex Stinton','Alex Stinton'),
]

QUANTITY = [
	(1,'1'),
	(2,'2'),
	(3,'3'),
]

COIN = [
	('BTC','Bitcoin'),
	('LTC','Litecoin'),
	('ETH','Ether'),
]

class submitForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	company = forms.CharField()
	email = forms.EmailField()
	package = forms.IntegerField(label='Select Package', widget=forms.Select(choices=PR_CHOICE))
	quantity = forms.IntegerField(label='Select Quantity', widget=forms.Select(choices=QUANTITY))
	manager = forms.CharField(label='Select Account Manager', widget=forms.Select(choices=MANAGER_CHOICE))
	coin = forms.CharField(label='Select Coin For Payment', widget=forms.RadioSelect(choices=COIN))
	coupon = forms.CharField(required=False)