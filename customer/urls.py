from django.urls import path, include

from customer.views import customer_home, log_out, crop_prediction, crop_prediction_result

urlpatterns = [
    path('', customer_home, name='customer_home'),
    path('/crop_prediction', crop_prediction, name='customer_crop_prediction'),
    path('/crop_prediction_result', crop_prediction_result, name='customer_crop_prediction_result'),
    path('log_out/', log_out, name='log_out'),

]