from django.urls import URLPattern, path
from car import views


urlpatterns = [
    path('get-post-person', views.person_view),
    path('get-post-car', views.car_view),
    path('information', views.information_view)
]