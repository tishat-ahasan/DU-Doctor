from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Message
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

# def new_message(request,self):
#     if request.method == 'POST':
#         current_user = request.user.username
#         u = User.objects.get(username = current_user)
#         id = u.Message.id
#         content = request.POST.get('content')
#         print(content)
#         # message_instance = Message()
#         # message_instance.content = content
#         # message_instance.author = self.request.user
#         # message_instance.save(self)
#         return HttpResponseRedirect(reverse('online_advice'))

class MessageListView(ListView):
    model = Message
    template_name = 'OnlineAdvice/online_advice.html'
    context_object_name = 'messages'
    # ordering = ['-date_posted']

class MessageCreateView(CreateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        print("hello");
        # data = form.save
        form.instance.author = self.request.user
        # return super(MessageCreateView,self).form_valid(form)
        return super().form_valid(form)

