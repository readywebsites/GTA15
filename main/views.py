from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # ✅ this will render your React page
