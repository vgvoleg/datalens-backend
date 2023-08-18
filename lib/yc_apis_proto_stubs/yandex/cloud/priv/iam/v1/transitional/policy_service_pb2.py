# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/priv/iam/v1/transitional/policy_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/priv/iam/v1/transitional/policy_service.proto\x12%yandex.cloud.priv.iam.v1.transitional\x1a\x1cgoogle/api/annotations.proto\"\'\n\x13ListPoliciesRequest\x12\x10\n\x08\x63loud_id\x18\x01 \x01(\t\"+\n\x19ListPoliciesCompatRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\"\x18\n\nAssignment\x12\n\n\x02id\x18\x01 \x01(\t\"Y\n\x14ListPoliciesResponse\x12\x41\n\x06result\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.priv.iam.v1.transitional.Assignment\"7\n\x10SetPolicyRequest\x12\x10\n\x08\x63loud_id\x18\x01 \x01(\t\x12\x11\n\tpolicy_id\x18\x02 \x01(\t\";\n\x16SetPolicyCompatRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x11\n\tpolicy_id\x18\x02 \x01(\t\"/\n\x11SetPolicyResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\">\n\x13\x44\x65letePolicyRequest\x12\x10\n\x08\x63loud_id\x18\x01 \x01(\t\x12\x15\n\rassignment_id\x18\x02 \x01(\t\"B\n\x19\x44\x65letePolicyCompatRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x15\n\rassignment_id\x18\x02 \x01(\t\"&\n\x14\x44\x65letePolicyResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xcf\x08\n\rPolicyService\x12\xaa\x01\n\x04List\x12:.yandex.cloud.priv.iam.v1.transitional.ListPoliciesRequest\x1a;.yandex.cloud.priv.iam.v1.transitional.ListPoliciesResponse\")\x82\xd3\xe4\x93\x02#\x12!/iam/v1/cloud/{cloud_id}/policies\x12\xb2\x01\n\nListCompat\x12@.yandex.cloud.priv.iam.v1.transitional.ListPoliciesCompatRequest\x1a;.yandex.cloud.priv.iam.v1.transitional.ListPoliciesResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/iam/v1/org/{org_id}/policies\x12\xa6\x01\n\x03Set\x12\x37.yandex.cloud.priv.iam.v1.transitional.SetPolicyRequest\x1a\x38.yandex.cloud.priv.iam.v1.transitional.SetPolicyResponse\",\x82\xd3\xe4\x93\x02&\"!/iam/v1/cloud/{cloud_id}/policies:\x01*\x12\xae\x01\n\tSetCompat\x12=.yandex.cloud.priv.iam.v1.transitional.SetPolicyCompatRequest\x1a\x38.yandex.cloud.priv.iam.v1.transitional.SetPolicyResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/iam/v1/org/{org_id}/policies:\x01*\x12\xba\x01\n\x06\x44\x65lete\x12:.yandex.cloud.priv.iam.v1.transitional.DeletePolicyRequest\x1a;.yandex.cloud.priv.iam.v1.transitional.DeletePolicyResponse\"7\x82\xd3\xe4\x93\x02\x31*//iam/v1/cloud/{cloud_id}/policy/{assignment_id}\x12\xc4\x01\n\x0c\x44\x65leteCompat\x12@.yandex.cloud.priv.iam.v1.transitional.DeletePolicyCompatRequest\x1a;.yandex.cloud.priv.iam.v1.transitional.DeletePolicyResponse\"5\x82\xd3\xe4\x93\x02/*-/iam/v1/cloud/{org_id}/policy/{assignment_id}B^B\x04PTPSZVa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1/transitional;iamb\x06proto3')



_LISTPOLICIESREQUEST = DESCRIPTOR.message_types_by_name['ListPoliciesRequest']
_LISTPOLICIESCOMPATREQUEST = DESCRIPTOR.message_types_by_name['ListPoliciesCompatRequest']
_ASSIGNMENT = DESCRIPTOR.message_types_by_name['Assignment']
_LISTPOLICIESRESPONSE = DESCRIPTOR.message_types_by_name['ListPoliciesResponse']
_SETPOLICYREQUEST = DESCRIPTOR.message_types_by_name['SetPolicyRequest']
_SETPOLICYCOMPATREQUEST = DESCRIPTOR.message_types_by_name['SetPolicyCompatRequest']
_SETPOLICYRESPONSE = DESCRIPTOR.message_types_by_name['SetPolicyResponse']
_DELETEPOLICYREQUEST = DESCRIPTOR.message_types_by_name['DeletePolicyRequest']
_DELETEPOLICYCOMPATREQUEST = DESCRIPTOR.message_types_by_name['DeletePolicyCompatRequest']
_DELETEPOLICYRESPONSE = DESCRIPTOR.message_types_by_name['DeletePolicyResponse']
ListPoliciesRequest = _reflection.GeneratedProtocolMessageType('ListPoliciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPOLICIESREQUEST,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.ListPoliciesRequest)
  })
_sym_db.RegisterMessage(ListPoliciesRequest)

