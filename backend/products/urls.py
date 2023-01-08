from django.urls import path
from products.views import ProductDetailAPIView, ProductListCreateAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('', ProductListCreateAPIView.as_view()),
]
