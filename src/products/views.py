from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product
from .forms import RawProductForm, ProductForm
# Create your views here.


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404  # or return redirect("/")
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

# ]=========================================================================[#


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description
    }
    return render(request, "product/detail.html", context)

# ]=========================================================================[#


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


# ]=========================================================================[#


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)

# ]=========================================================================[#


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'object': obj
#     }
#     return render(request, "products/product_detail.html", context)


# ]=========================================================================[#


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)
