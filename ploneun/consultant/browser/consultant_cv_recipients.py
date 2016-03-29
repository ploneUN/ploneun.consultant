from five import grok
from collective.pdfexport.interfaces import IPDFEmailSource
from Products.CMFCore.interfaces import IContentish
import json
from plone import api
from zope.component.hooks import getSite
from zope.component import getAdapters

grok.templatedir('templates')

class consultant_cv_recipients(grok.View):
    grok.context(IContentish)
    
    
    def __call__(self):
        self.request.response.setHeader("Content-type", "application/json")
        users = api.user.get_users()
        tokens = []
        
        #if 'q' in self.request.keys():
        #    for user in users:
        #        if self.request['q'] in user.getProperty("fullname"):
        #            tokens.append({"id":"%s" % user.getProperty("email").replace(u"'", u"\\'"),
        #                           "name":"%s" % user.getProperty("fullname").replace(u"'", u"\\'")})
                    
        adapters = getAdapters((self.context,), IPDFEmailSource)
        keys = []
        if 'q' in self.request.keys():
            q = self.request['q']
            for name, adapter in adapters:
                keys += adapter.search(q)
        # we will return up to 10 tokens only
        tokens = map(self._tokenize, keys[:10])
        
        return json.dumps(tokens)
    
    def _tokenize(self, key):
        value = key['value'].decode('utf-8')
        title = key['title'].decode('utf-8')

        return {'id': '%s' % value.replace(u"'", u"\\'"),
                'name': '%s' % title.replace(u"'", u"\\'")}
    
    