from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Buyer, Debt
from retail.paginators import RetailPaginator
from retail.permissions import IsActive
from retail.serialisers.buyer import BuyerSerializer
from retail.serialisers.debt import DebtSerializer


class DebtCreateAPIView(generics.CreateAPIView):
    """Создание Задолженности"""
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated, IsActive]


class DebtListAPIView(generics.ListAPIView):
    """Просмотр списка Задолженностей"""
    serializer_class = DebtSerializer
    queryset = Debt.objects.all()
    pagination_class = RetailPaginator


class DebtRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр Задолженности по идентификатору (id)"""
    serializer_class = DebtSerializer
    queryset = Debt.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class DebtUpdateAPIView(generics.UpdateAPIView):
    """Изменение Задолженности"""
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated, IsActive]

class DebtDestroyAPIView(generics.DestroyAPIView):
    """Удаление Задолженности"""
    permission_classes = [IsAuthenticated, IsActive]
