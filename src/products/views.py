from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)

    context = {
        "object": obj
    }

    # also the above works, or you can add a to_dict() to the model

    return render(request, "products/product_detail.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         form = ProductForm() # re-renders the form with new blank context (clears form)

#     context = {
#         "form": form
#     }

#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     context = {}

#     if request.method == "POST":
#         my_new_title = request.POST.get('title')

#         # Product.objects.create(title=my_new_title)
#         title = request.POST.get('title')

#     return render(request, "products/product_create.html", context)