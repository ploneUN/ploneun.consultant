from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent

from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from zope import schema
from zope.interface import alsoProvides

from ploneun.consultant import MessageFactory as _
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

# Interface class; used to define content-type schema.

class IConsultant(form.Schema, IImageScaleTraversable):
    """
    Consultant content type
    """

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=u'Full Name',
                    description=u'Full name of consultant')

    dexteritytextindexer.searchable('description')
    description = schema.Text(
            title=u'Brief description of consultant')

    gender = schema.Choice(
            title=u'Gender',
            vocabulary = 'ploneun.consultant.gender'
            )

    dexteritytextindexer.searchable('email')
    email = schema.TextLine(
            title=u'Email address')

    phone = schema.TextLine(
            title=u'Phone number',
            description=u'eg. +61-3-3333-333',
            required=False)

    skype = schema.TextLine(
            title=u'Skype ID',
            required=False)

    dexteritytextindexer.searchable('street_address')
    street_address = schema.Text(
                title=u'Street Address',
                required=False,)

    dexteritytextindexer.searchable('details')
    # details = RichText(
    #         title=u'Details',
    #         description=u'Details and notes on consultant such as work' 
    #         ' experience.',
    #         required=False
    #         )

    form.widget(details=WysiwygFieldWidget)
    details = schema.Text(title=u'Details',
             description=u'Details and notes on consultant such as work' 
             ' experience.',
             required=False)

    country = schema.Choice(
            title=_(u'Country'),
            description=_(u'Please select a country consultant is'
            ' based in.'),
            vocabulary='ploneun.consultant.country',
            required=True,
            missing_value = None,
            )

    languages = schema.List(
            title=u'Languages',
            description=u'Languages spoken & written',
            value_type=schema.Choice(
                vocabulary='ploneun.consultant.languages'
                ),
            required=True
            )

#    years_experience = schema.Int(
#            title=u'Years of Experience',
#            required=False
#    )


    #region =

    # industry (Generic)
    # job_function

    # fieldsets for Optional Personal Details 

    form.fieldset('Personal Details',
                  label=_(u"Optional Personal Details"),
                  fields=['dob', 'photo'],
                  )

    dob = schema.Date(
            title=u'Date of Birth',
            required=False)

    photo = NamedBlobImage(
            title=u'Upload photo.',
            required=False)

alsoProvides(IConsultant, IFormFieldProvider)
