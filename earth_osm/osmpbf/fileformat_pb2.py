# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: earth_osm/osmpbf/fileformat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!earth_osm/osmpbf/fileformat.proto\x12\x06OSMPBF\"\xa5\x01\n\x04\x42lob\x12\x10\n\x08raw_size\x18\x02 \x01(\x05\x12\r\n\x03raw\x18\x01 \x01(\x0cH\x00\x12\x13\n\tzlib_data\x18\x03 \x01(\x0cH\x00\x12\x13\n\tlzma_data\x18\x04 \x01(\x0cH\x00\x12!\n\x13OBSOLETE_bzip2_data\x18\x05 \x01(\x0c\x42\x02\x18\x01H\x00\x12\x12\n\x08lz4_data\x18\x06 \x01(\x0cH\x00\x12\x13\n\tzstd_data\x18\x07 \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"?\n\nBlobHeader\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x11\n\tindexdata\x18\x02 \x01(\x0c\x12\x10\n\x08\x64\x61tasize\x18\x03 \x02(\x05\x42\x0f\n\rcrosby.binary')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'earth_osm.osmpbf.fileformat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcrosby.binary'
  _BLOB.fields_by_name['OBSOLETE_bzip2_data']._options = None
  _BLOB.fields_by_name['OBSOLETE_bzip2_data']._serialized_options = b'\030\001'
  _BLOB._serialized_start=46
  _BLOB._serialized_end=211
  _BLOBHEADER._serialized_start=213
  _BLOBHEADER._serialized_end=276
# @@protoc_insertion_point(module_scope)