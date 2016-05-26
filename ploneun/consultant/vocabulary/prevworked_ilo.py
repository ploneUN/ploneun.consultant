from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class PrevWorkedIlo(grok.GlobalUtility):
    grok.name('ploneun.consultant.prevworked_ilo')
    grok.implements(IVocabularyFactory)

    items = [
        (
         "Previously worked with ILO",
         "Previously worked with ILO",
        ),
        ]

    def __call__(self, context):
        terms = [ SimpleTerm(value=pair[0], token=pair[0],
            title=pair[1]) for pair in self.items ]
        return SimpleVocabulary(terms)
