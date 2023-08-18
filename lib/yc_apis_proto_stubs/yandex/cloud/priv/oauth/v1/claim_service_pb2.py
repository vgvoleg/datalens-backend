# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/oauth/v1/claim_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.priv import validation_pb2 as yandex_dot_cloud_dot_priv_dot_validation__pb2
from yandex.cloud.priv.oauth import claims_pb2 as yandex_dot_cloud_dot_priv_dot_oauth_dot_claims__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/priv/oauth/v1/claim_service.proto\x12\x1ayandex.cloud.priv.oauth.v1\x1a\"yandex/cloud/priv/validation.proto\x1a$yandex/cloud/priv/oauth/claims.proto\"\xf5\x03\n\x10GetClaimsRequest\x12\'\n\x0bsubject_ids\x18\x01 \x03(\tB\x12\xc2\x89\x31\x06\x31-1000\xca\x89\x31\x04<=50\x12L\n\x06\x63laims\x18\x02 \x03(\x0e\x32\x32.yandex.cloud.priv.oauth.v1.GetClaimsRequest.ClaimB\x08\xc2\x89\x31\x04<=22\"\xe9\x02\n\x05\x43laim\x12\x15\n\x11\x43LAIM_UNSPECIFIED\x10\x00\x12\x07\n\x03SUB\x10\x01\x12\x08\n\x04NAME\x10\x02\x12\x0e\n\nGIVEN_NAME\x10\x03\x12\x0f\n\x0b\x46\x41MILY_NAME\x10\x04\x12\x16\n\x12PREFERRED_USERNAME\x10\x07\x12\x0b\n\x07PICTURE\x10\t\x12\t\n\x05\x45MAIL\x10\x0b\x12\n\n\x06GENDER\x10\r\x12\x0c\n\x08ZONEINFO\x10\x0f\x12\n\n\x06LOCALE\x10\x10\x12\x10\n\x0cPHONE_NUMBER\x10\x11\x12\x0c\n\x08SUB_TYPE\x10\x63\x12\x0e\n\nFEDERATION\x10\x64\x12\x10\n\x0cPICTURE_DATA\x10\x65\x12\n\n\x06GROUPS\x10g\x12\x16\n\x11YANDEX_CLAIMS_ALL\x10\xc8\x01\x12\x1e\n\x19YANDEX_CLAIMS_STAFF_LOGIN\x10\xc9\x01\x12\x1f\n\x1aYANDEX_CLAIMS_PASSPORT_UID\x10\xca\x01\x12\x18\n\x13YANDEX_CLAIMS_KARMA\x10\xcf\x01\"X\n\x11GetClaimsResponse\x12\x43\n\x0fsubject_details\x18\x02 \x03(\x0b\x32*.yandex.cloud.priv.oauth.v1.SubjectDetails\"V\n\x0eSubjectDetails\x12\x44\n\x0esubject_claims\x18\x01 \x01(\x0b\x32&.yandex.cloud.priv.oauth.SubjectClaimsB\x04\xa8\x89\x31\x01\x32r\n\x0c\x43laimService\x12\x62\n\x03Get\x12,.yandex.cloud.priv.oauth.v1.GetClaimsRequest\x1a-.yandex.cloud.priv.oauth.v1.GetClaimsResponseBUB\x04PACSZMa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/oauth/v1;oauthb\x06proto3')



_GETCLAIMSREQUEST = DESCRIPTOR.message_types_by_name['GetClaimsRequest']
_GETCLAIMSRESPONSE = DESCRIPTOR.message_types_by_name['GetClaimsResponse']
_SUBJECTDETAILS = DESCRIPTOR.message_types_by_name['SubjectDetails']
_GETCLAIMSREQUEST_CLAIM = _GETCLAIMSREQUEST.enum_types_by_name['Claim']
GetClaimsRequest = _reflection.GeneratedProtocolMessageType('GetClaimsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLAIMSREQUEST,
  '__module__' : 'yandex.cloud.priv.oauth.v1.claim_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.oauth.v1.GetClaimsRequest)
  })
_sym_db.RegisterMessage(GetClaimsRequest)

GetClaimsResponse = _reflection.GeneratedProtocolMessageType('GetClaimsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCLAIMSRESPONSE,
  '__module__' : 'yandex.cloud.priv.oauth.v1.claim_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.oauth.v1.GetClaimsResponse)
  })
_sym_db.RegisterMessage(GetClaimsResponse)

SubjectDetails = _reflection.GeneratedProtocolMessageType('SubjectDetails', (_message.Message,), {
  'DESCRIPTOR' : _SUBJECTDETAILS,
  '__module__' : 'yandex.cloud.priv.oauth.v1.claim_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.oauth.v1.SubjectDetails)
  })
_sym_db.RegisterMessage(SubjectDetails)

_CLAIMSERVICE = DESCRIPTOR.services_by_name['ClaimService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\004PACSZMa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/oauth/v1;oauth'
  _GETCLAIMSREQUEST.fields_by_name['subject_ids']._options = None
  _GETCLAIMSREQUEST.fields_by_name['subject_ids']._serialized_options = b'\302\2111\0061-1000\312\2111\004<=50'
  _GETCLAIMSREQUEST.fields_by_name['claims']._options = None
  _GETCLAIMSREQUEST.fields_by_name['claims']._serialized_options = b'\302\2111\004<=22'
  _SUBJECTDETAILS.fields_by_name['subject_claims']._options = None
  _SUBJECTDETAILS.fields_by_name['subject_claims']._serialized_options = b'\250\2111\001'
  _GETCLAIMSREQUEST._serialized_start=153
  _GETCLAIMSREQUEST._serialized_end=654
  _GETCLAIMSREQUEST_CLAIM._serialized_start=293
  _GETCLAIMSREQUEST_CLAIM._serialized_end=654
  _GETCLAIMSRESPONSE._serialized_start=656
  _GETCLAIMSRESPONSE._serialized_end=744
  _SUBJECTDETAILS._serialized_start=746
  _SUBJECTDETAILS._serialized_end=832
  _CLAIMSERVICE._serialized_start=834
  _CLAIMSERVICE._serialized_end=948
# @@protoc_insertion_point(module_scope)
