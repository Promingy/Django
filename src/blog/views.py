from django.shortcuts import render, get_object_or_404, redirect, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article
from .forms import ArticleForm

# Create your views here.

#! Class based views
class ArticleListView(ListView):
    #? generic template name looks for <app_name>/model_name>_<view_name>.html eg. blog/article_list.html
    # template_name = "articles/article_list.html"
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

    #? below is if we are using <int:id> over <int:pk>
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = "blog/article_create.html"
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ArticleCreateView(CreateView):
    template_name = "blog/article_create.html"
    form_class = ArticleForm
    queryset = Article.objects.all()
    # success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # def get_success_url(self):
        # return "/" #some path

class ArticleDeleteView(DeleteView):
    template_name = "blog/article_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)
        
    def get_success_url(self):
        return reverse("blog:list-view")

#! this is regular way of doing views
# def article_create_view(request):
#     print("!!!!!!!!!!!!!")
#     form = ArticleForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         form = ArticleForm(request.POST or None)
    
#     context = {
#         "form": form
#     }

#     return render(request, "article_create.html", context)

# def article_list_view(request):
#     queryset = Article.objects.all()

#     context = {
#         "object_list": queryset
#     }

#     return render(request, "article_list.html", context)

# def article_detail_view(request, id):
#     obj = Article.objects.get(id=id)

#     context = {
#         "object": obj
#     }

#     return render(request, "article_detail.html", context)