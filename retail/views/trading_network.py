from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Link_trading_network, Trading_network
from retail.paginators import RetailPaginator
from retail.permissions import IsActive
from retail.serialisers.link_trading_network import Link_trading_networkSerializer
from retail.serialisers.trading_network import Trading_networkSerializer


class Trading_networkCreateAPIView(generics.CreateAPIView):
    """Создание сети"""
    serializer_class = Trading_networkSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        new_trading_network = serializer.save()
        new_trading_network.save()


class Trading_networkListAPIView(generics.ListAPIView):
    """Просмотр списка Сетей"""
    serializer_class = Trading_networkSerializer
    queryset = Trading_network.objects.all()
    pagination_class = RetailPaginator


class Trading_networkRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр сети по идентификатору (id)"""
    serializer_class = Trading_networkSerializer
    queryset = Trading_network.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class Trading_networkUpdateAPIView(generics.UpdateAPIView):
    """Изменение сети"""
    serializer_class = Trading_networkSerializer
    permission_classes = [IsAuthenticated, IsActive]

class Trading_networkDestroyAPIView(generics.DestroyAPIView):
    """Удаление сети"""
    permission_classes = [IsAuthenticated, IsActive]
