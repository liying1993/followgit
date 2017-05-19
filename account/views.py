from django.shortcuts import render
from django.http import HttpResponse
from account.models import Profile
import pdb
# # Create your views here.
def test(request):
    pdb.set_trace()
    varible = request.GET["com"]
    username = Profile.objects.get(username__contain=varible)
    return HttpResponse()
