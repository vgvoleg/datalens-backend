import os

import attr

from bi_i18n.localizer_base import Translatable as BaseTranslatable
from bi_i18n.localizer_base import TranslationConfig

import bi_connector_postgresql as package

DOMAIN = f"bi_formula_ref_{package.__name__}"

_LOCALE_DIR = os.path.join(os.path.dirname(__file__), "..", "locales")

CONFIGS = [
    TranslationConfig(path=_LOCALE_DIR, domain=DOMAIN, locale="en"),
    TranslationConfig(path=_LOCALE_DIR, domain=DOMAIN, locale="ru"),
]


@attr.s
class Translatable(BaseTranslatable):
    domain: str = attr.ib(default=DOMAIN)
