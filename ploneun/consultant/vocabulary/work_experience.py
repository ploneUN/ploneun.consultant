from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class work_experience(grok.GlobalUtility):
    grok.name('ploneun.consultant.work_experience')
    grok.implements(IVocabularyFactory)

    items = [
        (
         'Previously worked with ILO',
         u'Worked for EVAL',
        ),
        (
         'Has a notice',
         u'Consultants with a notice',
        )
        ]

    def __call__(self, context):
        terms = [ SimpleTerm(value=pair[0], token=pair[0],
            title=pair[1]) for pair in self.items ]
        return SimpleVocabulary(terms)