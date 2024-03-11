from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Contacts
from retail.paginators import RetailPaginator
from retail.permissions import IsActive
from retail.serialisers.contacts import ContactsSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    """Создание Контактов"""
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        new_contact = serializer.save()
        #new_contact.owner = self.request.user
        new_contact.save()


class ContactListAPIView(generics.ListAPIView):
    """Просмотр списка данных Контактов"""
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    pagination_class = RetailPaginator


class ContactRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр данных отдельного Контакта по идентификатору (id)"""
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactUpdateAPIView(generics.UpdateAPIView):
    """Изменение данных Контакта"""
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, IsActive]

class ContactDestroyAPIView(generics.DestroyAPIView):
    """Удаление Контакта"""
    permission_classes = [IsAuthenticated, IsActive]
