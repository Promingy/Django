from django.urls import path
from .views import default_view

app_name="blog"

# from .views import 

urlpatterns = [
    path("", default_view, name="default-view")
]