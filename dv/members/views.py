from members.models import Member
from django.http import HttpResponse
import json

def mems(request):
	data = list(Member.objects.values('id', 'first_name', 'last_name'))
	return HttpResponse(json.dumps(data), content_type="application/json")
