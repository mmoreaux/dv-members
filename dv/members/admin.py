from django.contrib import admin
from members import models
from django.utils.html import format_html_join
from django.urls import reverse



@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
	list_display = ['LA_name', 'birth_date', 'email', 'dms_id', 'paid_contribution']
	list_filter = [
		('dms_id', admin.EmptyFieldListFilter),
		'paid_contribution',
	]
	fieldsets = [
		(None, {'fields': ['first_name', 'last_name', 'birth_date', 'phone_number', 'email']}),
		('Address', {'fields': ['address_city', 'address_street_name', 'address_house_number', 'address_zipcode']}),
		('Administrative details', {'fields': ['dms_id', 'paid_contribution']}),
		('Committees', {'fields': ['DA_chairs_committees', 'DA_in_committees']}),
	]
	readonly_fields = ['DA_chairs_committees', 'DA_in_committees']

	def LA_name(self, member):
		return f'{member.first_name} {member.last_name}'
	LA_name.short_description = 'Name'
	LA_name.admin_order_field = 'last_name'

	def DA_chairs_committees(self, member):
		committees = [(reverse("admin:members_committee_change", args=[c.pk]), c.name) for c in member.chairs_committees.all()]
		return format_html_join(', ', '<a href="{}">{}</a>', committees)
	DA_chairs_committees.short_description = 'Chair for Committees'

	def DA_in_committees(self, member):
		committees = [(reverse("admin:members_committee_change", args=[c.pk]), c.name) for c in member.in_committees.all()]
		return format_html_join(', ', '<a href="{}">{}</a>', committees)
	DA_in_committees.short_description = 'In Committees'



@admin.register(models.Committee)
class CommitteeAdmin(admin.ModelAdmin):
	list_display = ['name', 'LA_description', 'chairman', 'LA_members']

	def LA_description(self, committee):
		truncated = committee.description[:50]
		return truncated if truncated == committee.description else truncated + '...'
	LA_description.short_description = "Description"
	LA_description.admin_order_field = 'description'

	def LA_members(self, committee):
		members = committee.members.values_list('first_name', flat=True)
		names = f'{len(members)}: ' + ', '.join(members)
		truncated = names[:64]
		return truncated if truncated == names else truncated + '...'
	LA_members.short_description = "Members"
