
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page),
    path('contact/', contact_page),
    path('price/', price_page),
    path('service/', service_page),

]
