import attr

from bi_constants.enums import ConnectionType

from bi_core.connectors.clickhouse_base.dto import ClickHouseBaseDTO


@attr.s(frozen=True, kw_only=True)
class BaseCHYTDTO(ClickHouseBaseDTO):
    clique_alias: str = attr.ib(kw_only=True)


@attr.s(frozen=True, kw_only=True)
class CHYTDTO(BaseCHYTDTO):
    conn_type = ConnectionType.chyt

    port: int = attr.ib()
    host: str = attr.ib()
    protocol: str = attr.ib()
    token: str = attr.ib(repr=False)