

# Create your views here.
from django.views.generic import ListView, TemplateView
from urllib3 import request
from django.views.generic import View
from django.utils import timezone
from .render import Render

from django.shortcuts import render, redirect,get_object_or_404
from .models import Products, Orders, Services
from .forms import ProductsForm, ServicesForm, OrdersForm, GrowingForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.conf import urls
from newsapi import NewsApiClient
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import CreateView
# # Create your views here.
# view for form used to sell products
@login_required
def sell(request):
     if request.method == 'POST':
          form = ProductsForm(request.POST, request.FILES)
          if form.is_valid():
              form_instance = form.save(commit=False)
              user = request.user
              form_instance.user = user
              form_instance.save()


              return redirect('home')

     else:
         form = ProductsForm()
         return render(request, 'sell/products_form.html', {'form': form})
#      view for form to sell growing produce
def growing(request):
    if request.method =='POST':
        form = GrowingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = GrowingForm()
        return render(request, 'sell/growing_form.html', {'form':form})

# view for the form used to request a service
@login_required(redirect_field_name='login')
def service(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('orders')
    else:
        form = ServicesForm()
        return  render(request, 'sell/services_form.html', {'form': form})

# view for the form used to make an order
@login_required
def orders(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('home')

    else:
        form = OrdersForm()
        return  render(request, 'sell/orders_form.html', {'form': form})

# def latest_products (request):
#         latestProducts = Products.objects.all()[:4]
#         print(latestProducts)
#         context = {'latestProducts': latestProducts}
#         return render(request, 'accounts/home.html', context)
# ORDERS VIEWS
# view for displaying latest products on the home page

# view for displaying latest orders on the orders page

class Orders_view(ListView):
    context_object_name = 'orders'
    template_name = 'sell/orders.html'
    def get_queryset(self):
        return Orders.objects.all()[:4]
# view for new orders in home page

class LatestOrders(ListView):
    context_object_name = 'latestOrders'

    template_name = 'accounts/home.html'



    def get_queryset(self):
        dt = Orders.objects.all()[:4]
        print(dt)
        return  dt


#view for displaying latest services on the home page
class LatestServices(ListView):
    context_object_name = 'latestServices'
    template_name = 'sell/services.html'

    def get_queryset(self):
        return Services.objects.all()[:12]

# This is the market view
class Market(ListView):
    context_object_name = 'market'
    template_name = 'sell/market.html'

    paginate_by = 12
    # paginator = Paginator(context_object_name, 12)
    # # page = request.GET.get('page')
    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(paginator.num_pages)
    #
    # index = products.number - 1
    # max_index = len(paginator.page_range)
    # start_index = index - 5 if index >= 5 else 0
    # end_index = index + 5 if index <= max_index - 5 else max_index
    # page_range = paginator.page_range[start_index:end_index]

    def get_queryset(self):
        return Products.objects.all()[:12]


#     latest products on home page
# class LatestProducts(ListView):
#     context_object_name = 'latestProducts'
#     template_name = 'accounts/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(LatestProducts, self).get_context_data(**kwargs)
#         orders = Products.objects.all()[:4]
#
#         context.update({
#             'latestOrders': orders,
#         })
#         return context
#
#     def get_queryset(self):
#         return Products.objects.all()[:4]

def LatestProducts(request):
    latesProducts = Products.objects.all()[:4]
    orders = Orders.objects.all()[:4]
    services = Services.objects.all()[:4]
    return render(request, 'accounts/home.html',{'latestProducts':latesProducts, 'latestOrders':orders, 'services': services})


def ProductDetailView(request, pk):
    product = get_object_or_404(Products, pk=pk)


    return render(request, 'sell/single_product.html', {'product': product})

# Detailed view for a single product
# class ProductDetailView(DetailView):
#     model = Products
#     template_name = 'sell/single_product.html'




def News():
    while True:
        newsapi = NewsApiClient(api_key='7afe78e453a64e3ca55b795fdf8f0f04')

        agric_articles = newsapi.get_everything(q='agriculture',

                                                # domains='bbc.co.uk,techcrunch.com',
                                                from_param='2019-04-25',
                                                to='2019-04-05',
                                                # category = 'science, technology',
                                                language='en',
                                                )

        return JsonResponse(agric_articles)
        # print(agric_articles)
        # json_status = agric_articles['status']
        # if json_status == 'ok':
        #     for article in agric_articles['articles'][:10]:
        #         print(article)
class newsView(TemplateView):
    template_name = 'sell/news.html'


#     view to print pdfs
class Pdf(View):

    def get(self, request, ):
        products = Products.objects.all()
        today = timezone.now()
        seller =Products.user
        params = {
            'today': today,
            'products': products,
            'request': request,
            'seller': seller
        }
        return Render.render('sell/pdf.html', params)




# view for user to see client profile
def profile(request, username):
    profile = User.objects.get(id=username)
    posts = Products.objects.filter(user=profile).count
    print(profile)

    context = {'posts': posts, 'profile': profile}
    return render(request, 'accounts/profile.html', context)









