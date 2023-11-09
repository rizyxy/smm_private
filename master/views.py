from django.http import HttpResponse
from django.template import loader

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(None, request))
