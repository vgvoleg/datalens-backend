from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Mapping

from marshmallow import fields as ma_fields, EXCLUDE, post_dump, pre_load
from marshmallow_oneofschema import OneOfSchema
from marshmallow_enum import EnumField

from bi_model_tools.schema.dynamic_enum_field import DynamicEnumField

from bi_constants.enums import (
    BIType, CalcMode, CreateDSFrom, AggregationFunction, FieldType, ManagedBy,
    ComponentErrorLevel, ComponentType, WhereClauseOperation,
    JoinConditionType, BinaryJoinOperator, JoinType, ConditionPartCalcMode, ParameterValueConstraintType
)

from bi_api_client.dsmaker.primitives import (
    Dataset,
    ResultField, ResultSchemaAux,
    Column, DataSource,
    SourceAvatar, AvatarRelation, JoinCondition,
    DirectJoinPart, FormulaJoinPart, ResultFieldJoinPart,
    ObligatoryFilter, WhereClause,
    ComponentErrorRegistry, ComponentErrorPack, ComponentError,
    ParameterValueConstraint, RangeParameterValueConstraint, SetParameterValueConstraint,
    ParameterValue, StringParameterValue, IntegerParameterValue, FloatParameterValue,
    DateParameterValue, DateTimeParameterValue, DateTimeTZParameterValue, GenericDateTimeParameterValue,
    BooleanParameterValue, GeoPointParameterValue, GeoPolygonParameterValue, UuidParameterValue, MarkupParameterValue,
    ArrayStrParameterValue, ArrayIntParameterValue, ArrayFloatParameterValue,
    TreeStrParameterValue,
)
from bi_api_client.dsmaker.api.schemas.base import DefaultSchema
from bi_utils.schemas import OneOfSchemaWithDumpLoadHooks

if TYPE_CHECKING:
    from bi_api_client.dsmaker.primitives import JoinPart


class StringValueSchema(DefaultSchema[StringParameterValue]):
    TARGET_CLS = StringParameterValue
    value = ma_fields.String()


class IntegerValueSchema(DefaultSchema[IntegerParameterValue]):
    TARGET_CLS = IntegerParameterValue
    value = ma_fields.Integer()


class FloatValueSchema(DefaultSchema[FloatParameterValue]):
    TARGET_CLS = FloatParameterValue
    value = ma_fields.Float()


class DateValueSchema(DefaultSchema[DateParameterValue]):
    TARGET_CLS = DateParameterValue
    value = ma_fields.Date()


class DateTimeValueSchema(DefaultSchema[DateTimeParameterValue]):
    TARGET_CLS = DateTimeParameterValue
    value = ma_fields.DateTime()


class DateTimeTZValueSchema(DefaultSchema[DateTimeTZParameterValue]):
    TARGET_CLS = DateTimeTZParameterValue
    value = ma_fields.DateTime()


class GenericDateTimeValueSchema(DefaultSchema[GenericDateTimeParameterValue]):
    TARGET_CLS = GenericDateTimeParameterValue
    value = ma_fields.DateTime()


class BooleanValueSchema(DefaultSchema[BooleanParameterValue]):
    TARGET_CLS = BooleanParameterValue
    value = ma_fields.Boolean()


class GeoPointValueSchema(DefaultSchema[GeoPointParameterValue]):
    TARGET_CLS = GeoPointParameterValue
    value = ma_fields.List(ma_fields.Float())


class GeoPolygonValueSchema(DefaultSchema[GeoPolygonParameterValue]):
    TARGET_CLS = GeoPolygonParameterValue
    value = ma_fields.List(ma_fields.List(ma_fields.List(ma_fields.Float())))


class UuidValueSchema(DefaultSchema[UuidParameterValue]):
    TARGET_CLS = UuidParameterValue
    value = ma_fields.String()


class MarkupValueSchema(DefaultSchema[MarkupParameterValue]):
    TARGET_CLS = MarkupParameterValue
    value = ma_fields.String()


