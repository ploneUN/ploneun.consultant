from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

from p01.vocabulary.country import ISO3166Alpha2CountryVocabulary 

class Country(grok.GlobalUtility):
    grok.name('ploneun.consultant.country')
    grok.implements(IVocabularyFactory)

    def __call__(self,context):
      return ISO3166Alpha2CountryVocabulary(context) 
