from django.template import loader
from django.http import HttpResponse

def all_shop(request):
    template = loader.get_template('all_shops.html')
    return HttpResponse(template.render(None, request))

def shop_analytics(request):
    template = loader.get_template('shop_analytics.html')
    return HttpResponse(template.render(None, request))

def shop_products(request):
    template = loader.get_template('shop_products.html')
    return HttpResponse(template.render(None, request))

def add_shop(request):
    template = loader.get_template('add_shop.html')
    return HttpResponse(template.render(None, request))