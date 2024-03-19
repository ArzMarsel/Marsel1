from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import Chat1Message, Host1Message
from .models import ChatMessage, HostMessage


class MyListView(ListView):
    model = HostMessage
    template_name = 'h1.html'
    context_object_name = 'Mylist'


def index2(request):
    if request.method == 'POST':
        form = Host1Message(request.POST)
        if form.is_valid:
            form.save()
            return redirect('host')
    else:
        form = Host1Message()

    return render(request, 'h1.html', {'form': form})


def index1(request):
    if request.method == 'POST':
        form = Chat1Message(request.POST)
        if form.is_valid:
            form.save()
            return redirect('host')
    else:
        form = Host1Message()

    return render(request, 'h1.html', {'form': form})


class MylistView1(ListView):
    model = ChatMessage
    template_name = 'h4.html'
    context_object_name = 'Mylist1'

