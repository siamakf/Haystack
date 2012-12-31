from django.http import Http404, HttpResponse
import datetime

def current(request):
    return HttpResponse("PUSS")

def hello(request):
    return HttpResponse("Hello world")

def hours_ahead(request, offset, offtest):
    try:
        offset = int(offset)
        offtest = int(offtest)
       
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset+offtest)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset+offtest, dt)
    return HttpResponse(html)
