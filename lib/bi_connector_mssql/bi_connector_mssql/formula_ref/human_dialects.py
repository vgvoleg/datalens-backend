from bi_formula_ref.texts import StyledDialect

from bi_connector_mssql.formula.constants import MssqlDialect
from bi_connector_mssql.formula_ref.i18n import Translatable


HUMAN_DIALECTS = {
    MssqlDialect.MSSQLSRV_14_0: StyledDialect(
        '`Microsoft SQL Server 2017 (14.0)`',
        '`Microsoft`<br/>`SQL Server 2017`<br/>`(14.0)`',
        Translatable('`Microsoft SQL Server` version `2017 (14.0)`'),
    ),
}