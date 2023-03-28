from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60*30)(Home.as_view()), name='home'),
    path('home/inzhenernyye-kommunikatsii/', cache_page(60*30)(InzhCons.as_view()), name='inzh'),
    path('home/otdelochnyye-raboty/', cache_page(60*30)(OtdelkaCons.as_view()), name='otdelka'),
    path('home/doma-pod-klyuch/', cache_page(60*60)(HouseCons.as_view()), name='house'),
    path('home/kontakty/', cache_page(60*60)(ContactCons.as_view()), name='contact'),
    path('home/vakansii/', cache_page(60*60)(VacanciesCons.as_view()), name='vacancies'),
    path('home/o-nas/', cache_page(60*60)(AboutUsCons.as_view()), name='about_us'),
    path('home/kategoriya/<str:slug>', cache_page(60*60)(CategoryItem.as_view()), name='category_item'),
    path('home/politika-konfidentsialnosti/', cache_page(60*60)(PoliticaCons.as_view()), name='politica'),
]