from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Products
from retail.paginators import RetailPaginator
from retail.permissions import IsActive
from retail.serialisers.products import ProductsSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """Создание Продукта"""
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        new_product = serializer.save()
        #new_contact.owner = self.request.user
        new_product.save()


class ProductsListAPIView(generics.ListAPIView):
    """Просмотр списка Продуктов"""
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    pagination_class = RetailPaginator


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр отдельного Продукта по идентификатору (id)"""
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Изменение Продукта"""
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated, IsActive]

class ProductDestroyAPIView(generics.DestroyAPIView):
    """Удаление Продукта"""
    permission_classes = [IsAuthenticated, IsActive]
