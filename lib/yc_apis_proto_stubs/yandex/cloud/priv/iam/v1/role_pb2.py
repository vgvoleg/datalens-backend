# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/role.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#yandex/cloud/priv/iam/v1/role.proto\x12\x18yandex.cloud.priv.iam.v1\"h\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x16\n\x0epermission_ids\x18\x03 \x03(\t\x12\x11\n\tis_system\x18\x04 \x01(\x08\x12\x14\n\x0c\x63\x61tegory_ids\x18\x05 \x03(\t\"=\n\x0cRoleCategory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\tBOB\x02PRZIa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1;iamb\x06proto3')



_ROLE = DESCRIPTOR.message_types_by_name['Role']
_ROLECATEGORY = DESCRIPTOR.message_types_by_name['RoleCategory']
Role = _reflection.GeneratedProtocolMessageType('Role', (_message.Message,), {
  'DESCRIPTOR' : _ROLE,
  '__module__' : 'yandex.cloud.priv.iam.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.Role)
  })
_sym_db.RegisterMessage(Role)

RoleCategory = _reflection.GeneratedProtocolMessageType('RoleCategory', (_message.Message,), {
  'DESCRIPTOR' : _ROLECATEGORY,
  '__module__' : 'yandex.cloud.priv.iam.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.RoleCategory)
  })
_sym_db.RegisterMessage(RoleCategory)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\002PRZIa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1;iam'
  _ROLE._serialized_start=65
  _ROLE._serialized_end=169
  _ROLECATEGORY._serialized_start=171
  _ROLECATEGORY._serialized_end=232
# @@protoc_insertion_point(module_scope)
