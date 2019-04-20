from django.shortcuts import render,get_object_or_404
from .models import Product
from .forms import ProductForm,RawProductForm

# Create your views here.


def dynamic_lookup_view(request,my_id):
    obj = get_object_or_404(Product,id=my_id)
    if request.method=="POST" :
        obj.delete()
    contex = {
        "object" : obj
    }
    return render(request,"product/product_details.html",contex)


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    contex = {
        "form" : my_form
    }
    return render(request, "product/product_create.html", contex)



# def product_create_view(request):
#     if request.method == "POST":
#         new_title = request.POST.get('title')
#         print(new_title)
#     contex = {}
#     return render(request, "product/product_create.html", contex)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     contex = {
#         'form':form
#     }
#     return render(request,"product/product_create.html",contex)

def product_detail_view(request):
    obj = Product.objects.all()
    contex = {
        'object':obj
    }
    return render(request,"product/details.html",contex)