from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('django_testview.views',
    url(r'/(\S+)/(\d+)$', 'testurl', name='testurl' ),
    url(r'/(\S+)/$', 'testapp', name="show-testurls"),
    url(r'$', 'applist' , name="show-testurl-apps"),
)
