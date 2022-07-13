from django.db import models

class Member(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True)
	birth_date = models.DateField()
	email = models.EmailField(max_length=100)
	phone_number = models.CharField(max_length=20)
	address_city = models.CharField(max_length=50)
	address_street_name = models.CharField(max_length=100)
	address_house_number= models.CharField(max_length=10)
	address_zipcode = models.CharField(max_length=6)
	dms_id = models.IntegerField(null=True, blank=True)
	paid_contribution = models.BooleanField(default=False)
