from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class Gender(grok.GlobalUtility):
    grok.name('ploneun.consultant.gender')
    grok.implements(IVocabularyFactory)


    items = [
        (
         'male',
         u'Male',
        ),
        (
         'female',
         u'Female',
        ),
        ]

    def __call__(self, context):
        terms = [ SimpleTerm(value=pair[0], token=pair[0],
            title=pair[1]) for pair in self.items ]
        return SimpleVocabulary(terms)
