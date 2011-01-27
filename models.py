from django.db import models

class TestViewDefinitions:
        
    def __init__(self,appname):
        self._appname = appname
        self._module = None
        
    def __str__(self):
        return( self.name )
                
    def exists(self):
        return( self.module() != None )
    
    def module(self):
        if not self._module:
            try:
                self._module = __import__( self.name() )
            except:
                pass
        return( self._module )
    
    def urls(self):
        module = self.module()
        if not module:
            return []
        return module.testviewdefs.TEST_URLS
    
    def fixtures(self):
        module = self.module()
        if not module:
            return []
        return module.testviewdefs.FIXTURES
    
    def name(self):
        return( "%s.%s" % (self._appname, 'testviewdefs') )