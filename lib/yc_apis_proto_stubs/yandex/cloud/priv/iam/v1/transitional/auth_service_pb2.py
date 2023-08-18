# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/transitional/auth_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.priv import sensitive_pb2 as yandex_dot_cloud_dot_priv_dot_sensitive__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/priv/iam/v1/transitional/auth_service.proto\x12%yandex.cloud.priv.iam.v1.transitional\x1a\x1cgoogle/api/annotations.proto\x1a!yandex/cloud/priv/sensitive.proto\"+\n\x10SessionIdRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"B\n\x11SessionIdResponse\x12\x13\n\x05token\x18\x01 \x01(\tB\x04\xc8\x8f\x31\x01\x12\x18\n\nsecret_key\x18\x02 \x01(\tB\x04\xc8\x8f\x31\x01\x32\xb2\x01\n\x0b\x41uthService\x12\xa2\x01\n\tSessionId\x12\x37.yandex.cloud.priv.iam.v1.transitional.SessionIdRequest\x1a\x38.yandex.cloud.priv.iam.v1.transitional.SessionIdResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/iam/v1/auth/session_id:\x01*B^B\x04PTASZVa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1/transitional;iamb\x06proto3')



_SESSIONIDREQUEST = DESCRIPTOR.message_types_by_name['SessionIdRequest']
_SESSIONIDRESPONSE = DESCRIPTOR.message_types_by_name['SessionIdResponse']
SessionIdRequest = _reflection.GeneratedProtocolMessageType('SessionIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONIDREQUEST,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.SessionIdRequest)
  })
_sym_db.RegisterMessage(SessionIdRequest)

SessionIdResponse = _reflection.GeneratedProtocolMessageType('SessionIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONIDRESPONSE,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.SessionIdResponse)
  })
_sym_db.RegisterMessage(SessionIdResponse)

_AUTHSERVICE = DESCRIPTOR.services_by_name['AuthService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\004PTASZVa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1/transitional;iam'
  _SESSIONIDRESPONSE.fields_by_name['token']._options = None
  _SESSIONIDRESPONSE.fields_by_name['token']._serialized_options = b'\310\2171\001'
  _SESSIONIDRESPONSE.fields_by_name['secret_key']._options = None
  _SESSIONIDRESPONSE.fields_by_name['secret_key']._serialized_options = b'\310\2171\001'
  _AUTHSERVICE.methods_by_name['SessionId']._options = None
  _AUTHSERVICE.methods_by_name['SessionId']._serialized_options = b'\202\323\344\223\002\034\"\027/iam/v1/auth/session_id:\001*'
  _SESSIONIDREQUEST._serialized_start=164
  _SESSIONIDREQUEST._serialized_end=207
  _SESSIONIDRESPONSE._serialized_start=209
  _SESSIONIDRESPONSE._serialized_end=275
  _AUTHSERVICE._serialized_start=278
  _AUTHSERVICE._serialized_end=456
# @@protoc_insertion_point(module_scope)