ListPoliciesCompatRequest = _reflection.GeneratedProtocolMessageType('ListPoliciesCompatRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPOLICIESCOMPATREQUEST,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.ListPoliciesCompatRequest)
  })
_sym_db.RegisterMessage(ListPoliciesCompatRequest)

Assignment = _reflection.GeneratedProtocolMessageType('Assignment', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNMENT,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.Assignment)
  })
_sym_db.RegisterMessage(Assignment)

ListPoliciesResponse = _reflection.GeneratedProtocolMessageType('ListPoliciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPOLICIESRESPONSE,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.ListPoliciesResponse)
  })
_sym_db.RegisterMessage(ListPoliciesResponse)

SetPolicyRequest = _reflection.GeneratedProtocolMessageType('SetPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOLICYREQUEST,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.SetPolicyRequest)
  })
_sym_db.RegisterMessage(SetPolicyRequest)

SetPolicyCompatRequest = _reflection.GeneratedProtocolMessageType('SetPolicyCompatRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOLICYCOMPATREQUEST,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.SetPolicyCompatRequest)
  })
_sym_db.RegisterMessage(SetPolicyCompatRequest)

SetPolicyResponse = _reflection.GeneratedProtocolMessageType('SetPolicyResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPOLICYRESPONSE,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.SetPolicyResponse)
  })
_sym_db.RegisterMessage(SetPolicyResponse)

DeletePolicyRequest = _reflection.GeneratedProtocolMessageType('DeletePolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOLICYREQUEST,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.DeletePolicyRequest)
  })
_sym_db.RegisterMessage(DeletePolicyRequest)

DeletePolicyCompatRequest = _reflection.GeneratedProtocolMessageType('DeletePolicyCompatRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOLICYCOMPATREQUEST,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.DeletePolicyCompatRequest)
  })
_sym_db.RegisterMessage(DeletePolicyCompatRequest)

DeletePolicyResponse = _reflection.GeneratedProtocolMessageType('DeletePolicyResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOLICYRESPONSE,
  '__module__' : 'yandex.cloud.priv.iam.v1.transitional.policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.priv.iam.v1.transitional.DeletePolicyResponse)
  })
_sym_db.RegisterMessage(DeletePolicyResponse)

_POLICYSERVICE = DESCRIPTOR.services_by_name['PolicyService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\004PTPSZVa.yandex-team.ru/cloud/bitbucket/private-api/yandex/cloud/priv/iam/v1/transitional;iam'
  _POLICYSERVICE.methods_by_name['List']._options = None
  _POLICYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002#\022!/iam/v1/cloud/{cloud_id}/policies'
  _POLICYSERVICE.methods_by_name['ListCompat']._options = None
  _POLICYSERVICE.methods_by_name['ListCompat']._serialized_options = b'\202\323\344\223\002\037\022\035/iam/v1/org/{org_id}/policies'
  _POLICYSERVICE.methods_by_name['Set']._options = None
  _POLICYSERVICE.methods_by_name['Set']._serialized_options = b'\202\323\344\223\002&\"!/iam/v1/cloud/{cloud_id}/policies:\001*'
  _POLICYSERVICE.methods_by_name['SetCompat']._options = None
  _POLICYSERVICE.methods_by_name['SetCompat']._serialized_options = b'\202\323\344\223\002\"\"\035/iam/v1/org/{org_id}/policies:\001*'
  _POLICYSERVICE.methods_by_name['Delete']._options = None
  _POLICYSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\0021*//iam/v1/cloud/{cloud_id}/policy/{assignment_id}'
  _POLICYSERVICE.methods_by_name['DeleteCompat']._options = None
  _POLICYSERVICE.methods_by_name['DeleteCompat']._serialized_options = b'\202\323\344\223\002/*-/iam/v1/cloud/{org_id}/policy/{assignment_id}'
  _LISTPOLICIESREQUEST._serialized_start=131
  _LISTPOLICIESREQUEST._serialized_end=170
  _LISTPOLICIESCOMPATREQUEST._serialized_start=172
  _LISTPOLICIESCOMPATREQUEST._serialized_end=215
  _ASSIGNMENT._serialized_start=217
  _ASSIGNMENT._serialized_end=241
  _LISTPOLICIESRESPONSE._serialized_start=243
  _LISTPOLICIESRESPONSE._serialized_end=332
  _SETPOLICYREQUEST._serialized_start=334
  _SETPOLICYREQUEST._serialized_end=389
  _SETPOLICYCOMPATREQUEST._serialized_start=391
  _SETPOLICYCOMPATREQUEST._serialized_end=450
  _SETPOLICYRESPONSE._serialized_start=452
  _SETPOLICYRESPONSE._serialized_end=499
  _DELETEPOLICYREQUEST._serialized_start=501
  _DELETEPOLICYREQUEST._serialized_end=563
  _DELETEPOLICYCOMPATREQUEST._serialized_start=565
  _DELETEPOLICYCOMPATREQUEST._serialized_end=631
  _DELETEPOLICYRESPONSE._serialized_start=633
  _DELETEPOLICYRESPONSE._serialized_end=671
  _POLICYSERVICE._serialized_start=674
  _POLICYSERVICE._serialized_end=1777
# @@protoc_insertion_point(module_scope)
