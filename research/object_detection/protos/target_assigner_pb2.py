# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: research.object_detection/protos/target_assigner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from research.object_detection.protos import box_coder_pb2 as object__detection_dot_protos_dot_box__coder__pb2
from research.object_detection.protos import matcher_pb2 as object__detection_dot_protos_dot_matcher__pb2
from research.object_detection.protos import region_similarity_calculator_pb2 as object__detection_dot_protos_dot_region__similarity__calculator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='research.object_detection/protos/target_assigner.proto',
  package='research.object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-research.object_detection/protos/target_assigner.proto\x12\x17research.object_detection.protos\x1a\'research.object_detection/protos/box_coder.proto\x1a%research.object_detection/protos/matcher.proto\x1a:research.object_detection/protos/region_similarity_calculator.proto\"\xcd\x01\n\x0eTargetAssigner\x12\x31\n\x07matcher\x18\x01 \x01(\x0b\x32 .research.object_detection.protos.Matcher\x12R\n\x15similarity_calculator\x18\x02 \x01(\x0b\x32\x33.research.object_detection.protos.RegionSimilarityCalculator\x12\x34\n\tbox_coder\x18\x03 \x01(\x0b\x32!.research.object_detection.protos.BoxCoder'
  ,
  dependencies=[object__detection_dot_protos_dot_box__coder__pb2.DESCRIPTOR,object__detection_dot_protos_dot_matcher__pb2.DESCRIPTOR,object__detection_dot_protos_dot_region__similarity__calculator__pb2.DESCRIPTOR,])




_TARGETASSIGNER = _descriptor.Descriptor(
  name='TargetAssigner',
  full_name='research.object_detection.protos.TargetAssigner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matcher', full_name='research.object_detection.protos.TargetAssigner.matcher', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='similarity_calculator', full_name='research.object_detection.protos.TargetAssigner.similarity_calculator', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='box_coder', full_name='research.object_detection.protos.TargetAssigner.box_coder', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=420,
)

_TARGETASSIGNER.fields_by_name['matcher'].message_type = object__detection_dot_protos_dot_matcher__pb2._MATCHER
_TARGETASSIGNER.fields_by_name['similarity_calculator'].message_type = object__detection_dot_protos_dot_region__similarity__calculator__pb2._REGIONSIMILARITYCALCULATOR
_TARGETASSIGNER.fields_by_name['box_coder'].message_type = object__detection_dot_protos_dot_box__coder__pb2._BOXCODER
DESCRIPTOR.message_types_by_name['TargetAssigner'] = _TARGETASSIGNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetAssigner = _reflection.GeneratedProtocolMessageType('TargetAssigner', (_message.Message,), {
  'DESCRIPTOR' : _TARGETASSIGNER,
  '__module__' : 'research.object_detection.protos.target_assigner_pb2'
  # @@protoc_insertion_point(class_scope:research.object_detection.protos.TargetAssigner)
  })
_sym_db.RegisterMessage(TargetAssigner)


# @@protoc_insertion_point(module_scope)
