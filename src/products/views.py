from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)

    context = {
        "object": obj
    }

    # also the above works, or you can add a to_dict() to the model

    return render(request, "products/product_detail.html", context)

# def product_create_view(request): 
# """
    # This is for a forms.Form
# """
#     my_form = RawProductForm()

#     if request.method == "POST":
#         my_form = RawProductForm(request.POST) # Passing request.POST adds validations errs

#         if my_form.is_valid():
#             # now data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data) # turn cleaned data into kwarg
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)

#     context = {
#         "form": my_form
#     }

#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # """
#         # This is for a forms.ModelForm
#     # """
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

def product_create_view(request): #/ Render initial Data
    initial_data = {
        "title": "My initial title",
        "description": "This is the coolest description ever"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)

    if form.is_valid():
        form.save()
        form = ProductForm(None, initial=initial_data, instance=obj)

    context = {
        "form": form
    }

    return render(request, "products/product_create.html", context)

def product_update_view(request, id):
    obj = get_object_or_404(Produt, id=id)
    form = ProductForm(request.POST or None)

    if form.iv_valid():
        form.save()
    
    context = {
        "form": form
    }

    return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id) # preferred method to handle not found exception and lookup, the below also works

    #! this is not the recommend way to look up items
    # obj = Product.objects.get(id=id)

    #/ the below works but is more tedious to write
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }

    return render(request, "products/product_detail.html", context)

def product_delete_view(request,id):
    obj = get_object_or_404(Product, id=id)

    # POST REQUEST
    if request.method == "POST":
        #confirming delete
        obj.delete()
        return redirect("/home/")

    context={
        "object": obj
    }

    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() # List
    context = {
        "object_list": queryset
    }

    return render(request, 'products/product_list.html', context)