class ArrayStrValueSchema(DefaultSchema[ArrayStrParameterValue]):
    TARGET_CLS = ArrayStrParameterValue
    value = ma_fields.List(ma_fields.String())


class ArrayIntValueSchema(DefaultSchema[ArrayIntParameterValue]):
    TARGET_CLS = ArrayIntParameterValue
    value = ma_fields.List(ma_fields.Integer())


class ArrayFloatValueSchema(DefaultSchema[ArrayFloatParameterValue]):
    TARGET_CLS = ArrayFloatParameterValue
    value = ma_fields.List(ma_fields.Float())


class ValueSchema(OneOfSchemaWithDumpLoadHooks):
    CONTEXT_KEY = 'bi_value_type'
    type_field = 'type'
    type_schemas = {
        BIType.string.name: StringValueSchema,
        BIType.integer.name: IntegerValueSchema,
        BIType.float.name: FloatValueSchema,
        BIType.date.name: DateValueSchema,
        BIType.datetime.name: DateTimeValueSchema,
        BIType.datetimetz.name: DateTimeTZValueSchema,
        BIType.genericdatetime.name: GenericDateTimeValueSchema,
        BIType.boolean.name: BooleanValueSchema,
        BIType.geopoint.name: GeoPointValueSchema,
        BIType.geopolygon.name: GeoPolygonValueSchema,
        BIType.uuid.name: UuidValueSchema,
        BIType.markup.name: MarkupValueSchema,
        BIType.array_str.name: ArrayStrValueSchema,
        BIType.array_int.name: ArrayIntValueSchema,
        BIType.array_float.name: ArrayFloatValueSchema,
        BIType.tree_str.name: TreeStrParameterValue,
    }

    @pre_load(pass_many=False)
    def wrap_value_with_type(self, data: Any, **_: Any) -> Dict[str, Any]:
        type = getattr(self, 'context', {}).get(self.CONTEXT_KEY)
        return {'type': type, 'value': data}

    @post_dump(pass_many=False)
    def extract_value(self, data: Dict[str, Any], **_: Any) -> Any:
        return data['value']

    def get_obj_type(self, obj: ParameterValue) -> str:
        return getattr(obj, self.type_field).name


class AllParameterValueConstraintSchema(DefaultSchema[ParameterValueConstraint]):
    TARGET_CLS = ParameterValueConstraint


class RangeParameterValueConstraintSchema(DefaultSchema[RangeParameterValueConstraint]):
    TARGET_CLS = RangeParameterValueConstraint

    min = ma_fields.Nested(ValueSchema, allow_none=True)
    max = ma_fields.Nested(ValueSchema, allow_none=True)


class SetParameterValueConstraintSchema(DefaultSchema[SetParameterValueConstraint]):
    TARGET_CLS = SetParameterValueConstraint

    values = ma_fields.List(ma_fields.Nested(ValueSchema))


class ParameterValueConstraintSchema(OneOfSchema):
    type_field = 'type'
    type_schemas = {
        ParameterValueConstraintType.all.name: AllParameterValueConstraintSchema,
        ParameterValueConstraintType.range.name: RangeParameterValueConstraintSchema,
        ParameterValueConstraintType.set.name: SetParameterValueConstraintSchema,
    }

    def get_obj_type(self, obj: ParameterValueConstraint) -> str:
        return getattr(obj, self.type_field).name


