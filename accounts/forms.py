from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput



class UserRegistrationForm(UserCreationForm):
    phoneNumber = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput(), help_text='Enter a Valid Email')
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'last_name','phoneNumber', 'email', 'password1', 'password2')
    #     check if passwords match
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Your passwords do not match")
        return cd['password2']
    # validate if email already exits
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email Already Exists.')
        return email


#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('last_name', 'email')


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('profPic', 'date_of_birth', 'phone_number')
#         widgets ={
#             'date_of_birth': DatePickerInput(format='%Y-%m-%d'),
#         }
class UserEditForm(UserChangeForm):
    email = forms.CharField(widget=forms.TextInput(),required=True)
    last_name = forms.CharField(widget=forms.TextInput())
class ProfileEditForm(UserChangeForm):
    profPic = forms.FileField(widget=forms.FileInput(),required=False)
    date_of_birth = forms.DateTimeField(widget=forms.DateTimeInput())
