from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=(20, 30)) # Show Jürgen

    return render(request, "hello.html", {"name": "Elias", "products": list(queryset)})
