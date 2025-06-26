from django.urls import path
from .views import index  # views.py ma index() view hovu joie

urlpatterns = [
    path('', index, name='home'),  # base URL http://127.0.0.1:8000/
]
