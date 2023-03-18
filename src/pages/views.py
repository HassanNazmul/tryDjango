from django.shortcuts import render
# Create your views here.


def index_view(request, *args, **kwargs):
    return render(None, "index.html", {})


def about_view(request, *args, **kwargs):
    return render(None, "about.html", {})


def contact_view(request, *args, **kwargs):
    return render(None, "contact.html", {})
