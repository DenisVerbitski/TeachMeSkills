import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.decorators.http import require_http_methods
import requests

class MyView(View):
    def get(self, request, *args, **kwargs):
        if kwargs.get('data'):
            number = kwargs["data"]
        else:
            number = 1
        a = [requests.get('https://api.kanye.rest').json()['quote'] for _ in range(int(number))]
        return render(request, 'homework21/homework21.html', {"quotes": a})


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def index(request):
   
    if request.method == 'GET':
        numb = dict(request.GET.items())
        n = numb.get('number')
        nums = n 
        factorial = 1
        while int(n) > 1:
            factorial *= int(n)
            n = int(n) - 1
        back = json.dumps({"number": nums, "factorial": factorial})
        return HttpResponse(back)
    elif request.method == 'POST':
        return f'to get the factorial, you need to send a get request'
