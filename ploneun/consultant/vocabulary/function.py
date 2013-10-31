from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class Function(grok.GlobalUtility):
    grok.name('ploneun.consultant.function')
    grok.implements(IVocabularyFactory)

    items = [
        (
         'accounting',
         u'Acounting/Auditing',
        ),
        (
         'adminstrative',
         u'Administrative',
        ),
        (
         'advertising',
         u'Advertising',
        ),
        (
         'analyst',
         u'Analyst',
        ),
        (
         'art',
         u'Art/Creative',
        ),
        (
         'business',
         u'Business Development',
        ),
        (
         'consulting',
         u'Consulting',
        ),
        (
         'customer',
         u'Customer Service',
        ),
        (
         'design',
         u'Design',
        ),
        (
         'distribution',
         u'Distribution',
        ),
        (
         'education',
         u'Education',
        ),
        (
         'engineering',
         u'Engineering',
        ),
        (
         'finance',
         u'Finance',
        ),
        (
         'general',
         u'General Business',
        ),
        (
         'health',
         u'Health Care Provider',
        ),
        (
         'hr',
         u'Human Resourses',
        ),
        (
         'it',
         u'Information Technology',
        ),
        (
         'legal',
         u'Legal',
        ),
        (
         'mgmt',
         u'Management',
        ),
        (
         'manufacturing',
         u'Manufacturing',
        ),
        (
         'marketing',
         u'Marketing',
        ),
        (
         'product',
         u'Product Management',
        ),
        (
         'pm',
         u'Project Management',
        ),
        (
         'pr',
         u'Public Relations',
        ),
        (
         'purchasing',
         u'Purchasing',
        ),
        (
         'qa',
         u'Quality Assurance',
        ),
        (
         'research',
         u'Research',
        ),
        (
         'sales',
         u'Sales',
        ),
        (
         'science',
         u'Science',
        ),
        (
         'strategy',
         u'Strategy',
        ),
        (
         'supply',
         u'Supply Chain',
        ),
        (
         'training',
         u'Training',
        ),
        (
         'writing',
         u'Writing/Editing',
        ),
        (
         'other',
         u'Other',
        )
        ]

    def __call__(self, context):
        terms = [ SimpleTerm(value=pair[0], token=pair[0],
            title=pair[1]) for pair in self.items ]
        return SimpleVocabulary(terms)
