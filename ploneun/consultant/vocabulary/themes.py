from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class Themes(grok.GlobalUtility):
    grok.name('ploneun.consultant.themes')
    grok.implements(IVocabularyFactory)

    items = [
        (
         'childlabour',
         u'Child Labour',
        ),
        (
         'comms',
         u'Communications and Knowledge',
        ),
        (
         'dw',
         u'Decent Work',
        ),
        (
         'domestic',
         u'Domestic Workers',
        ),
        (
         'economicdev',
         u'Economic and Social Development',
        ),
        (
         'employers',
         u'Employers\' activities',
        ),
        (
         'emppromotion',
         u'Employment Promotion',
        ),
        (
         'empsecurity',
         u'Employment Security',
        ),
        (
         'equality',
         u'Equality and Discrimination',
        ),
       (
         'finance',
         u'Finance and Administrative Services',
        ),
        (
         'forcedlabour',
         u'Forced Labour',
        ),
       (
         'freedomassoc',
         u'Freedom of Association and The Right to Collective Bargaining',
        ),
        (
         'gj',
         u'Green Jobs',
        ),
         (
         'hiv',
         u'HIV/AIDS',
        ),
        (
         'sectors',
         u'Individual Sectors and Industries',
        ),
        (
         'ir',
         u'Industrial Relations',
        ),
        (
         'it',
         u'IT Services',
        ),
        (
         'law',
         u'Labour Law',
        ),
        (
         'inspection',
         u'Labour Inspection and Administration',
        ),
        (
         'migration',
         u'Labour Migration',
        ),
        (
         'standards',
         u'Labour Standards',
        ),
        (
         'management',
         u'Management Services',
        ),
        (
         'maritime',
         u'Maritime Labour Convention',
        ),
        (
         'mdg',
         u'Millennium Development Goals',
        ),
        (
         'programming',
         u'Programming, M&E',
        ),
        (
         'rural',
         u'Rural Development',
        ),
        (
         'safety',
         u'Safety and Health at Work',
        ),
        (
         'skills',
         u'Skills, Knowledge and Employability',
        ),
        (
         'social',
         u'Social Security',
        ),
        (
         'tripartism',
         u'Tripartism and Social Dialogue',
        ),
         (
         'workers',
         u'Workers\' Activities',
        ),
         (
         'conditions',
         u'Working Conditions',
        ),
        (
         'youthemployment',
         u'Youth Employment',
        ),
        (
         'other',
         u'Other',
        ),
        ]

    def __call__(self, context):
        terms = [ SimpleTerm(value=pair[0], token=pair[0],
            title=pair[1]) for pair in self.items ]
        return SimpleVocabulary(terms)
