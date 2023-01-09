import json
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from products.serializers import ProductSerializer
# Create your views here.

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        
    # data = request.data
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
        
    #     data=ProductSerializer(instance).data
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


