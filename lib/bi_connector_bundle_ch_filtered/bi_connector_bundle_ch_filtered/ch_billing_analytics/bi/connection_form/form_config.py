from __future__ import annotations

from bi_connector_bundle_ch_filtered.ch_billing_analytics.bi.connection_info import (
    CHBillingAnalyticsConnectionInfoProvider,
)
from bi_connector_bundle_ch_filtered.base.bi.connection_form.form_config import ServiceConnectionBaseFormFactory
from bi_connector_bundle_ch_filtered.base.bi.i18n.localizer import Translatable


class CHBillingAnalyticsConnectionFormFactory(ServiceConnectionBaseFormFactory):
    template_name = 'yc_billing_stats'

    def _title(self) -> str:
        return CHBillingAnalyticsConnectionInfoProvider.get_title(self._localizer)

    def _description(self) -> str:
        docs_url = self._localizer.translate(Translatable('cloud-docs-url'))
        docs_url += '/billing/security'

        return self._localizer.translate(Translatable('label_yc-billing-conn-description')).format(DOC_LINK=docs_url)
