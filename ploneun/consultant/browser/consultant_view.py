from five import grok
from plone.directives import dexterity, form
from ploneun.consultant.content.consultant import IConsultant
from ploneun.consultant.vocabulary import resolve_value
from AccessControl import getSecurityManager
from Products.CMFCore import permissions
grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IConsultant)
    grok.require('zope2.View')
    grok.template('consultant_view')
    grok.name('view')

    def detail_fields(self):
        fields = []

        if self.context.dob:
            fields.append({
                'id': 'dob',
                'title': 'Date of Birth',
                'render': self.context.dob.strftime('%e %B %Y')
            })

        fields.append({
            'id': 'gender',
            'title': 'Gender',
            'render': self.context.gender
        })

        themes = getattr(self.context, 'ilo_themes', [])
        if themes:
            fields.append({
                'id': 'themes',
                'title': 'Thematic Area(s) of Expertise',
                'render': '<ul>%s</ul>' % ''.join([
                    '<li>%s</li>' % i for i in themes
                ])
            })

        subject_expertise = getattr(self.context, 'ilo_subject_expertise', [])
        if subject_expertise:
            fields.append({
                'id': 'subject_expertise',
                'title': 'Subject Expertise',
                'render': '<ul>%s</ul>' % ''.join([
                    '<li>%s</li>' % i for i in subject_expertise
                ])
            })

        functions = getattr(self.context, 'functions', [])
        if functions:
            fields.append({
                'id': 'functions',
                'title': 'Job Functions',
                'render': '<ul>%s</ul>' % ''.join([
                    '<li>%s</li>' % resolve_value(self.context,
                        i, 'ploneun.consultant.function') for i in functions
                ])
            })

#        if self.context.years_experience:
#            fields.append({
#                'id': 'years_experience',
#                'title': 'Years of Experience',
#                'render': str(self.context.years_experience)
#            })
    
        languages = getattr(self.context, 'languages', [])
        if languages:
            fields.append({
                'id': 'languages',
                'title': 'Languages Spoken',
                'render': '<ul>%s</ul>' % ''.join([
                    '<li>%s</li>' % resolve_value(self.context,
                        i, 'ploneun.consultant.languages') for i in languages
                ])
            })

        return fields
   
    def contact_fields(self):
        fields = []

        fields.append({
            'id': 'email',
            'title': 'Email',
            'render': self.context.email
        })

        if self.context.phone:
            fields.append({
                'id': 'phone',
                'title': 'Phone',
                'render': self.context.phone
            })
    
        if self.context.skype:
            fields.append({
                'id':'skype',
                'title': 'Skype',
                'render': self.context.skype
            })

        if self.context.street_address:
            fields.append({
                'id': 'street_address',
                'title': 'Street Address',
                'render': self.context.street_address
            })

        if self.context.country:
            fields.append({
                'id': 'country',
                'title': 'Country',
                'render': resolve_value(
                    self.context,
                    self.context.country,
                    'ploneun.consultant.country'
                )
            })

        regions = getattr(self.context, 'ilo_regions', [])
        if regions:
            fields.append({
                'id': 'regions',
                'title': 'Regions',
                'render': '<ul>%s</ul>' % ''.join([
                    '<li>%s</li>' % i for i in regions
                ])
            })

        return fields

    def attachments(self):
        brains = self.context.portal_catalog({
            'portal_type': 'File',
            'path': {
                'query': '/'.join(self.context.getPhysicalPath()),
                'depth': 1
            }
        })
        sm = getSecurityManager()
        result = []
        for brain in brains:
            obj = brain.getObject()
            unit = obj.getFile()
            icon = unit.getBestIcon()
            filename = unit.filename
            result.append({
                'icon': icon,
                'filename': filename,
                'obj': obj,
                'editable': sm.checkPermission(
                    permissions.ModifyPortalContent, obj)
            })
        return result

