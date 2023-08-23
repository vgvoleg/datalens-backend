# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/mdb/greenplum/v1/backup_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2
from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2
from yandex.cloud.priv.mdb.greenplum.v1 import backup_pb2 as yandex_dot_cloud_dot_priv_dot_mdb_dot_greenplum_dot_v1_dot_backup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/priv/mdb/greenplum/v1/backup_service.proto\x12\"yandex.cloud.priv.mdb.greenplum.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a+yandex/cloud/priv/operation/operation.proto\x1a\"yandex/cloud/priv/validation.proto\x1a/yandex/cloud/priv/mdb/greenplum/v1/backup.proto\"+\n\x10GetBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\"s\n\x12ListBackupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xa8\x89\x31\x01\xca\x89\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xba\x89\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\xca\x89\x31\x05<=100\"k\n\x13ListBackupsResponse\x12;\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32*.yandex.cloud.priv.mdb.greenplum.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\".\n\x13\x44\x65leteBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xa8\x89\x31\x01\"=\n\x14\x44\x65leteBackupMetadata\x12\x11\n\tbackup_id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t2\x8d\x04\n\rBackupService\x12\x96\x01\n\x03Get\x12\x34.yandex.cloud.priv.mdb.greenplum.v1.GetBackupRequest\x1a*.yandex.cloud.priv.mdb.greenplum.v1.Backup\"-\x82\xd3\xe4\x93\x02\'\x12%/mdb/greenplum/v1/backups/{backup_id}\x12\x9a\x01\n\x04List\x12\x36.yandex.cloud.priv.mdb.greenplum.v1.ListBackupsRequest\x1a\x37.yandex.cloud.priv.mdb.greenplum.v1.ListBackupsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/mdb/greenplum/v1/backups\x12\xc5\x01\n\x06\x44\x65lete\x12\x37.yandex.cloud.priv.mdb.greenplum.v1.DeleteBackupRequest\x1a&.yandex.cloud.priv.operation.Operation\"Z\x82\xd3\xe4\x93\x02#*!/mdb/mysql/v1/backups/{backup_id}\xb2\xd2*-\n\x14\x44\x65leteBackupMetadata\x12\x15google.protobuf.EmptyBaB\x04PGBSZYa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/mdb/greenplum/v1;greenplumb\x06proto3')



_GETBACKUPREQUEST = DESCRIPTOR.message_types_by_name['GetBackupRequest']
_LISTBACKUPSREQUEST = DESCRIPTOR.message_types_by_name['ListBackupsRequest']
_LISTBACKUPSRESPONSE = DESCRIPTOR.message_types_by_name['ListBackupsResponse']
_DELETEBACKUPREQUEST = DESCRIPTOR.message_types_by_name['DeleteBackupRequest']
_DELETEBACKUPMETADATA = DESCRIPTOR.message_types_by_name['DeleteBackupMetadata']
GetBackupRequest = _reflection.GeneratedProtocolMessageType('GetBackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBACKUPREQUEST,
  '__module__' : 'yandex.cloud.priv.mdb.greenplum.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.mdb.greenplum.v1.GetBackupRequest)
  })
_sym_db.RegisterMessage(GetBackupRequest)

ListBackupsRequest = _reflection.GeneratedProtocolMessageType('ListBackupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBACKUPSREQUEST,
  '__module__' : 'yandex.cloud.priv.mdb.greenplum.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.mdb.greenplum.v1.ListBackupsRequest)
  })
_sym_db.RegisterMessage(ListBackupsRequest)

ListBackupsResponse = _reflection.GeneratedProtocolMessageType('ListBackupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBACKUPSRESPONSE,
  '__module__' : 'yandex.cloud.priv.mdb.greenplum.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.mdb.greenplum.v1.ListBackupsResponse)
  })
_sym_db.RegisterMessage(ListBackupsResponse)

DeleteBackupRequest = _reflection.GeneratedProtocolMessageType('DeleteBackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKUPREQUEST,
  '__module__' : 'yandex.cloud.priv.mdb.greenplum.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.mdb.greenplum.v1.DeleteBackupRequest)
  })
_sym_db.RegisterMessage(DeleteBackupRequest)

DeleteBackupMetadata = _reflection.GeneratedProtocolMessageType('DeleteBackupMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKUPMETADATA,
  '__module__' : 'yandex.cloud.priv.mdb.greenplum.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.mdb.greenplum.v1.DeleteBackupMetadata)
  })
_sym_db.RegisterMessage(DeleteBackupMetadata)

_BACKUPSERVICE = DESCRIPTOR.services_by_name['BackupService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\004PGBSZYa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/mdb/greenplum/v1;greenplum'
  _GETBACKUPREQUEST.fields_by_name['backup_id']._options = None
  _GETBACKUPREQUEST.fields_by_name['backup_id']._serialized_options = b'\250\2111\001'
  _LISTBACKUPSREQUEST.fields_by_name['folder_id']._options = None
  _LISTBACKUPSREQUEST.fields_by_name['folder_id']._serialized_options = b'\250\2111\001\312\2111\004<=50'
  _LISTBACKUPSREQUEST.fields_by_name['page_size']._options = None
  _LISTBACKUPSREQUEST.fields_by_name['page_size']._serialized_options = b'\272\2111\0060-1000'
  _LISTBACKUPSREQUEST.fields_by_name['page_token']._options = None
  _LISTBACKUPSREQUEST.fields_by_name['page_token']._serialized_options = b'\312\2111\005<=100'
  _DELETEBACKUPREQUEST.fields_by_name['backup_id']._options = None
  _DELETEBACKUPREQUEST.fields_by_name['backup_id']._serialized_options = b'\250\2111\001'
  _BACKUPSERVICE.methods_by_name['Get']._options = None
  _BACKUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\'\022%/mdb/greenplum/v1/backups/{backup_id}'
  _BACKUPSERVICE.methods_by_name['List']._options = None
  _BACKUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\033\022\031/mdb/greenplum/v1/backups'
  _BACKUPSERVICE.methods_by_name['Delete']._options = None
  _BACKUPSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002#*!/mdb/mysql/v1/backups/{backup_id}\262\322*-\n\024DeleteBackupMetadata\022\025google.protobuf.Empty'
  _GETBACKUPREQUEST._serialized_start=289
  _GETBACKUPREQUEST._serialized_end=332
  _LISTBACKUPSREQUEST._serialized_start=334
  _LISTBACKUPSREQUEST._serialized_end=449
  _LISTBACKUPSRESPONSE._serialized_start=451
  _LISTBACKUPSRESPONSE._serialized_end=558
  _DELETEBACKUPREQUEST._serialized_start=560
  _DELETEBACKUPREQUEST._serialized_end=606
  _DELETEBACKUPMETADATA._serialized_start=608
  _DELETEBACKUPMETADATA._serialized_end=669
  _BACKUPSERVICE._serialized_start=672
  _BACKUPSERVICE._serialized_end=1197
# @@protoc_insertion_point(module_scope)