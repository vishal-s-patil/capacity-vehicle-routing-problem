from django.shortcuts import render
from django.http import JsonResponse
from .solver import solve_optimal_path
import json


def home(request):
    return render(request, 'optimal_path.html')


def optimal_path_view(request):
    if request.method == 'POST':
        request_body = json.loads(request.body.decode('utf-8'))

        data = {
            "distance_matrix": request_body['distancesMatrix'],
            "num_vehicles": int(request_body['numberOfVehicles']),
            "depot": 0,
            "vehicle_capacities": [int(request_body['vehicle_capacities'])]*int(request_body['numberOfVehicles']),
            "demands": request_body['demands'],
        }

        # print('data', data)

        optimal_path = solve_optimal_path(data)

        print(optimal_path)

        return JsonResponse({'optimal_path': optimal_path})
    return render(request, 'optimal_path.html')
