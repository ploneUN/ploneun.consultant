from five import grok
from plone.directives import dexterity, form
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets.interfaces import IAboveContent
from Products.CMFCore.interfaces import IFolderish

grok.templatedir('templates')

class FacetednavExportscsv(grok.Viewlet):
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContent)
    grok.template('con_facetednav_exportcsv')
    grok.context(IFolderish)
    