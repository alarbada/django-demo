# pyright: strict
# Create your views here.
from django.http import HttpResponse, HttpRequest

def list_products():
    return HttpResponse('{ "products": ["product1", "product2"]}')

def create_product():
    return HttpResponse(status=201)

def products(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return list_products()
    elif request.method == "POST":
        return create_product()
    else:
        return HttpResponse(status=404)
