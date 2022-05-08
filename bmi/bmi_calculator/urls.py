from django.urls import path,include

from bmi_calculator.views import Home,Calculate
from django.views.generic import TemplateView

urlpatterns = [
    path('', Home.as_view() ,name='home'),
    path('bmi-calculator', Calculate.as_view() ,name='bmi_calculate'),
]