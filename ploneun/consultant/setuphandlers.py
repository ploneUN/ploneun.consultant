from collective.grok import gs
from ploneun.consultant import MessageFactory as _

@gs.importstep(
    name=u'ploneun.consultant', 
    title=_('ploneun.consultant import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ploneun.consultant.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
