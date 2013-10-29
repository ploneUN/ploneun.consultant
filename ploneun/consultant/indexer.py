from plone.indexer import indexer
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
