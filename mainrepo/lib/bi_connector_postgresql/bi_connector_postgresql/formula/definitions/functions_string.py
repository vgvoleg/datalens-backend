import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as sa_postgresql

from bi_connector_postgresql.formula.constants import PostgreSQLDialect as D
import bi_formula.definitions.functions_string as base
from bi_formula.definitions.base import (
    TranslationVariant, TranslationVariantWrapped,
)
from bi_formula.definitions.common import make_binary_chain
from bi_formula.shortcuts import n


V = TranslationVariant.make
VW = TranslationVariantWrapped.make


DEFINITIONS_STRING = [
    # ascii
    base.FuncAscii.for_dialect(D.POSTGRESQL),

    # char
    base.FuncChar(variants=[
        V(D.POSTGRESQL, sa.func.CHR),
    ]),

    # concat
    base.Concat1.for_dialect((D.POSTGRESQL)),
    base.ConcatMultiStrConst.for_dialect(D.POSTGRESQL),
    base.ConcatMultiStr(variants=[
        V(D.POSTGRESQL, lambda *args: make_binary_chain(
            (lambda x, y: x.concat(y)),  # should result in `x || y` SQL.
            *args,  # should result in `x || y || z || ...` SQL
            wrap_as_nodes=False)),
    ]),
    base.ConcatMultiAny.for_dialect(D.POSTGRESQL),

    # contains
    base.FuncContainsConst.for_dialect(D.POSTGRESQL),
    base.FuncContainsNonConst(variants=[
        V(D.POSTGRESQL, lambda x, y: sa.func.STRPOS(x, y) > 0),
    ]),
    base.FuncContainsNonString.for_dialect(D.POSTGRESQL),

    # endswith
    base.FuncEndswithConst.for_dialect(D.POSTGRESQL),
    base.FuncEndswithNonConst(variants=[
        V(D.POSTGRESQL, lambda x, y: (
            sa.func.SUBSTRING(x, sa.func.char_length(x) - sa.func.char_length(y) + 1) == y)),
    ]),
    base.FuncEndswithNonString.for_dialect(D.POSTGRESQL),

    # find
    base.FuncFind2(variants=[
        V(D.POSTGRESQL, sa.func.STRPOS),
    ]),
    base.FuncFind3(variants=[
        V(
            D.POSTGRESQL,
            lambda x, y, z: n.if_(  # type: ignore  # TODO: fix
                sa.func.STRPOS(sa.func.SUBSTRING(x, z), y) > 0
            ).then(
                sa.func.STRPOS(sa.func.SUBSTRING(x, z), y) + z - 1,
            ).else_(0)
        ),
    ]),

    # icontains
    base.FuncIContainsConst.for_dialect(D.POSTGRESQL),
    base.FuncIContainsNonConst.for_dialect(D.POSTGRESQL),
    base.FuncIContainsNonString.for_dialect(D.POSTGRESQL),

    # iendswith
    base.FuncIEndswithConst.for_dialect(D.POSTGRESQL),
    base.FuncIEndswithNonConst.for_dialect(D.POSTGRESQL),
    base.FuncIEndswithNonString.for_dialect(D.POSTGRESQL),

    # istartswith
    base.FuncIStartswithConst.for_dialect(D.POSTGRESQL),
    base.FuncIStartswithNonConst.for_dialect(D.POSTGRESQL),
    base.FuncIStartswithNonString.for_dialect(D.POSTGRESQL),

    # left
    base.FuncLeft.for_dialect(D.POSTGRESQL),

    # len
    base.FuncLenString(variants=[
        V(D.POSTGRESQL, sa.func.LENGTH),
    ]),

    # lower
    base.FuncLowerConst.for_dialect(D.POSTGRESQL),
    base.FuncLowerNonConst.for_dialect(D.POSTGRESQL),

    # ltrim
    base.FuncLtrim.for_dialect(D.POSTGRESQL),

    # regexp_extract
    base.FuncRegexpExtract(variants=[
        V(D.POSTGRESQL, lambda text, pattern: sa.type_coerce(sa.select(
            [sa.func.REGEXP_MATCHES(text, pattern, 'g')]
        ).limit(1).as_scalar(), sa_postgresql.ARRAY(sa.String))[1]),
    ]),

    # regexp_extract_nth
    base.FuncRegexpExtractNth(variants=[
        V(D.POSTGRESQL, lambda text, pattern, ind: sa.type_coerce(sa.select(
            [sa.func.REGEXP_MATCHES(text, pattern, 'g')]
        ).limit(1).offset(ind - 1).as_scalar(), sa_postgresql.ARRAY(sa.String))[1]),
    ]),

    # regexp_match
    base.FuncRegexpMatch(variants=[
        V(D.POSTGRESQL, lambda text, pattern: text.op('~')(pattern)),
    ]),

    # regexp_replace
    base.FuncRegexpReplace(variants=[
        V(D.POSTGRESQL, lambda text, patt, repl: sa.func.REGEXP_REPLACE(text, patt, repl, 'g')),
    ]),

    # replace
    base.FuncReplace.for_dialect(D.POSTGRESQL),

    # right
    base.FuncRight.for_dialect(D.POSTGRESQL),

    # rtrim
    base.FuncRtrim.for_dialect(D.POSTGRESQL),

    # space
    base.FuncSpaceConst.for_dialect(D.POSTGRESQL),
    base.FuncSpaceNonConst(variants=[
        V(D.POSTGRESQL, lambda size: sa.func.REPEAT(' ', size)),
    ]),

    # split
    base.FuncSplit1(variants=[
        V(D.POSTGRESQL, lambda text: sa.func.string_to_array(text, ',')),
    ]),
    base.FuncSplit2(variants=[
        V(D.POSTGRESQL, lambda text, delim: sa.func.string_to_array(text, delim)),
    ]),
    base.FuncSplit3(variants=[
        V(D.POSTGRESQL, lambda text, delim, ind: sa.func.SPLIT_PART(
            text, delim, sa.cast(ind, sa.INTEGER)
        )),  # FIXME: does not work with negative indices
    ]),

    # startswith
    base.FuncStartswithConst.for_dialect(D.POSTGRESQL),
    base.FuncStartswithNonConst(variants=[
        V(D.POSTGRESQL, lambda x, y: sa.func.STRPOS(x, y) == 1),
    ]),
    base.FuncStartswithNonString.for_dialect(D.POSTGRESQL),

    # substr
    base.FuncSubstr2.for_dialect(D.POSTGRESQL),
    base.FuncSubstr3.for_dialect(D.POSTGRESQL),

    # trim
    base.FuncTrim.for_dialect(D.POSTGRESQL),

    # upper
    base.FuncUpperConst.for_dialect(D.POSTGRESQL),
    base.FuncUpperNonConst.for_dialect(D.POSTGRESQL),
]