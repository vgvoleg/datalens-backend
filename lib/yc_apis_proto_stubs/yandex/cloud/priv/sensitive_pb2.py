# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/sensitive.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!yandex/cloud/priv/sensitive.proto\x12\x11yandex.cloud.priv\x1a google/protobuf/descriptor.proto*\xa4\x02\n\rSensitiveType\x12\x1e\n\x1aSENSITIVE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rSENSITIVE_CRC\x10\x01\x12\x17\n\x13SENSITIVE_IAM_TOKEN\x10\x02\x12\x14\n\x10SENSITIVE_REMOVE\x10\x03\x12)\n%SENSITIVE_YANDEX_PASSPORT_OAUTH_TOKEN\x10\x04\x12\x18\n\x14SENSITIVE_IAM_COOKIE\x10\x05\x12\x1b\n\x17SENSITIVE_REFRESH_TOKEN\x10\x06\x12\x11\n\rSENSITIVE_JWT\x10\x07\x12\x1b\n\x17SENSITIVE_COOKIE_HEADER\x10\x08\x12\x1f\n\x1bSENSITIVE_SET_COOKIE_HEADER\x10\t:2\n\tsensitive\x12\x1d.google.protobuf.FieldOptions\x18\xf9\x91\x06 \x01(\x08:Y\n\x0esensitive_type\x12\x1d.google.protobuf.FieldOptions\x18\xfa\x91\x06 \x01(\x0e\x32 .yandex.cloud.priv.SensitiveTypeBFZDa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv;cloudb\x06proto3')

_SENSITIVETYPE = DESCRIPTOR.enum_types_by_name['SensitiveType']
SensitiveType = enum_type_wrapper.EnumTypeWrapper(_SENSITIVETYPE)
SENSITIVE_TYPE_UNSPECIFIED = 0
SENSITIVE_CRC = 1
SENSITIVE_IAM_TOKEN = 2
SENSITIVE_REMOVE = 3
SENSITIVE_YANDEX_PASSPORT_OAUTH_TOKEN = 4
SENSITIVE_IAM_COOKIE = 5
SENSITIVE_REFRESH_TOKEN = 6
SENSITIVE_JWT = 7
SENSITIVE_COOKIE_HEADER = 8
SENSITIVE_SET_COOKIE_HEADER = 9

SENSITIVE_FIELD_NUMBER = 100601
sensitive = DESCRIPTOR.extensions_by_name['sensitive']
SENSITIVE_TYPE_FIELD_NUMBER = 100602
sensitive_type = DESCRIPTOR.extensions_by_name['sensitive_type']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(sensitive)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(sensitive_type)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv;cloud'
  _SENSITIVETYPE._serialized_start=91
  _SENSITIVETYPE._serialized_end=383
# @@protoc_insertion_point(module_scope)
