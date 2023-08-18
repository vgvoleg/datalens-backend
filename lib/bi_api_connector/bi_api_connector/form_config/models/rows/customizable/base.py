from typing import ClassVar, Optional, Any

import attr

from bi_api_connector.form_config.models.common import (
    SerializableConfig,
    MarkdownStr,
    Width,
    skip_if_null,
    remap_skip_if_null,
)
from bi_api_connector.form_config.models.rows.base import (
    FormFieldMixin,
    DisplayConditionsMixin,
    FormRow,
    InnerFieldMixin,
)


@attr.s(kw_only=True, frozen=True)
class RowItem(SerializableConfig):
    component_id: ClassVar[str]

    def as_dict(self) -> dict[str, Any]:
        return dict(
            id=self.component_id,
            **super().as_dict(),
        )


@attr.s(kw_only=True, frozen=True)
class PlaceholderMixin(SerializableConfig):
    placeholder: Optional[str] = attr.ib(default=None, metadata=skip_if_null())


@attr.s(kw_only=True, frozen=True)
class DefaultValueMixin(SerializableConfig):
    # comma separated if multiple=true
    default_value: Optional[str | bool] = attr.ib(default=None, metadata=remap_skip_if_null('defaultValue'))


@attr.s(kw_only=True, frozen=True)
class ControlRowItem(RowItem, FormFieldMixin, DisplayConditionsMixin, InnerFieldMixin, DefaultValueMixin):
    fake_value: Optional[str] = attr.ib(default=None, metadata=remap_skip_if_null('fakeValue'))
    hint_text: Optional[MarkdownStr] = attr.ib(default=None, metadata=remap_skip_if_null('hintText'))
    width: Optional[Width] = attr.ib(default=None, metadata=skip_if_null())


@attr.s(kw_only=True, frozen=True)
class CustomizableRow(FormRow):
    items: list[RowItem] = attr.ib()
