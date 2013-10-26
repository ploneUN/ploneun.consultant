from five import grok
from plone.directives import dexterity, form
from ploneun.consultant.content.consultant import IConsultant

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IConsultant)
    grok.require('zope2.View')
    grok.template('consultant_view')
    grok.name('view')

