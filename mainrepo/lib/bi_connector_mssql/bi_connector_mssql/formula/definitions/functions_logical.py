import sqlalchemy as sa

import bi_formula.definitions.functions_logical as base
from bi_formula.definitions.base import (
    TranslationVariant,
)

from bi_connector_mssql.formula.constants import MssqlDialect as D


V = TranslationVariant.make


DEFINITIONS_LOGICAL = [
    # case
    base.FuncCase.for_dialect(D.MSSQLSRV),

    # if
    base.FuncIf.for_dialect(D.MSSQLSRV),

    # ifnull
    base.FuncIfnull(variants=[
        V(D.MSSQLSRV, sa.func.ISNULL),
    ]),

    # iif
    base.FuncIif3Legacy.for_dialect(D.MSSQLSRV),

    # isnull
    base.FuncIsnull.for_dialect(D.MSSQLSRV),

    # zn
    base.FuncZn(variants=[
        V(D.MSSQLSRV, lambda x: sa.func.ISNULL(x, 0)),
    ]),
]