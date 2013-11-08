from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from ploneun.consultant.interfaces import IProductSpecific
from Products.ATContentTypes.interfaces.file import IATFile
from plone.app.blob.interfaces import IATBlobFile
from Acquisition import aq_parent
from ploneun.consultant.content.consultant import IConsultant

grok.templatedir('templates')

class ContentInConsultant(grok.Viewlet):
    grok.context(IContentish)
    grok.viewletmanager(manager.IBelowContentTitle)
    grok.template('content_in_consultant')
    grok.layer(IProductSpecific)

    def available(self):
        if not (
            IATFile.providedBy(self.context) or 
            IATBlobFile.providedBy(self.context)
            ):
            return False
        return bool(self.consultant())
    
    def consultant(self):
        parent = aq_parent(self.context)
        if IConsultant.providedBy(parent):
            return parent
        return None
        
