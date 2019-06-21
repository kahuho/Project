from . import views
from django.conf.urls import url
from sell.views import LatestProducts, LatestServices, Market, Orders_view, ProductDetailView, growing
from django.urls import path
from sell.views import newsView, profile

urlpatterns = [
    url(r'^sell/$', views.sell, name="sell"),
    path('ordersForm/', views.orders, name='ordersform'),
    path('serviceForm/', views.service, name='serviceform'),
    path('', views.LatestProducts,name='home'),
    path('LatestServices/', views.LatestServices, name='LatestServices'),
    path('news_json/', views.News, name='news_json'),
    path('news/', newsView.as_view(), name='news'),
    path('market/', Market.as_view(), name='market'),
    path('orders/', Orders_view.as_view(), name='orders'),
    path('services/',  LatestServices.as_view(), name='services'),
    path('single_product/<pk>/', views.ProductDetailView, name='single_product'),
    path('user_profile/<username>', views.profile, name='seller_profile'),
    path('growingForm/', views.growing, name='growingForm'),

]