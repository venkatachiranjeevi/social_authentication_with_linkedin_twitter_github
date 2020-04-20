import json

from django.shortcuts import render

# Create your views here.

# core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.http import HttpResponse

# Create your views here.
def login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return redirect('/')


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def get_users(request):
    try:
        user_objects = CustomUser.objects.all()
        user_details = [{'username': user.username, 'id': user.id, 'mobileNumber': user.mobile_number} for user in user_objects]
        return HttpResponse(json.dumps(user_details), content_type="application/json")
    except Exception:
        return HttpResponse('Exception in getting user details')

@login_required
def get_user_by_id(request):
    user_id = request.GET.get('userid')
    if not user_id:
        return HttpResponse('No user selected')
    user_details = CustomUser.objects.get(id=user_id)
    return HttpResponse(json.dumps({'username': user_details.username, 'id': user_details.id}) , content_type="application/json")

@login_required
def search_user_by_mobile(request):
    serch_mobile_number = request.GET.get('mobile_number')
    if not serch_mobile_number:
        user_details = CustomUser.objects.all()
    else:
        user_details = CustomUser.objects.filter(mobile_number__contains=serch_mobile_number)
    user_details = [{'username': user.username, 'id': user.id} for user in user_details]
    return HttpResponse(json.dumps(user_details), content_type="application/json")


