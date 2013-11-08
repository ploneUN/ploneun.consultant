from five import grok
from Products.CMFCore.interfaces import IContentish

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


