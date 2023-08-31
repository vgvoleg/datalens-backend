from typing import Optional, Literal

import attr

from bi_api_connector.form_config.models.common import (
    Align,
    Width,
    MarkdownStr,
    SerializableConfig,
    skip_if_null,
    remap_skip_if_null,
    inner,
)
from bi_api_connector.form_config.models.rows.base import DisplayConditionsMixin, FormFieldMixin, InnerFieldMixin
from bi_api_connector.form_config.models.rows.customizable.base import (
    RowItem,
    ControlRowItem,
    PlaceholderMixin,
    DefaultValueMixin,
)


@attr.s(kw_only=True, frozen=True)
class HiddenRowItem(RowItem, FormFieldMixin, InnerFieldMixin, DisplayConditionsMixin, DefaultValueMixin):
    """
    Can be used to send values that do not have a corresponding control item
    (e.g. calculated token expiration time, that is received from an external API)
    """

    component_id = 'hidden'


@attr.s(kw_only=True, frozen=True)
class LabelRowItem(RowItem, DisplayConditionsMixin):
    """ https://a.yandex-team.ru/arcadia/data-ui/datalens/src/ui/units/connections/components/ConnectorForm/components/Label """

    component_id = 'label'
    text: str = attr.ib()
    align: Optional[Align] = attr.ib(default=None, metadata=skip_if_null())
    help_text: Optional[MarkdownStr] = attr.ib(default=None, metadata=remap_skip_if_null('helpText'))


@attr.s(kw_only=True, frozen=True)
class SelectableOption:  # TODO rename to RadioButtonOption
    text: str = attr.ib()
    value: str = attr.ib()


@attr.s(kw_only=True, frozen=True)
class InputRowItem(ControlRowItem, PlaceholderMixin):
    """
    https://github.com/gravity-ui/uikit/tree/main/src/components/TextInput
    https://preview.gravity-ui.com/uikit/?path=/story/components-textinput--default
    """

    @attr.s(kw_only=True, frozen=True)
    class Props(SerializableConfig):
        multiline: Optional[bool] = attr.ib(default=None, metadata=skip_if_null())  # false if undefined
        type: Literal['text', 'password', 'number'] = attr.ib(default='text')

    component_id = 'input'

    control_props: Optional[Props] = attr.ib(default=None, metadata=remap_skip_if_null('controlProps'))


@attr.s(kw_only=True, frozen=True)
class SelectOption(SerializableConfig):
    class Data(SerializableConfig):
        description: Optional[str] = attr.ib(default=None, metadata=skip_if_null())

    content: str = attr.ib()
    value: str = attr.ib()
    data: Optional[Data] = attr.ib(default=None, metadata=skip_if_null())


@attr.s(kw_only=True, frozen=True)
class SelectRowItem(ControlRowItem, PlaceholderMixin):
    """ https://a.yandex-team.ru/arcadia/data-ui/common/src/components/YCSelect """

    @attr.s(kw_only=True, frozen=True)
    class Props(SerializableConfig):
        show_search: Optional[bool] = attr.ib(default=None, metadata=remap_skip_if_null('showSearch'))

    component_id = 'select'

    available_values: Optional[list[SelectOption]] = attr.ib(default=None, metadata=remap_skip_if_null('availableValues'))
    control_props: Optional[Props] = attr.ib(default=None, metadata=remap_skip_if_null('controlProps'))


@attr.s(kw_only=True, frozen=True)
class RadioButtonRowItem(ControlRowItem):
    """
    https://github.com/gravity-ui/uikit/tree/main/src/components/RadioButton
    https://preview.gravity-ui.com/uikit/?path=/story/components-radiobutton--default
    """

    component_id = 'radio_button'

    options: list[SelectableOption] = attr.ib()


@attr.s(kw_only=True, frozen=True)
class RadioGroupRowItemOption(SerializableConfig):

    @attr.s(kw_only=True, frozen=True)
    class ValueContent(SerializableConfig):
        text: str = attr.ib()
        hint_text: Optional[MarkdownStr] = attr.ib(default=None, metadata=remap_skip_if_null('hintText'))

    content: ValueContent = attr.ib()
    value: str = attr.ib()


