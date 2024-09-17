from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print("REQUEST", request.user)
    # return HttpResponse("<h1>Hello!</h1>") # String of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "contact.html")

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page!</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 44,
        "my_list": [3, 2, 1, "abc"],
        "my_html": "<h1> IM HTML </h1>"
    }

    return render(request, "about.html", my_context)