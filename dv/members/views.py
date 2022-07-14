from members.models import Member
from django.http import HttpResponse
import json

def mems(request):
	return HttpResponse(json.dumps(list(Member.objects.values('id', 'first_name', 'last_name'))))