@attr.s(kw_only=True, frozen=True)
class RadioGroupRowItem(RowItem, DisplayConditionsMixin, FormFieldMixin, InnerFieldMixin):
    """
    https://github.com/gravity-ui/uikit/tree/main/src/components/RadioGroup
    https://preview.gravity-ui.com/uikit/?path=/story/components-radiogroup--default
    """

    @attr.s(kw_only=True, frozen=True)
    class Props(SerializableConfig):
        disabled: Optional[bool] = attr.ib(default=None, metadata=skip_if_null())

    component_id = 'radio_group'

    options: list[RadioGroupRowItemOption] = attr.ib()
    default_value: Optional[str] = attr.ib(default=None, metadata=remap_skip_if_null('defaultValue'))
    control_props: Optional[Props] = attr.ib(default=None, metadata=remap_skip_if_null('controlProps'))

    def __attrs_post_init__(self) -> None:
        if (self.default_value is not None and
                self.default_value not in (possible_values := [option.value for option in self.options])):
            raise ValueError(
                f'Invalid default value for radio group: {self.default_value} is not in {possible_values}'
            )


@attr.s(kw_only=True, frozen=True)
class CheckboxRowItem(RowItem, DisplayConditionsMixin, FormFieldMixin, InnerFieldMixin, DefaultValueMixin):
    """
    https://github.com/gravity-ui/uikit/tree/main/src/components/Checkbox
    https://preview.gravity-ui.com/uikit/?path=/story/components-checkbox--default
    """

    @attr.s(kw_only=True, frozen=True)
    class Props(SerializableConfig):
        size: Optional[Literal['m', 'l']] = attr.ib(default=None, metadata=skip_if_null())
        qa: Optional[str] = attr.ib(default=None, metadata=skip_if_null())  # UI-specific testing stuff, should be removed at some point

    component_id = 'checkbox'

    text: str = attr.ib()
    control_props: Optional[Props] = attr.ib(default=None, metadata=remap_skip_if_null('controlProps'))


@attr.s(kw_only=True, frozen=True)
class DatepickerRowItem(ControlRowItem):
    """ https://a.yandex-team.ru/arcadia/data-ui/common/src/components/SimpleDatepicker """

    @attr.s(kw_only=True, frozen=True)
    class Props(SerializableConfig):
        size: Optional[Literal['s', 'm', 'l', 'xl']] = attr.ib(default=None, metadata=skip_if_null())

    component_id = 'datepicker'

    width: Optional[Width] = attr.ib(default=None, init=False, metadata=inner())  # not supported by Datepicker
    control_props: Optional[Props] = attr.ib(default=None, metadata=remap_skip_if_null('controlProps'))


@attr.s(kw_only=True, frozen=True)
class PlainTextRowItem(RowItem, DisplayConditionsMixin):
    """ https://a.yandex-team.ru/arcadia/data-ui/datalens/src/ui/units/connections/components/ConnectorForm/components/PlainText """

    component_id = 'plain_text'

    text: str = attr.ib()
    hint_text: Optional[MarkdownStr] = attr.ib(default=None, metadata=remap_skip_if_null('hintText'))


@attr.s(kw_only=True, frozen=True)
class DescriptionRowItem(RowItem, DisplayConditionsMixin):
    """ https://a.yandex-team.ru/arcadia/data-ui/datalens/src/ui/units/connections/components/ConnectorForm/components/Description """

    component_id = 'description'

    text: MarkdownStr = attr.ib()


@attr.s(kw_only=True, frozen=True)
class FileInputRowItem(RowItem, FormFieldMixin, InnerFieldMixin, DisplayConditionsMixin):
    """ https://a.yandex-team.ru/arcadia/data-ui/common/src/components/FileInput """

    component_id = 'file-input'