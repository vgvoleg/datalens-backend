import sqlalchemy as sa

import bi_formula.definitions.functions_logical as base
from bi_formula.definitions.base import (
    TranslationVariant,
)

from bi_connector_mysql.formula.constants import MySQLDialect as D


V = TranslationVariant.make


DEFINITIONS_LOGICAL = [
    # case
    base.FuncCase.for_dialect(D.MYSQL),

    # if
    base.FuncIf.for_dialect(D.MYSQL),

    # ifnull
    base.FuncIfnull(variants=[
        V(D.MYSQL, sa.func.IFNULL),
    ]),

    # iif
    base.FuncIif3Legacy.for_dialect(D.MYSQL),

    # isnull
    base.FuncIsnull(variants=[
        V(D.MYSQL, sa.func.ISNULL),
    ]),

    # zn
    base.FuncZn(variants=[
        V(D.MYSQL, lambda x: sa.func.IFNULL(x, 0)),
    ]),
]
