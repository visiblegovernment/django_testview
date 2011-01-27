from mainapp.models import Ward,Councillor,EmailRule
from django.db.models.signals import post_syncdb
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from django_testview.models import TestViewDefinitions
from django.conf import settings

def load_testurl_fixtures(sender, **kwargs):
    if kwargs['app'].__name__ != 'testview.models':
        return
    for app in settings.INSTALLED_APPS:
        definitions = TestViewDefinitions(app)
        if definitions.exists():
            fixtures = definitions.fixtures()
            call_command('loaddata', *fixtures, **{'verbosity': 1})
        
    
post_syncdb.connect(load_testurl_fixtures)
