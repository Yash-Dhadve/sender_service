import json
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