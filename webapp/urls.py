
from django.urls import path
from . import views


app_name = 'webapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('contact/', views.contact_page, name='contact_page'),

    path('about/', views.about_page, name='about_page'),

    path('obavestenja/', views.obavestenja_page, name='obavestenja_page'),

	path('<int:year>/<int:month>/<int:day>/<slug:obavestenje>/', views.obavestenje_detalji, name='obavestenje_detalji'),

	path('finansije/', views.finansije_page, name='finansije_page'),



	path('obavestenja/novo-obavestenje/', views.obavestenje_dodaj, name='obavestenje_dodaj'),



]

