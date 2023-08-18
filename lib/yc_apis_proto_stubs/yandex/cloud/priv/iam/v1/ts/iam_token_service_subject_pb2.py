# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/ts/iam_token_service_subject.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;yandex/cloud/priv/iam/v1/ts/iam_token_service_subject.proto\x12\x1byandex.cloud.priv.iam.v1.ts\x1a\"yandex/cloud/priv/validation.proto\"\x86\x02\n\x07Subject\x12H\n\x0cuser_account\x18\x01 \x01(\x0b\x32\x30.yandex.cloud.priv.iam.v1.ts.Subject.UserAccountH\x00\x12N\n\x0fservice_account\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.priv.iam.v1.ts.Subject.ServiceAccountH\x00\x1a\'\n\x0bUserAccount\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x1a*\n\x0eServiceAccount\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50B\x0c\n\x04type\x12\x04\x80\x83\x31\x01\x42TB\x04PITSZLa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1/ts;iamb\x06proto3')



_SUBJECT = DESCRIPTOR.message_types_by_name['Subject']
_SUBJECT_USERACCOUNT = _SUBJECT.nested_types_by_name['UserAccount']
_SUBJECT_SERVICEACCOUNT = _SUBJECT.nested_types_by_name['ServiceAccount']
Subject = _reflection.GeneratedProtocolMessageType('Subject', (_message.Message,), {

  'UserAccount' : _reflection.GeneratedProtocolMessageType('UserAccount', (_message.Message,), {
    'DESCRIPTOR' : _SUBJECT_USERACCOUNT,
    '__module__' : 'yandex.cloud.priv.iam.v1.ts.iam_token_service_subject_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.ts.Subject.UserAccount)
    })
  ,

  'ServiceAccount' : _reflection.GeneratedProtocolMessageType('ServiceAccount', (_message.Message,), {
    'DESCRIPTOR' : _SUBJECT_SERVICEACCOUNT,
    '__module__' : 'yandex.cloud.priv.iam.v1.ts.iam_token_service_subject_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.ts.Subject.ServiceAccount)
    })
  ,
  'DESCRIPTOR' : _SUBJECT,
  '__module__' : 'yandex.cloud.priv.iam.v1.ts.iam_token_service_subject_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.ts.Subject)
  })
_sym_db.RegisterMessage(Subject)
_sym_db.RegisterMessage(Subject.UserAccount)
_sym_db.RegisterMessage(Subject.ServiceAccount)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\004PITSZLa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1/ts;iam'
  _SUBJECT_USERACCOUNT.fields_by_name['id']._options = None
  _SUBJECT_USERACCOUNT.fields_by_name['id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _SUBJECT_SERVICEACCOUNT.fields_by_name['id']._options = None
  _SUBJECT_SERVICEACCOUNT.fields_by_name['id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _SUBJECT.oneofs_by_name['type']._options = None
  _SUBJECT.oneofs_by_name['type']._serialized_options = b'\200\2031\001'
  _SUBJECT._serialized_start=129
  _SUBJECT._serialized_end=391
  _SUBJECT_USERACCOUNT._serialized_start=294
  _SUBJECT_USERACCOUNT._serialized_end=333
  _SUBJECT_SERVICEACCOUNT._serialized_start=335
  _SUBJECT_SERVICEACCOUNT._serialized_end=377
# @@protoc_insertion_point(module_scope)
