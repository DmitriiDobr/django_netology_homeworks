from django.shortcuts import render, redirect
from django.shortcuts import render
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    parameter = request.GET.get('sort')
    if parameter == 'name':
        phones = Phone.objects.order_by('name')
    elif parameter == 'min_price':
        phones = Phone.objects.order_by('price')
    elif parameter == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones,
    }

    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    print(slug)
    phone = Phone.objects.get(slug = slug)
    print(phone)

    context = {
        'phone': phone
    }
    return render(
        request,
        'product.html',
        context
    )