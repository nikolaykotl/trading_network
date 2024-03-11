from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Link_trading_network
from retail.paginators import RetailPaginator
from retail.permissions import IsActive
from retail.serialisers.link_trading_network import Link_trading_networkSerializer


class Link_trading_networkCreateAPIView(generics.CreateAPIView):
    """Создание Звена сети"""
    serializer_class = Link_trading_networkSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        new_link = serializer.save()
        #new_contact.owner = self.request.user
        new_link.save()


class Link_trading_networkListAPIView(generics.ListAPIView):
    """Просмотр списка Звеньев"""
    serializer_class = Link_trading_networkSerializer
    queryset = Link_trading_network.objects.all()
    pagination_class = RetailPaginator


class Link_trading_networkRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр Звена сети по идентификатору (id)"""
    serializer_class = Link_trading_networkSerializer
    queryset = Link_trading_network.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class Link_trading_networkUpdateAPIView(generics.UpdateAPIView):
    """Изменение данных Звена"""
    serializer_class = Link_trading_networkSerializer
    permission_classes = [IsAuthenticated, IsActive]

class Link_trading_networkDestroyAPIView(generics.DestroyAPIView):
    """Удаление Звена"""
    permission_classes = [IsAuthenticated, IsActive]
