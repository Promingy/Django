from django.urls import path

# import .views as products
from .views import product_list_view, product_create_view, product_detail_view, product_update_view, product_delete_view

urlpatterns = [
    path("", product_list_view, name="products"),
    path("create/", product_create_view, name="product-create"),
    path("<int:id>/", product_detail_view, name="product-detail"),
    path("<int:id>/update/", product_update_view, name="product-update"),
    path("<int:id>/delete/", product_delete_view, name="product-delete"),
]
