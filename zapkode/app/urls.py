from django.urls import path
from .import views
from django.views import View
from app import views
from django.contrib.auth import views as auth_views

from .forms import MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm
urlpatterns = [

    path('', views.Registration,
         name='registration'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='passwordreset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='passwordresetdone.html'), name='password_reset_done'),

    # path('search/',views.search),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='passwordresetconfirmed.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='passwordresetcomplete.html'), name='password_reset_complete'),
    path('welcome/',views.Welcome,name='welcome'),
    path('login/',views.login_user,name='login'),
]
