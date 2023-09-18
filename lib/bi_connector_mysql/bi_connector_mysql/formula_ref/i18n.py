import os

import attr

from dl_i18n.localizer_base import TranslationConfig, Translatable as BaseTranslatable

import bi_connector_mysql as package


DOMAIN = f'bi_formula_ref_{package.__name__}'

_LOCALE_DIR = os.path.join(os.path.dirname(__file__), '..', 'locales')

CONFIGS = [
    TranslationConfig(path=_LOCALE_DIR, domain=DOMAIN, locale='en'),
    TranslationConfig(path=_LOCALE_DIR, domain=DOMAIN, locale='ru'),
]

@attr.s
class Translatable(BaseTranslatable):
    domain: str = attr.ib(default=DOMAIN)
