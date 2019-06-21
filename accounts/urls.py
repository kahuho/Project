from .views import HomeView
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts import views

urlpatterns = [
              path('',include('sell.urls')),

              url(r'^register/$', views.register, name='register'),
               url (r'^edit/$', views.edit, name='edit'),
              url(r'^login/$',  views.user_login, name='login'),
              url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
              url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout-then-login'),
               # social auth
              url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

            # change passwords ulrs
               url(r'^password-change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
               url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
               #    password reset
               url(r'^password-reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
                url(r'^password-change/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

                url(r'^password-reset_complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

         ]