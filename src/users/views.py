from django.shortcuts import render
from .models import User
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User  # Import your User model

@csrf_exempt  # Remove this if using Django's default CSRF setup
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            full_name = data.get("full_name")
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not all([full_name, username, email, password]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            # Create user (adjust this based on your user model)
            user = User.objects.create_user(username=username, email=email, password=password)
            user.full_name = full_name
            user.save()

            return JsonResponse({"message": "User registered successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)