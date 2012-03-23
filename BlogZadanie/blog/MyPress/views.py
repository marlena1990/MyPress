# Create your views here.
#from django.template import Context, loader
from django.shortcuts import render_to_response
from blog.MyPress.models import AnkietaPytania
#from django.http import HttpResponse

def index(request):
    latest_ankieta_list = AnkietaPytania.objects.all().order_by('-czasRozpoczecia')[:5]
    # output = ', '.join([p.pytanieAnkiety for p in latest_ankieta_list])
    #t = loader.get_template('MyPress/index.html')
    #c = Context({
    #    'latest_ankieta_list': latest_ankieta_list,
    #})
    #return HttpResponse(t.render(c))
    #return HttpResponse(output)
    return render_to_response('MyPress/index.html', {'latest_ankieta_list': latest_ankieta_list})
