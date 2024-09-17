"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import pages.views as pages
import products.views as products

urlpatterns = [
    path("home/", pages.home_view, name="home"),
    path("contact/", pages.contact_view, name="contact"),
    path("about/", pages.about_view, name="about"),
    path("social/", pages.social_view, name="social"),
    path("product/", products.product_detail_view, name="product"),
    path('create/', products.product_create_view, name="create_product"),
    path('admin/', admin.site.urls),
]
