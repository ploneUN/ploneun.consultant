from inigo.redirecttocontainer.base import BaseRedirector
from five import grok
from Products.ATContentTypes.interfaces.file import IATFile
from plone.app.blob.interfaces import IATBlobFile
from ploneun.consultant.content.consultant import IConsultant

class RedirectFileToMissionReport(BaseRedirector):
    grok.context(IATFile)
    grok.name('ploneun.consultant.redirectfiletoconsultant')
    container_iface = IConsultant
    direct_parent = True


class RedirectBlobFileToMissionReport(BaseRedirector):
    grok.context(IATBlobFile)
    grok.name('ploneun.consultant.redirectblobfiletoconsultant')
    container_iface = IConsultant
    direct_parent = True
