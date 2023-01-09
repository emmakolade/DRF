from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            

class ProductDelteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProductMixinView(ListModelMixin, GenericAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view
def product_alt_view(request, pk=None, * args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
