from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from ploneun.consultant import MessageFactory as _

class IJobFunction(form.Schema):
    """
       Marker/Form interface for Job Function
    """

    # -*- Your Zope schema definitions here ... -*-

    functions = schema.List(
            title=u'Job Functions',
            value_type=schema.Choice(
                vocabulary='ploneun.consultant.function'),
            required=False,
            missing_value = None,
            )


alsoProvides(IJobFunction,IFormFieldProvider)
