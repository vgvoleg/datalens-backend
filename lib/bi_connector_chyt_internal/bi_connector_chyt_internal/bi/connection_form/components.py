from __future__ import annotations

import attr
from enum import unique
from typing import Optional

import bi_api_connector.form_config.models.rows as C
from bi_api_connector.form_config.models.rows.base import DisplayConditionsMixin, FormFieldMixin
from bi_api_connector.form_config.models.rows.prepared.base import PreparedRow, DisabledMixin
from bi_api_connector.form_config.models.common import remap_skip_if_null
from bi_api_connector.form_config.models.common import FormFieldName
from bi_connector_chyt_internal.bi.i18n.localizer import Translatable
from bi_api_connector.form_config.models.base import ConnectionFormMode

from bi_i18n.localizer_base import Localizer


@attr.s(kw_only=True, frozen=True)
class OAuthTokenCHYTRow(PreparedRow, DisplayConditionsMixin, FormFieldMixin, DisabledMixin):
    type = 'oauth_chyt'

    fake_value: Optional[str] = attr.ib(default=None, metadata=remap_skip_if_null('fakeValue'))


@unique
class CHYTInternalFieldName(FormFieldName):
    alias = 'alias'
    cluster = 'cluster'


def clique_alias_row(localizer: Localizer, mode: ConnectionFormMode) -> C.CustomizableRow:
    return C.CustomizableRow(items=[
        C.LabelRowItem(text=localizer.translate(Translatable('field_clique'))),
        C.InputRowItem(
            name=CHYTInternalFieldName.alias,
            width='l',
            default_value='' if mode == ConnectionFormMode.create else None,
            ),
        ])


def cluster_row(localizer: Localizer) -> C.CustomizableRow:
    return C.CustomizableRow(items=[
        C.LabelRowItem(text=localizer.translate(Translatable('field_cluster'))),
        C.SelectRowItem(
            name=CHYTInternalFieldName.cluster,
            width='l',
            available_values=[
                C.SelectOption(content='Hahn', value='hahn'),
                C.SelectOption(content='Arnold', value='arnold'),
                C.SelectOption(content='Vanga', value='vanga'),
                C.SelectOption(content='Seneca-vla', value='seneca-vla'),
                C.SelectOption(content='Seneca-sas', value='seneca-sas'),
                C.SelectOption(content='Bohr', value='bohr'),
                C.SelectOption(content='Landau', value='landau'),
            ],
            default_value='hahn',
            control_props=C.SelectRowItem.Props(show_search=False),
        )
    ])