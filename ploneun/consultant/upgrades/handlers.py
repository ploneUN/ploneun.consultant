from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade ploneun.consultant to 3',
                description=u'Upgrade ploneun.consultant to 3',
                source='2', destination='3',
                sortkey=1, profile='ploneun.consultant:default')
def to3(context):
    setup = getToolByName(context, 'portal_setup')
    site = getSite().id
    if site in 'eval':
        catalog = getToolByName(context, 'portal_catalog')
        for brain in catalog(portal_type="ploneun.consultant.consultant"):
            obj = brain.getObject()
            del obj.functions
    else:
        setup.runAllImportStepsFromProfile('profile-ploneun.consultant.upgrades:to3')


@gs.upgradestep(title=u'Upgrade ploneun.consultant to 2',
                description=u'Upgrade ploneun.consultant to 2',
                source='1', destination='2',
                sortkey=1, profile='ploneun.consultant:default')
def to2(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-ploneun.consultant.upgrades:to2')
