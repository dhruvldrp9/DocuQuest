# myapp/views.py

from django.shortcuts import render, redirect
from .forms import UploadPDFForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_pdf.html', {'form': form})  # Replace with your success URL
    else:
        form = UploadPDFForm()
    return render(request, 'upload_pdf.html', {'form': form})


@csrf_exempt  # For development, CSRF protection is disabled; enable in production
def ask_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')

        # Define the URL of your Python server handling the question
        python_server_url = "http://localhost:8001/"

        # Send the question to your Python server
        response = requests.post(python_server_url, json={'question': question})

        # Process the response from your Python server
        if response.status_code == 200:
            response_data = response.json()
            answer = response_data.get('result')
            return JsonResponse({'result': answer})
        else:
            return JsonResponse({'result': 'Sorry, there was an error processing your request.'}, status=500)

    return JsonResponse({'result': 'Method not allowed.'}, status=405)