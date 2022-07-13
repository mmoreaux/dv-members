from django.contrib import admin
from members import models

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'birth_date', 'email', 'dms_id', 'paid_contribution']
	list_filter = [
		('dms_id', admin.EmptyFieldListFilter),
		'paid_contribution',
	]
admin.site.register(models.Member, MemberAdmin)

class CommitteeAdmin(admin.ModelAdmin):
	list_display = ['name', 'chairman']
admin.site.register(models.Committee, CommitteeAdmin)
