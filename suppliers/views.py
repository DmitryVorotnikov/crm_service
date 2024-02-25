from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from suppliers.models import Supplier
from suppliers.serializers import SupplierCreateUpdateSerializer, SupplierListRetrieveSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    """
    View for creating a supplier.
    Представление для создания поставщика.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierCreateUpdateSerializer


class SupplierListAPIView(generics.ListAPIView):
    """
    View for viewing the list of all suppliers.
    Представление для просмотра списка всех поставщиков.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierListRetrieveSerializer
    queryset = Supplier.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('name', 'country', 'city',)
    search_fields = ('name', 'country', 'city',)
    ordering_fields = ('who_is_the_supplier', 'name', 'country', 'city',)


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """
    View for viewing a single supplier.
    Представление для просмотра одного поставщика.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierListRetrieveSerializer
    queryset = Supplier.objects.all()


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """
    View for editing a supplier.
    Представление для редактирования поставщика.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierCreateUpdateSerializer
    queryset = Supplier.objects.all()


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """
    View for deleting a supplier.
    Представление для удаления поставщика.
    """
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
