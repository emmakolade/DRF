from django.urls import path
from products.views import ProductDetailAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDelteAPIView

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('<int:pk>/update', ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete', ProductDelteAPIView.as_view()),
]
