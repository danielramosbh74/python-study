from django.urls import path

from .views import index, contato

urlpatterns = [
    path('', ('index.html')),
    path('contato', ('contato.html')),
]