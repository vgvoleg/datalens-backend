# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/reference/reference.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/priv/reference/reference.proto\x12\x1byandex.cloud.priv.reference\"\xba\x01\n\tReference\x12\x37\n\x08referrer\x18\x01 \x01(\x0b\x32%.yandex.cloud.priv.reference.Referrer\x12\x39\n\x04type\x18\x02 \x01(\x0e\x32+.yandex.cloud.priv.reference.Reference.Type\"9\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nMANAGED_BY\x10\x01\x12\x0b\n\x07USED_BY\x10\x02\"$\n\x08Referrer\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\tBZB\x04PREFZRa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/reference;referenceb\x06proto3')



_REFERENCE = DESCRIPTOR.message_types_by_name['Reference']
_REFERRER = DESCRIPTOR.message_types_by_name['Referrer']
_REFERENCE_TYPE = _REFERENCE.enum_types_by_name['Type']
Reference = _reflection.GeneratedProtocolMessageType('Reference', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCE,
  '__module__' : 'yandex.cloud.priv.reference.reference_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.reference.Reference)
  })
_sym_db.RegisterMessage(Reference)

Referrer = _reflection.GeneratedProtocolMessageType('Referrer', (_message.Message,), {
  'DESCRIPTOR' : _REFERRER,
  '__module__' : 'yandex.cloud.priv.reference.reference_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.reference.Referrer)
  })
_sym_db.RegisterMessage(Referrer)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\004PREFZRa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/reference;reference'
  _REFERENCE._serialized_start=77
  _REFERENCE._serialized_end=263
  _REFERENCE_TYPE._serialized_start=206
  _REFERENCE_TYPE._serialized_end=263
  _REFERRER._serialized_start=265
  _REFERRER._serialized_end=301
# @@protoc_insertion_point(module_scope)
