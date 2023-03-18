from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('inzh/', InzhCons.as_view(), name='inzh'),
    path('otdelka/', OtdelkaCons.as_view(), name='otdelka'),
    path('turnkey-houses/', HouseCons.as_view(), name='house'),
    path('contacts/', ContactCons.as_view(), name='contact'),
    path('vacancies/', VacanciesCons.as_view(), name='vacancies'),
    path('about-us/', AboutUsCons.as_view(), name='about_us'),
    path('kategoriya/<str:slug>', CategoryInzh.as_view(), name='category_item'),
]