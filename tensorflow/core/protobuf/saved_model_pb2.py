# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/saved_model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.protobuf import meta_graph_pb2 as tensorflow_dot_core_dot_protobuf_dot_meta__graph__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*tensorflow/core/protobuf/saved_model.proto\x12\ntensorflow\x1a)tensorflow/core/protobuf/meta_graph.proto\"_\n\nSavedModel\x12\"\n\x1asaved_model_schema_version\x18\x01 \x01(\x03\x12-\n\x0bmeta_graphs\x18\x02 \x03(\x0b\x32\x18.tensorflow.MetaGraphDefB\x88\x01\n\x18org.tensorflow.frameworkB\x10SavedModelProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.protobuf.saved_model_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.tensorflow.frameworkB\020SavedModelProtosP\001ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\370\001\001'
  _SAVEDMODEL._serialized_start=101
  _SAVEDMODEL._serialized_end=196
# @@protoc_insertion_point(module_scope)