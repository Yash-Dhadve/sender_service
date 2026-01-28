import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_control

import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def status(request):
    return JsonResponse({"status": "sender running"})

@csrf_exempt
def receive_ack(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("✅ ACK received from receiver:", data)

        return JsonResponse({
            "status": "ok",
            "message": "ACK received successfully"
        })

    return JsonResponse({"error": "Invalid method"}, status=405)

def landing_view(request):
    return render(request, 'landing.html')
    