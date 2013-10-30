from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from p01.vocabulary.language import ISO639Alpha2LanguageVocabulary

class Languages(grok.GlobalUtility):
    grok.name('ploneun.consultant.languages')
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        return ISO639Alpha2LanguageVocabulary(context)
