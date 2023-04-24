from django.urls import path, include

from customer.views import customer_home

urlpatterns = [
    path('', customer_home, name='customer_home'),

]