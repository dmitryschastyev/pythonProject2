
from django.urls import path

from .views import main_view, departure_view, tour_view, custom_handler404, custom_handler500
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', main_view, name='index'),
    path('/departure/<str:departure>/', departure_view, name='departure'),
    path('/tour/<int:id>/', tour_view, name='tour')
]