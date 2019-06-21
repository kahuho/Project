from django import forms
from .models import Products, Services, Orders, Growing
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput



class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('ProductName', 'ProductDescription', 'price', 'location','sublocation', 'category', 'unitofsale','image')

    def __init__(self, *args, **kwargs):
            super(ProductsForm, self).__init__(*args, **kwargs)
            self.fields['ProductName'].widget.attrs['class'] = 'form-control'
            self.fields['ProductDescription'].widget.attrs['class'] = 'form-control'
            self.fields['price'].widget.attrs['class'] = 'form-control'
            self.fields['location'].widget.attrs['class'] = 'form-control'
            self.fields['unitofsale'].widget.attrs['class'] = 'form-control'
            self.fields['category'].widget.attrs['class'] = 'form-control'

class GrowingForm(forms.ModelForm):
    class Meta:
        model = Growing
        fields = ('ProductName', 'DescribeFarming', 'MaturityDate', 'price', 'location', 'category', 'unitofsale', 'image')
        widgets= {
            'MaturityDate': DatePickerInput(format='%Y-%m-%d'),
        }
    def __init__(self, *args, **kwargs):
        super(GrowingForm, self).__init__(*args, **kwargs)
        self.fields['ProductName'].widget.attrs['class'] = 'form-control'
        self.fields['DescribeFarming'].widget.attrs['class'] = 'form-control'
        self.fields['MaturityDate'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['unitofsale'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('title','location', 'description', 'period')
        widgets = {
            'period': DatePickerInput(format='%Y-%m-%d'),  # default date-format %m/%d/%Y will be used
        }

    def __init__(self, *args, **kwargs):
            super(ServicesForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs['class'] = 'form-control'
            self.fields['location'].widget.attrs['class'] = 'form-control'
            self.fields['description'].widget.attrs['class'] = 'form-control'
            self.fields['period'].widget.attrs['class'] = DatePickerInput()


class OrdersForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('title', 'category', 'description','period', 'location')
        widgets = {
            'period': DatePickerInput(format='%Y-%m-%d'),  # default date-format %m/%d/%Y will be used
        }

    def __init__(self, *args, **kwargs):
        super(OrdersForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        # self.fields['period'].widget.attrs['class'] = 'form-control'


