from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# model for the list of counties
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


COUNTIES = (
               ('Baringo', 'BARINGO'),
               ('Bomet','BOMET'),
               ('Bungoma', 'BUNGOMA'),
               ('Busia', 'BUSIA'),
               ('Elegeyo Marakwet', 'ELGEYO MARAKWET'),
               ('Embu', 'EMBU'),
               ('Garissa', 'GARISSA'),
               ('Isiolo', 'ISIOLO'),
               ('Homa Bay', 'HOMA BAY'),
               ('Kajiado', 'KAJIADO'),
               ('Kakamega', 'KAKAMEGA'),
               ('Kericho', 'KERICHO'),
               ('Kiambu', 'KIAMBU'),
               ('Kilifi', 'KILIFI'),
               ('Kirinyaga', 'KIRINYAGA'),
               ('Kisii', 'KISII'),
               ('Kisumu', 'KISUMU'),
               ('Kitui', 'KITUI'),
               ('Kwale', 'KWALE'),
               ('Laikipia', 'LAIKIPIA'),
               ('Bungoma', 'BUNGOMA'),
               ('Lamu', 'LAMU'),
               ('Machakos', 'MACHAKOS'),
               ('Makueni', 'MAKUENI'),
               ('mandera', 'MANDERA'),
               ('meru', 'MERU'),
               ('migori', 'MIGORI'),
               ('marsabit', 'MARSABIT'),
               ('mombasa', 'MOMBASA'),
               ('muranga', 'MURANGA'),
               ('nairobi', 'NAIROBI'),
               ('nakuru', 'NAKURU'),
               ('nandi', 'NANDI'),
               ('narok', 'NAROK'),
               ('nyamira', 'NYAMIRA'),
               ('nyandarua', 'NYANDARUA'),
               ('nyeri', 'NYERI'),
               ('samburu', 'SAMBURU'),
               ('siaya', 'SIAYA'),
               ('taita taveta', 'TAITA TAVETA'),
               ('tana river', 'TANA RIVER'),
               ('tharaka nithi', 'THARAKA NITHI'),
               ('trans nzoia', 'TRANS NZOIA'),
               ('turkana', 'TURKANA'),
               ('uasin gishu', 'UASIN GISHU'),
               ('vihiga', 'VIHIGA'),
               ('wajir', 'WAJIR'),
               ('west pokot', 'WEST POKOT'),

            )
# class Category (models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'
#     def __str__(self):
#         return self.name
#     def get_absolute_url(self):
#         return reverse('sell:product_list_by_category', args=[self.slug])

CATEGORIES = (
    ('equipment', 'FARM EQUIPMENT'),
    ('cereals', 'CEREALS'),
    ('vegetables', 'VEGETABLES'),
    ('livestock', 'LIVESTOCK'),
    ('other', 'OTHER'),
    ('cash crops', 'CASH CROPS'),
    ('agrochemicals', 'AGROCHEMICALS'),
    ('fruits', 'FRUITS'),
    (' fertilizers', 'FERTILIZERS'),
    ('fishery', 'FISHERY'),

)

class Products(models.Model):

    UNIT = (
        ('whole', 'whole unit'),
        ('item', 'per single item'),
    )


    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ProductDescription = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(choices = COUNTIES, max_length=300, default='Nairobi')
    category = models.CharField( choices = CATEGORIES, max_length=10, default='other')
    # category = models.ForeignKey(Category, related_name='products')

    unitofsale = models.CharField(max_length=10, choices=UNIT)
    image = models.FileField(upload_to='products_images/', blank=True)
    sublocation = models.CharField(max_length=100, default='Njoro')
    created= models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,db_index=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

# Growing produce model
class Growing(models.Model):

    UNIT = (
        ('whole', 'whole unit'),
        ('item', 'per single item'),
    )


    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(choices = COUNTIES, max_length=300, default='Nairobi')
    category = models.CharField( choices = CATEGORIES, max_length=10, default='other')
    image = models.FileField(upload_to='products_images/', blank=True)
    created= models.DateTimeField(auto_now_add=True)
    unitofsale = models.CharField(max_length=10, choices=UNIT)
    sublocation = models.CharField(max_length=100, default='Njoro')
    MaturityDate = models.DateTimeField(auto_now=False)
    DescribeFarming = models.TextField(max_length=450, blank=False)
    slug = models.SlugField(max_length=200,db_index=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)


class Services (models.Model):
    title = models.CharField(max_length=75)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="2")
    location = models.CharField(choices=COUNTIES, max_length=300, default='Nairobi')
    period = models.DateTimeField(auto_now=False)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True )



class Orders (models.Model):
    category = models.CharField(choices= CATEGORIES, max_length=10, default='other' )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="2")
    location = models.CharField(choices=COUNTIES, max_length=150, default='Nairobi')
    description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, default='other')
    period = models.DateTimeField(auto_now=False)




from django.db import models

# Create your models here.
