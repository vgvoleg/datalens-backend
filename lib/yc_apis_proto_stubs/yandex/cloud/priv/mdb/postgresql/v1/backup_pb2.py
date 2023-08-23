# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/mdb/postgresql/v1/backup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/priv/mdb/postgresql/v1/backup.proto\x12#yandex.cloud.priv.mdb.postgresql.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x90\x04\n\x06\x42\x61\x63kup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11source_cluster_id\x18\x04 \x01(\t\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04size\x18\x06 \x01(\x03\x12L\n\x04type\x18\x07 \x01(\x0e\x32>.yandex.cloud.priv.mdb.postgresql.v1.Backup.BackupCreationType\x12H\n\x06method\x18\x08 \x01(\x0e\x32\x38.yandex.cloud.priv.mdb.postgresql.v1.Backup.BackupMethod\x12\x14\n\x0cjournal_size\x18\t \x01(\x03\"Y\n\x0c\x42\x61\x63kupMethod\x12\x1d\n\x19\x42\x41\x43KUP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04\x42\x41SE\x10\x01\x12\x0f\n\x0bINCREMENTAL\x10\x02\x12\x0f\n\x0bSCHEMA_ONLY\x10\x03\"U\n\x12\x42\x61\x63kupCreationType\x12$\n BACKUP_CREATION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tAUTOMATED\x10\x01\x12\n\n\x06MANUAL\x10\x02\x42\x62\x42\x03PPBZ[a.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/mdb/postgresql/v1;postgresqlb\x06proto3')



_BACKUP = DESCRIPTOR.message_types_by_name['Backup']
_BACKUP_BACKUPMETHOD = _BACKUP.enum_types_by_name['BackupMethod']
_BACKUP_BACKUPCREATIONTYPE = _BACKUP.enum_types_by_name['BackupCreationType']
Backup = _reflection.GeneratedProtocolMessageType('Backup', (_message.Message,), {
  'DESCRIPTOR' : _BACKUP,
  '__module__' : 'yandex.cloud.priv.mdb.postgresql.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.mdb.postgresql.v1.Backup)
  })
_sym_db.RegisterMessage(Backup)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\003PPBZ[a.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/mdb/postgresql/v1;postgresql'
  _BACKUP._serialized_start=123
  _BACKUP._serialized_end=651
  _BACKUP_BACKUPMETHOD._serialized_start=475
  _BACKUP_BACKUPMETHOD._serialized_end=564
  _BACKUP_BACKUPCREATIONTYPE._serialized_start=566
  _BACKUP_BACKUPCREATIONTYPE._serialized_end=651
# @@protoc_insertion_point(module_scope)