from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('home/inzhenernyye-kommunikatsii/', InzhCons.as_view(), name='inzh'),
    path('home/otdelochnyye-raboty/', OtdelkaCons.as_view(), name='otdelka'),
    path('home/doma-pod-klyuch/', HouseCons.as_view(), name='house'),
    path('home/kontakty/', ContactCons.as_view(), name='contact'),
    path('home/vakansii/', VacanciesCons.as_view(), name='vacancies'),
    path('home/o-nas/', AboutUsCons.as_view(), name='about_us'),
    path('home/kategoriya/<str:slug>', CategoryInzh.as_view(), name='category_item'),
    path('home/politika-konfidentsialnosti/', PoliticaCons.as_view(), name='politica'),
]