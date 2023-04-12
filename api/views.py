# pyright: strict
# Create your views here.
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest):
    return HttpResponse('{ "products": ["product1", "product2"]}')
