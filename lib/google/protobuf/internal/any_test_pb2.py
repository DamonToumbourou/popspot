# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/any_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/any_test.proto',
  package='google.protobuf.internal',
  syntax='proto2',
  serialized_pb=_b('\n\'google/protobuf/internal/any_test.proto\x12\x18google.protobuf.internal\x1a\x19google/protobuf/any.proto\"K\n\x07TestAny\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\tint_value\x18\x02 \x01(\x05*\x08\x08\n\x10\x80\x80\x80\x80\x02\"\x85\x01\n\x11TestAnyExtension1\x12\t\n\x01i\x18\x0f \x01(\x05\x32\x65\n\nextension1\x12!.google.protobuf.internal.TestAny\x18\xab\xff\xf6. \x01(\x0b\x32+.google.protobuf.internal.TestAnyExtension1')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_TESTANY = _descriptor.Descriptor(
  name='TestAny',
  full_name='google.protobuf.internal.TestAny',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.internal.TestAny.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='google.protobuf.internal.TestAny.int_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10, 536870912), ],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=171,
)


_TESTANYEXTENSION1 = _descriptor.Descriptor(
  name='TestAnyExtension1',
  full_name='google.protobuf.internal.TestAnyExtension1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='i', full_name='google.protobuf.internal.TestAnyExtension1.i', index=0,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='extension1', full_name='google.protobuf.internal.TestAnyExtension1.extension1', index=0,
      number=98418603, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=307,
)

_TESTANY.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['TestAny'] = _TESTANY
DESCRIPTOR.message_types_by_name['TestAnyExtension1'] = _TESTANYEXTENSION1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestAny = _reflection.GeneratedProtocolMessageType('TestAny', (_message.Message,), dict(
  DESCRIPTOR = _TESTANY,
  __module__ = 'google.protobuf.internal.any_test_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.internal.TestAny)
  ))
_sym_db.RegisterMessage(TestAny)

TestAnyExtension1 = _reflection.GeneratedProtocolMessageType('TestAnyExtension1', (_message.Message,), dict(
  DESCRIPTOR = _TESTANYEXTENSION1,
  __module__ = 'google.protobuf.internal.any_test_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.internal.TestAnyExtension1)
  ))
_sym_db.RegisterMessage(TestAnyExtension1)

_TESTANYEXTENSION1.extensions_by_name['extension1'].message_type = _TESTANYEXTENSION1
TestAny.RegisterExtension(_TESTANYEXTENSION1.extensions_by_name['extension1'])

# @@protoc_insertion_point(module_scope)
