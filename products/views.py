from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductCreateUpdateSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """
    View for creating a product.
    Представление для создания продукта.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCreateUpdateSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    View for editing a product.
    Представление для редактирования продукта.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCreateUpdateSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """
    View for deleting a product.
    Представление для удаления продукта.
    """
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
