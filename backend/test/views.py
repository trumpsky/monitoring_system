from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
# from django.views.decorators.csrf import csrf_exempt
from test.models import User

# Create your views here.
# @csrf_exempt
@require_http_methods(['POST'])
def test(request):
    return HttpResponse('hello world')

@require_http_methods(['POST'])
def login_test(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        if user:
            return HttpResponse('login success')
        else:
            return HttpResponse('login failed')
    else:
        return render(request, '')