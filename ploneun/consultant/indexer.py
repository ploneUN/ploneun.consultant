from plone.indexer import indexer
from DateTime import DateTime
from collective import dexteritytextindexer
from ploneun.consultant.content.consultant import IConsultant
from five import grok
from ploneun.consultant.vocabulary import resolve_value

class CountryIndexer(grok.Adapter):
    grok.context(IConsultant)
    grok.implements(dexteritytextindexer.IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def country(self):
        country = resolve_value(self.context, self.context.country,
                'ploneun.consultant.country')
        return country

    def languages(self):
        languages = self.context.languages

        results = []

        for language in languages:
            l = resolve_value(self.context, language,
                    'ploneun.consultant.languages')
            results.append(l)

        return " ".join(results)

    def __call__(self):
        return self.country() + ' ' + self.languages()

@indexer(IConsultant)
def dobIndexer(obj):
    if obj.dob is None:
        return None
    return DateTime(obj.dob.isoformat())
grok.global_adapter(dobIndexer, name='ploneun_dob')

@indexer(IConsultant)
def ploneUNCountryIndexer(obj):
    if obj.country is None:
        return None
    return obj.country
grok.global_adapter(ploneUNCountryIndexer, name='ploneun_country')

@indexer(IConsultant)
def ploneUNLanguageIndexer(obj):
    if obj.languages is None:
        return None
    return obj.languages
grok.global_adapter(ploneUNLanguageIndexer, name='ploneun_languages')

@indexer(IConsultant)
def ploneUNWorkExperienceIndexer(obj):
    if obj.work_experience is None:
        return None
    return obj.work_experience
grok.global_adapter(ploneUNWorkExperienceIndexer, name='ploneun_work_experience')

@indexer(IConsultant)
def ploneUNThemeIndexer(obj):
    if obj.themes is None:
        return None
    return obj.themes
grok.global_adapter(ploneUNThemeIndexer, name='ploneun_themes')

@indexer(IConsultant)
def ploneUNFunctionIndexer(obj):
    if obj.functions is None:
        return None
    return obj.functions
grok.global_adapter(ploneUNFunctionIndexer, name='ploneun_functions')

@indexer(IConsultant)
def ploneUNGenderIndexer(obj):
    if obj.gender is None:
        return None
    return obj.gender
grok.global_adapter(ploneUNGenderIndexer, name='ploneun_gender')

@indexer(IConsultant)
def ploneUNExperience(obj):
    if obj.years_experience is None:
        return None
    return obj.years_experience
grok.global_adapter(ploneUNExperience, name='ploneun_years_experience')

# @indexer(IConsultant)
# def prevworked_ilo_indexer(obj):
#     if obj.prevworked_ilo:
#         return "Previously worked with ILO"
# grok.global_adapter(prevworked_ilo_indexer, name='prevworked_ilo_indexer')

# @indexer(IConsultant)
# def has_notice_indexer(obj):
#     if obj.has_notice:
#         return "Has a notice"
# grok.global_adapter(has_notice_indexer, name='has_notice_indexer')