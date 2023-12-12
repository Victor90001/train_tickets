from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import requests, datetime
from datetime import datetime, timedelta


def index(request):
    return render(request, 'index.html')


def fetchhandler(request):
    if request.method == 'GET':
        param = {
                'field': 'from',
                'format': 'old',
                't_type_code': 'train'
                }
        if 'part' in request.GET:
            param['part'] = request.GET['part']
        url = 'https://suggests.rasp.yandex.net/by_t_type'
        res = requests.get(url, params=param).json()
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return redirect('index')


def trains(request):
    if request.method == 'POST':
        post_data = request.POST
        api_url = 'https://api.rasp.yandex.net/v3.0/search/'
        headers = {
            'Authorization': 'ea1789a3-16e0-43b7-b275-9b0e76282542'
        }
        params = {
            'from': post_data['inputFromId'],
            'to': post_data['inputToId'],
            'format': 'json',
            'lang': 'ru_RU',
            'date': post_data['inputDate'],
            'transport_types': 'train',
        }
        res = requests.get(api_url, headers=headers ,params=params).json()
        for segment in res['segments']:
            segment['departure'] = datetime.strptime(segment['departure'], '%Y-%m-%dT%H:%M:%S%z')
            segment['arrival'] = datetime.strptime(segment['arrival'], '%Y-%m-%dT%H:%M:%S%z')
            segment['duration'] = (datetime.min+timedelta(seconds=float(segment['duration']))).time()
        context = {
            'from': res['search']['from']['title'],
            'to': res['search']['to']['title'],
            'segments': res['segments'],
        }
        return render(request, 'trains.html', context)
    return redirect('index')


def er404(request):
    raise Http404("There is no page!")
# Create your views here.
