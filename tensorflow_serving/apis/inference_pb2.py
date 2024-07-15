# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/inference.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow_serving.apis import classification_pb2 as tensorflow__serving_dot_apis_dot_classification__pb2
from tensorflow_serving.apis import input_pb2 as tensorflow__serving_dot_apis_dot_input__pb2
from tensorflow_serving.apis import model_pb2 as tensorflow__serving_dot_apis_dot_model__pb2
from tensorflow_serving.apis import regression_pb2 as tensorflow__serving_dot_apis_dot_regression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'tensorflow_serving/apis/inference.proto\x12\x12tensorflow.serving\x1a,tensorflow_serving/apis/classification.proto\x1a#tensorflow_serving/apis/input.proto\x1a#tensorflow_serving/apis/model.proto\x1a(tensorflow_serving/apis/regression.proto\"W\n\rInferenceTask\x12\x31\n\nmodel_spec\x18\x01 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\"\xdc\x01\n\x0fInferenceResult\x12\x31\n\nmodel_spec\x18\x01 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\x12I\n\x15\x63lassification_result\x18\x02 \x01(\x0b\x32(.tensorflow.serving.ClassificationResultH\x00\x12\x41\n\x11regression_result\x18\x03 \x01(\x0b\x32$.tensorflow.serving.RegressionResultH\x00\x42\x08\n\x06result\"s\n\x15MultiInferenceRequest\x12\x30\n\x05tasks\x18\x01 \x03(\x0b\x32!.tensorflow.serving.InferenceTask\x12(\n\x05input\x18\x02 \x01(\x0b\x32\x19.tensorflow.serving.Input\"N\n\x16MultiInferenceResponse\x12\x34\n\x07results\x18\x01 \x03(\x0b\x32#.tensorflow.serving.InferenceResultB\x03\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow_serving.apis.inference_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _INFERENCETASK._serialized_start=225
  _INFERENCETASK._serialized_end=312
  _INFERENCERESULT._serialized_start=315
  _INFERENCERESULT._serialized_end=535
  _MULTIINFERENCEREQUEST._serialized_start=537
  _MULTIINFERENCEREQUEST._serialized_end=652
  _MULTIINFERENCERESPONSE._serialized_start=654
  _MULTIINFERENCERESPONSE._serialized_end=732
# @@protoc_insertion_point(module_scope)