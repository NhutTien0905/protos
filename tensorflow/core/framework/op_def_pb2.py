# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/op_def.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import attr_value_pb2 as tensorflow_dot_core_dot_framework_dot_attr__value__pb2
from tensorflow.core.framework import full_type_pb2 as tensorflow_dot_core_dot_framework_dot_full__type__pb2
from tensorflow.core.framework import resource_handle_pb2 as tensorflow_dot_core_dot_framework_dot_resource__handle__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&tensorflow/core/framework/op_def.proto\x12\ntensorflow\x1a*tensorflow/core/framework/attr_value.proto\x1a)tensorflow/core/framework/full_type.proto\x1a/tensorflow/core/framework/resource_handle.proto\x1a%tensorflow/core/framework/types.proto\"\xf3\x06\n\x05OpDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\tinput_arg\x18\x02 \x03(\x0b\x32\x18.tensorflow.OpDef.ArgDef\x12,\n\noutput_arg\x18\x03 \x03(\x0b\x32\x18.tensorflow.OpDef.ArgDef\x12\x16\n\x0e\x63ontrol_output\x18\x14 \x03(\t\x12\'\n\x04\x61ttr\x18\x04 \x03(\x0b\x32\x19.tensorflow.OpDef.AttrDef\x12.\n\x0b\x64\x65precation\x18\x08 \x01(\x0b\x32\x19.tensorflow.OpDeprecation\x12\x0f\n\x07summary\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x16\n\x0eis_commutative\x18\x12 \x01(\x08\x12\x14\n\x0cis_aggregate\x18\x10 \x01(\x08\x12\x13\n\x0bis_stateful\x18\x11 \x01(\x08\x12\"\n\x1a\x61llows_uninitialized_input\x18\x13 \x01(\x08\x12$\n\x1cis_distributed_communication\x18\x15 \x01(\x08\x1a\x9c\x02\n\x06\x41rgDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\"\n\x04type\x18\x03 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x11\n\ttype_attr\x18\x04 \x01(\t\x12\x13\n\x0bnumber_attr\x18\x05 \x01(\t\x12\x16\n\x0etype_list_attr\x18\x06 \x01(\t\x12\x42\n\x0bhandle_data\x18\x07 \x03(\x0b\x32-.tensorflow.ResourceHandleProto.DtypeAndShape\x12\x0e\n\x06is_ref\x18\x10 \x01(\x08\x12\x37\n\x16\x65xperimental_full_type\x18\x11 \x01(\x0b\x32\x17.tensorflow.FullTypeDef\x1a\xbd\x01\n\x07\x41ttrDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12,\n\rdefault_value\x18\x03 \x01(\x0b\x32\x15.tensorflow.AttrValue\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bhas_minimum\x18\x05 \x01(\x08\x12\x0f\n\x07minimum\x18\x06 \x01(\x03\x12-\n\x0e\x61llowed_values\x18\x07 \x01(\x0b\x32\x15.tensorflow.AttrValue\"5\n\rOpDeprecation\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x13\n\x0b\x65xplanation\x18\x02 \x01(\t\"\'\n\x06OpList\x12\x1d\n\x02op\x18\x01 \x03(\x0b\x32\x11.tensorflow.OpDefB{\n\x18org.tensorflow.frameworkB\x0bOpDefProtosP\x01ZMgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/op_def_go_proto\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.framework.op_def_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.tensorflow.frameworkB\013OpDefProtosP\001ZMgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/op_def_go_proto\370\001\001'
  _OPDEF._serialized_start=230
  _OPDEF._serialized_end=1113
  _OPDEF_ARGDEF._serialized_start=637
  _OPDEF_ARGDEF._serialized_end=921
  _OPDEF_ATTRDEF._serialized_start=924
  _OPDEF_ATTRDEF._serialized_end=1113
  _OPDEPRECATION._serialized_start=1115
  _OPDEPRECATION._serialized_end=1168
  _OPLIST._serialized_start=1170
  _OPLIST._serialized_end=1209
# @@protoc_insertion_point(module_scope)
