from django.urls import path
from core.views import index
from . import views

urlpatterns = [
    path('campaigns/user/<slug:author>/<slug:url>', views.detail, name='post_detail'),
    path('campaigns', index, name='index'),
    path('campaigns/user/<slug:slug>', views.user, name='user'),
    path('campaigns/user/<slug:author>/paymenthandler/<slug:url>', views.paymenthandler, name='paymenthandler'),
]