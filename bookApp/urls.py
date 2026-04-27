from django.urls import path
from .views import *

urlpatterns = [
   path('home/', homePage, name='home'),
   path('register/', registerPage, name='register'),
   path('', loginPage, name='login'),
   path('logout/', logoutPage, name='logout'),
   path('profile/', profilePage, name='profile'),
   path('book/', bookPage, name='book'),
   path('sell/', sellBookPage, name='sell'),
]
