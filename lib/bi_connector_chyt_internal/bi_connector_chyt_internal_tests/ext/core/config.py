from dl_constants.enums import BIType, RawSQLLevel

DEFAULT_CONFIG = dict(
    alias="*chyt_datalens_back",
    cluster="hahn",
    raw_sql_level=RawSQLLevel.dashsql,
)
NO_ROBOT_ACCESS_CONFIG = DEFAULT_CONFIG | dict(
    alias='*chyt_datalens_back_no_robot',
)
NOT_EXISTS_CONFIG = DEFAULT_CONFIG | dict(
    alias='*chyt_datalens_back_not_exists',
)

TEST_TABLES = dict(
    any_table='//home/yandexbi/datalens-back/any_table',
    no_access_table='//home/yandexbi/datalens-back/bi_test_data/no_inherit_acl/no_access_for_test_robot',
    sample_superstore='//home/yandexbi/datalens-back/bi_test_data/sample_superstore',
)

DATA_SOURCE_TEST_QUERY = f'select *, 123 as extra from "{TEST_TABLES["sample_superstore"]}" limit 10'
RANGE_DATASET_DSRC_PARAMS = dict(
    directory_path='//home/yandexbi/datalens-back/bi_test_data/sample_superstore_range',
    range_from='2014-01-03',
    range_to='2017-12-30',
)
SUBSELECT_DSRC_PARAMS = dict(subsql=DATA_SOURCE_TEST_QUERY)

SAMPLE_TABLE_SIMPLIFIED_SCHEMA = [
    ('APIKey', BIType.integer),
    ('SessionType', BIType.integer),
    ('EventType', BIType.integer),
    ('UUID', BIType.string),
    ('PublisherName', BIType.string),
    ('DeviceIDHash', BIType.integer),
    ('DeviceID', BIType.string),
    ('StartTime', BIType.string),
    ('StartDate', BIType.string),
    ('DeviceIDSessionIDHash', BIType.integer),
    ('PublisherID', BIType.integer),
    ('extra', BIType.integer),
]
