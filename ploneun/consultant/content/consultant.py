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

from ploneun.consultant import MessageFactory as _


# Interface class; used to define content-type schema.

class IConsultant(form.Schema, IImageScaleTraversable):
    """
    Consultant content type
    """

    title = schema.TextLine(title=u'Full Name',
                    description=u'Full name of consultant')

    description = schema.Text(
            title=u'Brief description of consultant')

    photo = NamedBlobImage(
            title=u'Upload photo.')

    email = schema.TextLine(
            title=u'Email address')

    phone = schema.TextLine(
            title=u'Phone number',
            description=u'eg. +61-3-3333-333')

    skype = schema.TextLine(
            title=u'Skype ID')

    street_address = schema.Text(
                title=u'Street Address')

    # country = 
    # region =
    # specialization (Generic)
    

    


