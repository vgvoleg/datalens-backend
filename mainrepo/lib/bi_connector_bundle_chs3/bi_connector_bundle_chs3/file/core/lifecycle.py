from bi_connector_bundle_chs3.chs3_base.core.lifecycle import BaseFileS3ConnectionLifecycleManager
from bi_connector_bundle_chs3.file.core.us_connection import FileS3Connection


class FileS3ConnectionLifecycleManager(BaseFileS3ConnectionLifecycleManager):
    ENTRY_CLS = FileS3Connection