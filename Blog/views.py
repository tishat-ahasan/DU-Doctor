from django.shortcuts import render

from Blog.models import Article
from .ModelForm import ArticleForm
from django.http import HttpResponse

# Create your views here.

def article_detail_view(request,*args , **kwargs):
    my_form = ArticleForm
    if request.method == "POST":
        Article.objects.create(my_form)
    contex = {
        'form' : my_form
    }
    return render(request,'Blog/article_detail.html',contex)
