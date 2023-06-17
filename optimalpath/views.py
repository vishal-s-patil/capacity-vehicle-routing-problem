from django.shortcuts import render
from django.http import JsonResponse
from .solver import solve_optimal_path
import json


def home(request):
    return render(request, 'optimal_path.html')


def optimal_path_view(request):
    if request.method == 'POST':
        request_body = json.loads(request.body.decode('utf-8'))

        points = request_body['points']
        source = request_body['source']
        destination = request_body['destination']

        optimal_path = solve_optimal_path(points, source, destination)

        return JsonResponse({'optimal_path': optimal_path})
    return render(request, 'optimal_path.html')
