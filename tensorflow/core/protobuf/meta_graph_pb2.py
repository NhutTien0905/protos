# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/meta_graph.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from tensorflow.core.framework import graph_pb2 as tensorflow_dot_core_dot_framework_dot_graph__pb2
from tensorflow.core.framework import op_def_pb2 as tensorflow_dot_core_dot_framework_dot_op__def__pb2
from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2
from tensorflow.core.protobuf import saved_object_graph_pb2 as tensorflow_dot_core_dot_protobuf_dot_saved__object__graph__pb2
from tensorflow.core.protobuf import saver_pb2 as tensorflow_dot_core_dot_protobuf_dot_saver__pb2
from tensorflow.core.protobuf import struct_pb2 as tensorflow_dot_core_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)tensorflow/core/protobuf/meta_graph.proto\x12\ntensorflow\x1a\x19google/protobuf/any.proto\x1a%tensorflow/core/framework/graph.proto\x1a&tensorflow/core/framework/op_def.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\x1a\x31tensorflow/core/protobuf/saved_object_graph.proto\x1a$tensorflow/core/protobuf/saver.proto\x1a%tensorflow/core/protobuf/struct.proto\"\xa8\x07\n\x0cMetaGraphDef\x12;\n\rmeta_info_def\x18\x01 \x01(\x0b\x32$.tensorflow.MetaGraphDef.MetaInfoDef\x12\'\n\tgraph_def\x18\x02 \x01(\x0b\x32\x14.tensorflow.GraphDef\x12\'\n\tsaver_def\x18\x03 \x01(\x0b\x32\x14.tensorflow.SaverDef\x12\x43\n\x0e\x63ollection_def\x18\x04 \x03(\x0b\x32+.tensorflow.MetaGraphDef.CollectionDefEntry\x12\x41\n\rsignature_def\x18\x05 \x03(\x0b\x32*.tensorflow.MetaGraphDef.SignatureDefEntry\x12\x30\n\x0e\x61sset_file_def\x18\x06 \x03(\x0b\x32\x18.tensorflow.AssetFileDef\x12\x36\n\x10object_graph_def\x18\x07 \x01(\x0b\x32\x1c.tensorflow.SavedObjectGraph\x1a\xf6\x02\n\x0bMetaInfoDef\x12\x1a\n\x12meta_graph_version\x18\x01 \x01(\t\x12,\n\x10stripped_op_list\x18\x02 \x01(\x0b\x32\x12.tensorflow.OpList\x12&\n\x08\x61ny_info\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x1a\n\x12tensorflow_version\x18\x05 \x01(\t\x12\x1e\n\x16tensorflow_git_version\x18\x06 \x01(\t\x12\x1e\n\x16stripped_default_attrs\x18\x07 \x01(\x08\x12S\n\x10\x66unction_aliases\x18\x08 \x03(\x0b\x32\x39.tensorflow.MetaGraphDef.MetaInfoDef.FunctionAliasesEntry\x1a\x36\n\x14\x46unctionAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aO\n\x12\x43ollectionDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.tensorflow.CollectionDef:\x02\x38\x01\x1aM\n\x11SignatureDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.tensorflow.SignatureDef:\x02\x38\x01\"\xdf\x03\n\rCollectionDef\x12\x37\n\tnode_list\x18\x01 \x01(\x0b\x32\".tensorflow.CollectionDef.NodeListH\x00\x12\x39\n\nbytes_list\x18\x02 \x01(\x0b\x32#.tensorflow.CollectionDef.BytesListH\x00\x12\x39\n\nint64_list\x18\x03 \x01(\x0b\x32#.tensorflow.CollectionDef.Int64ListH\x00\x12\x39\n\nfloat_list\x18\x04 \x01(\x0b\x32#.tensorflow.CollectionDef.FloatListH\x00\x12\x35\n\x08\x61ny_list\x18\x05 \x01(\x0b\x32!.tensorflow.CollectionDef.AnyListH\x00\x1a\x19\n\x08NodeList\x12\r\n\x05value\x18\x01 \x03(\t\x1a\x1a\n\tBytesList\x12\r\n\x05value\x18\x01 \x03(\x0c\x1a\x1e\n\tInt64List\x12\x11\n\x05value\x18\x01 \x03(\x03\x42\x02\x10\x01\x1a\x1e\n\tFloatList\x12\x11\n\x05value\x18\x01 \x03(\x02\x42\x02\x10\x01\x1a.\n\x07\x41nyList\x12#\n\x05value\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\x06\n\x04kind\"\xd1\x03\n\nTensorInfo\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x36\n\ncoo_sparse\x18\x04 \x01(\x0b\x32 .tensorflow.TensorInfo.CooSparseH\x00\x12\x42\n\x10\x63omposite_tensor\x18\x05 \x01(\x0b\x32&.tensorflow.TensorInfo.CompositeTensorH\x00\x12#\n\x05\x64type\x18\x02 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x32\n\x0ctensor_shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x1a\x65\n\tCooSparse\x12\x1a\n\x12values_tensor_name\x18\x01 \x01(\t\x12\x1b\n\x13indices_tensor_name\x18\x02 \x01(\t\x12\x1f\n\x17\x64\x65nse_shape_tensor_name\x18\x03 \x01(\t\x1ak\n\x0f\x43ompositeTensor\x12,\n\ttype_spec\x18\x01 \x01(\x0b\x32\x19.tensorflow.TypeSpecProto\x12*\n\ncomponents\x18\x02 \x03(\x0b\x32\x16.tensorflow.TensorInfoB\n\n\x08\x65ncoding\"\xa0\x02\n\x0cSignatureDef\x12\x34\n\x06inputs\x18\x01 \x03(\x0b\x32$.tensorflow.SignatureDef.InputsEntry\x12\x36\n\x07outputs\x18\x02 \x03(\x0b\x32%.tensorflow.SignatureDef.OutputsEntry\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x1a\x45\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.tensorflow.TensorInfo:\x02\x38\x01\x1a\x46\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.tensorflow.TensorInfo:\x02\x38\x01\"M\n\x0c\x41ssetFileDef\x12+\n\x0btensor_info\x18\x01 \x01(\x0b\x32\x16.tensorflow.TensorInfo\x12\x10\n\x08\x66ilename\x18\x02 \x01(\tB\x87\x01\n\x18org.tensorflow.frameworkB\x0fMetaGraphProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.protobuf.meta_graph_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.tensorflow.frameworkB\017MetaGraphProtosP\001ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\370\001\001'
  _METAGRAPHDEF_METAINFODEF_FUNCTIONALIASESENTRY._options = None
  _METAGRAPHDEF_METAINFODEF_FUNCTIONALIASESENTRY._serialized_options = b'8\001'
  _METAGRAPHDEF_COLLECTIONDEFENTRY._options = None
  _METAGRAPHDEF_COLLECTIONDEFENTRY._serialized_options = b'8\001'
  _METAGRAPHDEF_SIGNATUREDEFENTRY._options = None
  _METAGRAPHDEF_SIGNATUREDEFENTRY._serialized_options = b'8\001'
  _COLLECTIONDEF_INT64LIST.fields_by_name['value']._options = None
  _COLLECTIONDEF_INT64LIST.fields_by_name['value']._serialized_options = b'\020\001'
  _COLLECTIONDEF_FLOATLIST.fields_by_name['value']._options = None
  _COLLECTIONDEF_FLOATLIST.fields_by_name['value']._serialized_options = b'\020\001'
  _SIGNATUREDEF_INPUTSENTRY._options = None
  _SIGNATUREDEF_INPUTSENTRY._serialized_options = b'8\001'
  _SIGNATUREDEF_OUTPUTSENTRY._options = None
  _SIGNATUREDEF_OUTPUTSENTRY._serialized_options = b'8\001'
  _METAGRAPHDEF._serialized_start=377
  _METAGRAPHDEF._serialized_end=1313
  _METAGRAPHDEF_METAINFODEF._serialized_start=779
  _METAGRAPHDEF_METAINFODEF._serialized_end=1153
  _METAGRAPHDEF_METAINFODEF_FUNCTIONALIASESENTRY._serialized_start=1099
  _METAGRAPHDEF_METAINFODEF_FUNCTIONALIASESENTRY._serialized_end=1153
  _METAGRAPHDEF_COLLECTIONDEFENTRY._serialized_start=1155
  _METAGRAPHDEF_COLLECTIONDEFENTRY._serialized_end=1234
  _METAGRAPHDEF_SIGNATUREDEFENTRY._serialized_start=1236
  _METAGRAPHDEF_SIGNATUREDEFENTRY._serialized_end=1313
  _COLLECTIONDEF._serialized_start=1316
  _COLLECTIONDEF._serialized_end=1795
  _COLLECTIONDEF_NODELIST._serialized_start=1622
  _COLLECTIONDEF_NODELIST._serialized_end=1647
  _COLLECTIONDEF_BYTESLIST._serialized_start=1649
  _COLLECTIONDEF_BYTESLIST._serialized_end=1675
  _COLLECTIONDEF_INT64LIST._serialized_start=1677
  _COLLECTIONDEF_INT64LIST._serialized_end=1707
  _COLLECTIONDEF_FLOATLIST._serialized_start=1709
  _COLLECTIONDEF_FLOATLIST._serialized_end=1739
  _COLLECTIONDEF_ANYLIST._serialized_start=1741
  _COLLECTIONDEF_ANYLIST._serialized_end=1787
  _TENSORINFO._serialized_start=1798
  _TENSORINFO._serialized_end=2263
  _TENSORINFO_COOSPARSE._serialized_start=2041
  _TENSORINFO_COOSPARSE._serialized_end=2142
  _TENSORINFO_COMPOSITETENSOR._serialized_start=2144
  _TENSORINFO_COMPOSITETENSOR._serialized_end=2251
  _SIGNATUREDEF._serialized_start=2266
  _SIGNATUREDEF._serialized_end=2554
  _SIGNATUREDEF_INPUTSENTRY._serialized_start=2413
  _SIGNATUREDEF_INPUTSENTRY._serialized_end=2482
  _SIGNATUREDEF_OUTPUTSENTRY._serialized_start=2484
  _SIGNATUREDEF_OUTPUTSENTRY._serialized_end=2554
  _ASSETFILEDEF._serialized_start=2556
  _ASSETFILEDEF._serialized_end=2633
# @@protoc_insertion_point(module_scope)