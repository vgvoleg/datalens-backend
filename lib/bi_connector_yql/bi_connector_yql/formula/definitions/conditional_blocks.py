import sqlalchemy as sa

import bi_formula.definitions.conditional_blocks as base
from bi_formula.definitions.base import (
    TranslationVariant,
)

from bi_connector_yql.formula.constants import YqlDialect as D


V = TranslationVariant.make


DEFINITIONS_COND_BLOCKS = [
    # _case_block_
    base.CaseBlock.for_dialect(D.YQL),

    # _if_block_
    base.IfBlock3(variants=[
        V(D.YQL, sa.func.IF),
    ]),
    base.IfBlockMulti.for_dialect(D.YQL),
]
