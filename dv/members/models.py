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

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Committee(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	chairman = models.ForeignKey('Member', on_delete=models.PROTECT, related_name='chairs_committees')
	members = models.ManyToManyField('Member', related_name='in_committees')

	def __str__(self):
		return self.name
