from django.urls import path, include

from customer.views import customer_home, log_out, crop_prediction

urlpatterns = [
    path('', customer_home, name='customer_home'),
    path('/crop_prediction', crop_prediction, name='customer_crop_prediction'),
    path('log_out/', log_out, name='log_out'),

]