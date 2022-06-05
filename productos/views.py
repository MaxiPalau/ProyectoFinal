from django.shortcuts import render
from productos.models import Productos

# Create your views here.
def productos(request):
    producto = Productos.objects.all()
    print(producto) 
    context = {'producto':producto}
    return render(request, 'productos.html', context=context)

def search_product_view(request):
    print(request.GET)
    productos = Productos.objects.filter(modelo__contains = request.GET['search'])
    context = {'productos':productos}
    return render(request, 'search_product.html', context = context)
    #return render(request, 'search_product.html')
