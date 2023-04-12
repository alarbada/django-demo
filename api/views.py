# pyright: strict

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest

import json
from typing import List, TypedDict
from decimal import Decimal

from .models import Product

ProductData = TypedDict("ProductData", {
    "title": str,
    "description": str,
    "price": float
})

def list_products() -> HttpResponse:
    products = Product.objects.get_queryset()

    productsData: List[ProductData] = []
    for product in products:
        data = ProductData(
            title=product.title,
            description=product.description,
            price=float(product.price),
        )
        productsData.append(data)

    serialized = json.dumps(productsData)
    res = HttpResponse(serialized)
    res["Content-Type"] = "application/json"
    res.status_code = 200

    return res

# The url does not exist, the exercise assumes that that endpoint is already implemented
@login_required(login_url="/login")
def create_product(req: HttpRequest) -> HttpResponse:
    # read request body into product
    body = req.body.decode("utf-8")
    data = json.loads(body)

    product = Product()
    product.title = data["title"]
    product.description = data["description"]
    product.price = Decimal(data["price"])
    product.save()

    return HttpResponse(status=201)

# This django app is an api server, so it doesn't need csrf protection.
@csrf_exempt
def products(req: HttpRequest) -> HttpResponse:
    try:
        if req.method == "GET":
            return list_products()
        elif req.method == "POST":
            return create_product(req)
        else:
            return HttpResponse(status=404)
    except:
        return HttpResponse(status=500)
