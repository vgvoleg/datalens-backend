# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/oauth_scope.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/priv/iam/v1/oauth_scope.proto\x12\x18yandex.cloud.priv.iam.v1\"T\n\nOAuthScope\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tis_system\x18\x02 \x01(\x08\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x16\n\x0epermission_ids\x18\x04 \x03(\tBQB\x04POASZIa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1;iamb\x06proto3')



_OAUTHSCOPE = DESCRIPTOR.message_types_by_name['OAuthScope']
OAuthScope = _reflection.GeneratedProtocolMessageType('OAuthScope', (_message.Message,), {
  'DESCRIPTOR' : _OAUTHSCOPE,
  '__module__' : 'yandex.cloud.priv.iam.v1.oauth_scope_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.OAuthScope)
  })
_sym_db.RegisterMessage(OAuthScope)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\004POASZIa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1;iam'
  _OAUTHSCOPE._serialized_start=72
  _OAUTHSCOPE._serialized_end=156
# @@protoc_insertion_point(module_scope)
