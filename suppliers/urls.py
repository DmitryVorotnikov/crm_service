from django.urls import path

from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierCreateAPIView, SupplierListAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, SupplierDestroyAPIView

app_name = SuppliersConfig.name

urlpatterns = [
    # Supplier URLs:
    path('create/', SupplierCreateAPIView.as_view(), name='suppliers_create'),
    path('', SupplierListAPIView.as_view(), name='suppliers_list'),
    path('<int:pk>/', SupplierRetrieveAPIView.as_view(), name='suppliers_get'),
    path('update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='suppliers_update'),
    path('delete/<int:pk>/', SupplierDestroyAPIView.as_view(), name='suppliers_delete'),
]