class ResultFieldSchema(DefaultSchema[ResultField]):
    TARGET_CLS = ResultField

    title = ma_fields.String(required=True)
    source = ma_fields.String()
    guid = ma_fields.String(attribute='id')
    calc_mode = EnumField(CalcMode, required=True)
    hidden = ma_fields.Boolean(load_default=False)
    description = ma_fields.String()
    formula = ma_fields.String(load_default='')
    initial_data_type = EnumField(BIType, allow_none=True)
    cast = EnumField(BIType)
    type = EnumField(FieldType, readonly=True)
    data_type = EnumField(BIType, allow_none=True)
    valid = ma_fields.Boolean(allow_none=True)
    avatar_id = ma_fields.String(allow_none=True)
    aggregation = EnumField(AggregationFunction, load_default=AggregationFunction.none.name)
    has_auto_aggregation = ma_fields.Boolean(allow_none=True)
    lock_aggregation = ma_fields.Boolean(allow_none=True)
    managed_by = EnumField(ManagedBy, allow_none=True, dump_default=ManagedBy.user)
    default_value = ma_fields.Nested(ValueSchema, allow_none=True)
    value_constraint = ma_fields.Nested(ParameterValueConstraintSchema, allow_none=True)

    # Only locally used
    created_ = ma_fields.Boolean(load_default=True, load_only=True, attribute='created_')  # Always True

    @pre_load(pass_many=False)
    def store_type_in_context(self, data: Mapping[str, Any], **_: Any) -> Mapping[str, Any]:
        if 'cast' in data:
            self.context[ValueSchema.CONTEXT_KEY] = data['cast']
        return data


class ResultSchemaAuxSchema(DefaultSchema[ResultSchemaAux]):
    TARGET_CLS = ResultSchemaAux

    inter_dependencies = ma_fields.Dict(allow_none=False)


class WhereClauseSchema(DefaultSchema[WhereClause]):
    TARGET_CLS = WhereClause

    column = ma_fields.String()
    operation = EnumField(WhereClauseOperation)
    values = ma_fields.List(ma_fields.String())


class ObligatoryFilterSchema(DefaultSchema[ObligatoryFilter]):
    TARGET_CLS = ObligatoryFilter

    id = ma_fields.String()
    field_guid = ma_fields.String()
    default_filters = ma_fields.List(ma_fields.Nested(WhereClauseSchema))
    managed_by = EnumField(ManagedBy)
    valid = ma_fields.Boolean()


class ColumnSchema(DefaultSchema[Column]):
    TARGET_CLS = Column

    name = ma_fields.String()
    title = ma_fields.String()
    native_type = ma_fields.Dict(allow_none=True)
    user_type = EnumField(BIType)
    description = ma_fields.String(dump_default='', allow_none=True)
    has_auto_aggregation = ma_fields.Boolean(dump_default=False, allow_none=True)
    lock_aggregation = ma_fields.Boolean(dump_default=False, allow_none=True)
    nullable = ma_fields.Boolean(dump_default=None, allow_none=True)


class DataSourceSchema(DefaultSchema[DataSource]):
    TARGET_CLS = DataSource

    id = ma_fields.String()
    title = ma_fields.String()
    is_ref = ma_fields.Boolean()
    connection_id = ma_fields.String(allow_none=True)
    ref_source_id = ma_fields.String(allow_none=True, required=False)
    source_type = DynamicEnumField(CreateDSFrom)
    raw_schema = ma_fields.Nested(ColumnSchema, allow_none=True, required=False, many=True)
    index_info_set = ma_fields.List(ma_fields.Dict, allow_none=True)
    parameters = ma_fields.Dict()
    managed_by = EnumField(ManagedBy, allow_none=True, dump_default=ManagedBy.user)
    valid = ma_fields.Boolean()

    # Only locally used
    created_ = ma_fields.Boolean(load_default=True, load_only=True, attribute='created_')  # Always True


class SourceAvatarSchema(DefaultSchema[SourceAvatar]):
    TARGET_CLS = SourceAvatar

    id = ma_fields.String(required=True)
    source_id = ma_fields.String()
    title = ma_fields.String()
    is_root = ma_fields.Boolean()
    managed_by = EnumField(ManagedBy, allow_none=True, dump_default=ManagedBy.user)
    valid = ma_fields.Boolean()

    # Only locally used
    created_ = ma_fields.Boolean(load_default=True, load_only=True, attribute='created_')  # Always True


