from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import post
# Create your views here.

# def post_notice_showing(request):
#     return render(request,'PostNotice/post_notice.html')

class showNotice(ListView):
    model = post
    template_name = 'PostNotice/show_notice.html'
    context_object_name = 'posts'
    ordering = ['-post_date']


class postNotice(CreateView):
    model = post
    fields = ['title','description']

    def form_valid(self, form):
        return super().form_valid(form)