from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Buyer
from retail.paginators import RetailPaginator
from retail.permissions import IsActive
from retail.serialisers.buyer import BuyerSerializer


class BuyerCreateAPIView(generics.CreateAPIView):
    """Создание Покупателя"""
    serializer_class = BuyerSerializer
    permission_classes = [IsAuthenticated, IsActive]

  #  def perform_create(self, serializer):
  #      new_counterparty = serializer.save()
        #new_contact.owner = self.request.user
  #      new_counterparty.save()


class BuyerListAPIView(generics.ListAPIView):
    """Просмотр списка Покупателей"""
    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all()
    pagination_class = RetailPaginator


class BuyerRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр отдельного Покупателя по идентификатору (id)"""
    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class BuyerUpdateAPIView(generics.UpdateAPIView):
    """Изменение Покупателя"""
    serializer_class = BuyerSerializer
    permission_classes = [IsAuthenticated, IsActive]

class BuyerDestroyAPIView(generics.DestroyAPIView):
    """Удаление Покупателя"""
    permission_classes = [IsAuthenticated, IsActive]
