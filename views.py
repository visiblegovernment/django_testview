from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Context, RequestContext
from django.contrib.gis.measure import D 
from django.conf import settings
from models import TestViewDefinitions

def applist(request):
    apps = []
    for app in settings.INSTALLED_APPS:
        if TestViewDefinitions(app).exists():
            apps.append( app )
    return render_to_response("applist.html",
                {"apps": apps,
                 },
                context_instance=RequestContext(request))    

def testapp(request,app):
    urls = []
    error = None
    definitions = TestViewDefinitions(app)
    if definitions.exists():
        urls = definitions.urls()
    else:
        error = "Failed to import from app %s" % (app)
    return render_to_response("urllist.html",
                {'app':app,
                 "urls": urls,
                 "error":error
                 },
                context_instance=RequestContext(request))    
    
def testurl(request,app,test_id): 
    urls = []
    error = None
    definitions = TestViewDefinitions(app)
    if definitions.exists():
        urls = definitions.urls()
    else:
        error = "Failed to import from app %s" % (app)
    test_id = int(test_id)
    (test_url,test_text) = urls[ test_id ]
    prev = None
    next = None
    if test_id != 0:
        prev = test_id - 1
    if test_id != len(urls) -1:
        next = test_id + 1
    return render_to_response("testview.html",
                {"testurl": test_url,
                 "testtext":test_text,
                 "prev": prev,
                 "next": next,
                 'app': app,
                 "error":error, },
                context_instance=RequestContext(request))    
