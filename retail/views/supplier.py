from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Supplier
from retail.paginators import RetailPaginator
from retail.permissions import IsActive
from retail.serialisers.supplier import SupplierSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    """Создание Поставщика"""
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        new_supplier = serializer.save()
        new_supplier.save()


class SupplierListAPIView(generics.ListAPIView):
    """Просмотр списка Поставщиков"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    pagination_class = RetailPaginator


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр Поставщика по идентификатору (id)"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """Изменение Поставщика"""
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActive]

class SupplierDestroyAPIView(generics.DestroyAPIView):
    """Удаление Поставщика"""
    permission_classes = [IsAuthenticated, IsActive]
