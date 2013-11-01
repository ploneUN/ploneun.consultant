from plone.indexer import indexer
from DateTime import DateTime
from collective import dexteritytextindexer
from ploneun.consultant.content.consultant import IConsultant
import p01.vocabulary.country
import p01.vocabulary.language
from five import grok

class CountryIndexer(grok.Adapter):
    grok.context(IConsultant)
    grok.implements(dexteritytextindexer.IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def country(self):
        country = p01.vocabulary.country.ISO3166Alpha2CountryVocabulary(
                self.context).getTerm(self.context.country).title
        return country

    def languages(self):
        languages = self.context.languages

        results = []

        for language in languages:
            l = po1.vocabulary.language.ISO3166Alpha2CountryVocabulary(
                    self.context).getTerm(self.language).title

            results.append(l)

        return " ".join(results)

    def __call__(self):
        return self.country() + ' ' + self.language()

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