class ConditionPartDirectSchema(DefaultSchema[DirectJoinPart]):
    TARGET_CLS = DirectJoinPart

    source = ma_fields.String(required=True)


class ConditionPartFormulaSchema(DefaultSchema[FormulaJoinPart]):
    TARGET_CLS = FormulaJoinPart

    formula = ma_fields.String(required=True)


class ConditionPartResultFieldSchema(DefaultSchema[ResultFieldJoinPart]):
    TARGET_CLS = ResultFieldJoinPart

    field_id = ma_fields.String(required=True)


class ConditionPartGenericSchema(OneOfSchema):
    class Meta:
        unknown = EXCLUDE

    type_field_remove = False
    type_field = 'calc_mode'
    type_schemas = {
        ConditionPartCalcMode.direct.name: ConditionPartDirectSchema,
        ConditionPartCalcMode.formula.name: ConditionPartFormulaSchema,
        ConditionPartCalcMode.result_field.name: ConditionPartResultFieldSchema,
    }

    def get_obj_type(self, obj: JoinPart) -> str:
        return getattr(obj, self.type_field).name


class AvatarRelationSchema(DefaultSchema[AvatarRelation]):
    TARGET_CLS = AvatarRelation

    class JoinConditionSchema(DefaultSchema[JoinCondition]):
        TARGET_CLS = JoinCondition

        type = EnumField(JoinConditionType, dump_default=JoinConditionType.binary, dump_only=True)
        operator = EnumField(BinaryJoinOperator, required=True)
        left = ma_fields.Nested(ConditionPartGenericSchema, attribute='left_part', required=True)
        right = ma_fields.Nested(ConditionPartGenericSchema, attribute='right_part', required=True)

    id = ma_fields.String(required=True)
    left_avatar_id = ma_fields.String()
    right_avatar_id = ma_fields.String()
    conditions = ma_fields.Nested(JoinConditionSchema, many=True)
    join_type = EnumField(JoinType)
    managed_by = EnumField(ManagedBy, allow_none=True, dump_default=ManagedBy.user, load_default=ManagedBy.user)

    # Only locally used
    created_ = ma_fields.Boolean(load_default=True, load_only=True, attribute='created_')  # Always True


class ComponentErrorListSchema(DefaultSchema[ComponentErrorRegistry]):
    TARGET_CLS = ComponentErrorRegistry

    class ComponentErrorPackSchema(DefaultSchema[ComponentErrorPack]):
        TARGET_CLS = ComponentErrorPack

        class ComponentErrorSchema(DefaultSchema[ComponentError]):
            TARGET_CLS = ComponentError

            message = ma_fields.String()
            level = EnumField(ComponentErrorLevel)
            code = ma_fields.String()
            details = ma_fields.Dict()

        id = ma_fields.String()
        type = EnumField(ComponentType)
        errors = ma_fields.List(ma_fields.Nested(ComponentErrorSchema))

    items = ma_fields.List(ma_fields.Nested(ComponentErrorPackSchema))


class DatasetContentInternalSchema(DefaultSchema[Dataset]):
    """
    A base class for schemas that need to contain the full dataset description
    """
    TARGET_CLS = Dataset

    sources = ma_fields.Nested(DataSourceSchema, many=True, required=False)
    source_avatars = ma_fields.Nested(SourceAvatarSchema, many=True, required=False)
    avatar_relations = ma_fields.Nested(AvatarRelationSchema, many=True, required=False)
    result_schema = ma_fields.Nested(ResultFieldSchema, many=True, required=False)
    result_schema_aux = ma_fields.Nested(ResultSchemaAuxSchema, allow_none=False)
    rls = ma_fields.Dict(load_default=dict, required=False)
    component_errors = ma_fields.Nested(ComponentErrorListSchema, required=False)
    obligatory_filters = ma_fields.Nested(ObligatoryFilterSchema, many=True, load_default=list)
    revision_id = ma_fields.String(allow_none=True, dump_default=None, load_default=None)
