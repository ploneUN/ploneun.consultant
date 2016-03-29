from five import grok
from Products.CMFCore.interfaces import IContentish
import json
from plone import api


grok.templatedir('templates')

class consultantfaceted(grok.View):
    grok.context(IContentish)
    grok.name('consultantfaceted')
    grok.require('zope2.View')
    grok.template('consultantfaceted')
    
    def trim_text(self, value):
        if len(value) > 80:
            return value[:85] + "..."
        return value
    
    
    def get_consultants(self, brains):
        consultants_str = []
        for brain in brains:
            consultants_str.append('id=%s' % brain.UID)
        if consultants_str:
            return '&'.join(consultants_str)
        return ''
        
        
        
    

    
    

    


