from django.urls import path

from retail.views.contacts import ContactCreateAPIView, ContactListAPIView, \
    ContactRetrieveAPIView, ContactUpdateAPIView, ContactDestroyAPIView
from retail.views.buyer import BuyerCreateAPIView, BuyerListAPIView, BuyerRetrieveAPIView, \
    BuyerUpdateAPIView, BuyerDestroyAPIView
from retail.views.debt import DebtCreateAPIView, DebtListAPIView, DebtRetrieveAPIView, DebtUpdateAPIView, \
    DebtDestroyAPIView
from retail.views.supplier import SupplierCreateAPIView, SupplierListAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView
from retail.views.link_trading_network import Link_trading_networkCreateAPIView, Link_trading_networkListAPIView, Link_trading_networkRetrieveAPIView, Link_trading_networkUpdateAPIView, \
    Link_trading_networkDestroyAPIView
from retail.views.products import ProductCreateAPIView, ProductsListAPIView, ProductRetrieveAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView
from retail.views.trading_network import Trading_networkCreateAPIView, Trading_networkListAPIView, \
    Trading_networkRetrieveAPIView, Trading_networkUpdateAPIView, Trading_networkDestroyAPIView

app_name="retail"

urlpatterns = [
    path('contact/create/', ContactCreateAPIView.as_view(),
         name='contact_create'),
    path('contacts/', ContactListAPIView.as_view(), name='contacts_list'),
    path('contact/<int:pk>/', ContactRetrieveAPIView.as_view(),
         name='contact_detail'),
    path('contact/update/<int:pk>/', ContactUpdateAPIView.as_view(),
         name='contact_update'),
    path('contact/delete/<int:pk>/', ContactDestroyAPIView.as_view(),
         name='contact_delete'),
    path('supplier/create/', SupplierCreateAPIView.as_view(),
         name='supplier_create'),
    path('suppliers/', SupplierListAPIView.as_view(), name='supplier_list'),
    path('supplier/<int:pk>/', SupplierRetrieveAPIView.as_view(),
         name='supplier_detail'),
    path('supplier/update/<int:pk>/', SupplierUpdateAPIView.as_view(),
         name='supplier_update'),
    path('supplier/delete/<int:pk>/', SupplierDestroyAPIView.as_view(),
         name='supplier_delete'),
    path('buyer/create/', BuyerCreateAPIView.as_view(),
         name='buyer_create'),
    path('buyer/', BuyerListAPIView.as_view(), name='buyers_list'),
    path('buyer/<int:pk>/', BuyerRetrieveAPIView.as_view(),
         name='buyer_detail'),
    path('buyer/update/<int:pk>/', BuyerUpdateAPIView.as_view(),
         name='buyer_update'),
    path('buyer/delete/<int:pk>/', BuyerDestroyAPIView.as_view(),
         name='buyer_delete'),
    path('link_trading_network/create/', Link_trading_networkCreateAPIView.as_view(),
         name='link_trading_network_create'),
    path('link_trading_network/', Link_trading_networkListAPIView.as_view(), name='links_trading_network_list'),
    path('link_trading_network/<int:pk>/', Link_trading_networkRetrieveAPIView.as_view(),
         name='link_trading_network_detail'),
    path('link_trading_network/update/<int:pk>/', Link_trading_networkUpdateAPIView.as_view(),
         name='link_trading_network_update'),
    path('link_trading_network/delete/<int:pk>/', Link_trading_networkDestroyAPIView.as_view(),
         name='link_delete'),
    path('product/create/', ProductCreateAPIView.as_view(),
         name='product_create'),
    path('products/', ProductsListAPIView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(),
         name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(),
         name='product_update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(),
         name='product_delete'),
    path('debt/create/', DebtCreateAPIView.as_view(),
         name='debt_create'),
    path('debts/', DebtListAPIView.as_view(), name='debts_list'),
    path('debt/<int:pk>/', DebtRetrieveAPIView.as_view(),
         name='debt_detail'),
    path('debt/update/<int:pk>/', DebtUpdateAPIView.as_view(),
         name='debt_update'),
    path('debt/delete/<int:pk>/', DebtDestroyAPIView.as_view(),
         name='debt_delete'),
    path('trading_network/create/', Trading_networkCreateAPIView.as_view(),
         name='trading_network_create'),
    path('trading_networks/', Trading_networkListAPIView.as_view(), name='trading_networks_list'),
    path('trading_network/<int:pk>/', Trading_networkRetrieveAPIView.as_view(),
         name='trading_network_detail'),
    path('trading_network/update/<int:pk>/', Trading_networkUpdateAPIView.as_view(),
         name='trading_network_update'),
    path('trading_network/delete/<int:pk>/', Trading_networkDestroyAPIView.as_view(),
         name='trading_network_delete'),
]
