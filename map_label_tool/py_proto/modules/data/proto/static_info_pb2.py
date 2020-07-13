# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/data/proto/static_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.canbus.proto import canbus_conf_pb2 as modules_dot_canbus_dot_proto_dot_canbus__conf__pb2
from modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from modules.common.configs.proto import vehicle_config_pb2 as modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2
from modules.control.proto import control_conf_pb2 as modules_dot_control_dot_proto_dot_control__conf__pb2
from modules.routing.proto import routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/data/proto/static_info.proto',
  package='apollo.data',
  syntax='proto2',
  serialized_pb=_b('\n$modules/data/proto/static_info.proto\x12\x0b\x61pollo.data\x1a&modules/canbus/proto/canbus_conf.proto\x1a\"modules/canbus/proto/chassis.proto\x1a\x31modules/common/configs/proto/vehicle_config.proto\x1a(modules/control/proto/control_conf.proto\x1a#modules/routing/proto/routing.proto\"\x97\x03\n\x0bVehicleInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x05\x62rand\x18\x02 \x01(\x0e\x32\x1e.apollo.data.VehicleInfo.Brand\x12-\n\x05model\x18\x03 \x01(\x0e\x32\x1e.apollo.data.VehicleInfo.Model\x12+\n\x07license\x18\x04 \x01(\x0b\x32\x16.apollo.canbus.LicenseB\x02\x18\x01\x12.\n\x0b\x63\x61nbus_conf\x18\x05 \x01(\x0b\x32\x19.apollo.canbus.CanbusConf\x12\x34\n\x0evehicle_config\x18\x06 \x01(\x0b\x32\x1c.apollo.common.VehicleConfig\x12\x33\n\x0e\x63ontrol_config\x18\x07 \x01(\x0b\x32\x1b.apollo.control.ControlConf\")\n\x05\x42rand\x12\x0b\n\x07LINCOLN\x10\x01\x12\x08\n\x04\x46ORD\x10\x02\x12\t\n\x05LEXUS\x10\x03\")\n\x05Model\x12\x07\n\x03MKZ\x10\x01\x12\x0b\n\x07TRANSIT\x10\x02\x12\n\n\x06RX450H\x10\x03\"<\n\x0f\x45nvironmentInfo\x12\x14\n\x08map_name\x18\x01 \x01(\tB\x02\x18\x01\x12\x13\n\x0btemperature\x18\x02 \x01(\x02\"w\n\x0cHardwareInfo\x12\x37\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32&.apollo.data.HardwareInfo.ConfigsEntry\x1a.\n\x0c\x43onfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf6\x01\n\x0cSoftwareInfo\x12\x18\n\x0c\x64ocker_image\x18\x01 \x01(\tB\x02\x18\x01\x12\x11\n\tcommit_id\x18\x02 \x01(\t\x12\x10\n\x04mode\x18\x03 \x01(\tB\x02\x18\x01\x12\x37\n\x07\x63onfigs\x18\x04 \x03(\x0b\x32&.apollo.data.SoftwareInfo.ConfigsEntry\x12>\n\x16latest_routing_request\x18\x05 \x01(\x0b\x32\x1e.apollo.routing.RoutingRequest\x1a.\n\x0c\x43onfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"=\n\x08UserInfo\x12\x0e\n\x06\x65ntity\x18\x01 \x01(\t\x12\x0e\n\x06\x64river\x18\x02 \x01(\t\x12\x11\n\tco_driver\x18\x03 \x01(\t\"\xe9\x01\n\nStaticInfo\x12)\n\x07vehicle\x18\x01 \x01(\x0b\x32\x18.apollo.data.VehicleInfo\x12\x31\n\x0b\x65nvironment\x18\x02 \x01(\x0b\x32\x1c.apollo.data.EnvironmentInfo\x12+\n\x08hardware\x18\x03 \x01(\x0b\x32\x19.apollo.data.HardwareInfo\x12+\n\x08software\x18\x04 \x01(\x0b\x32\x19.apollo.data.SoftwareInfo\x12#\n\x04user\x18\x05 \x01(\x0b\x32\x15.apollo.data.UserInfo\"D\n\x0eStaticInfoConf\x12\x18\n\x10hardware_configs\x18\x01 \x03(\t\x12\x18\n\x10software_configs\x18\x02 \x03(\t')
  ,
  dependencies=[modules_dot_canbus_dot_proto_dot_canbus__conf__pb2.DESCRIPTOR,modules_dot_canbus_dot_proto_dot_chassis__pb2.DESCRIPTOR,modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2.DESCRIPTOR,modules_dot_control_dot_proto_dot_control__conf__pb2.DESCRIPTOR,modules_dot_routing_dot_proto_dot_routing__pb2.DESCRIPTOR,])



_VEHICLEINFO_BRAND = _descriptor.EnumDescriptor(
  name='Brand',
  full_name='apollo.data.VehicleInfo.Brand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LINCOLN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEXUS', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=583,
  serialized_end=624,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEINFO_BRAND)

_VEHICLEINFO_MODEL = _descriptor.EnumDescriptor(
  name='Model',
  full_name='apollo.data.VehicleInfo.Model',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MKZ', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSIT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RX450H', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=626,
  serialized_end=667,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEINFO_MODEL)


_VEHICLEINFO = _descriptor.Descriptor(
  name='VehicleInfo',
  full_name='apollo.data.VehicleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apollo.data.VehicleInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brand', full_name='apollo.data.VehicleInfo.brand', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='apollo.data.VehicleInfo.model', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='license', full_name='apollo.data.VehicleInfo.license', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='canbus_conf', full_name='apollo.data.VehicleInfo.canbus_conf', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle_config', full_name='apollo.data.VehicleInfo.vehicle_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control_config', full_name='apollo.data.VehicleInfo.control_config', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VEHICLEINFO_BRAND,
    _VEHICLEINFO_MODEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=667,
)


_ENVIRONMENTINFO = _descriptor.Descriptor(
  name='EnvironmentInfo',
  full_name='apollo.data.EnvironmentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_name', full_name='apollo.data.EnvironmentInfo.map_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='apollo.data.EnvironmentInfo.temperature', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=669,
  serialized_end=729,
)


_HARDWAREINFO_CONFIGSENTRY = _descriptor.Descriptor(
  name='ConfigsEntry',
  full_name='apollo.data.HardwareInfo.ConfigsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.data.HardwareInfo.ConfigsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.data.HardwareInfo.ConfigsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=850,
)

_HARDWAREINFO = _descriptor.Descriptor(
  name='HardwareInfo',
  full_name='apollo.data.HardwareInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configs', full_name='apollo.data.HardwareInfo.configs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HARDWAREINFO_CONFIGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=731,
  serialized_end=850,
)


_SOFTWAREINFO_CONFIGSENTRY = _descriptor.Descriptor(
  name='ConfigsEntry',
  full_name='apollo.data.SoftwareInfo.ConfigsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.data.SoftwareInfo.ConfigsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.data.SoftwareInfo.ConfigsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=850,
)

_SOFTWAREINFO = _descriptor.Descriptor(
  name='SoftwareInfo',
  full_name='apollo.data.SoftwareInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docker_image', full_name='apollo.data.SoftwareInfo.docker_image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='commit_id', full_name='apollo.data.SoftwareInfo.commit_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='apollo.data.SoftwareInfo.mode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='configs', full_name='apollo.data.SoftwareInfo.configs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latest_routing_request', full_name='apollo.data.SoftwareInfo.latest_routing_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SOFTWAREINFO_CONFIGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=853,
  serialized_end=1099,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='apollo.data.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='apollo.data.UserInfo.entity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driver', full_name='apollo.data.UserInfo.driver', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='co_driver', full_name='apollo.data.UserInfo.co_driver', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1101,
  serialized_end=1162,
)


_STATICINFO = _descriptor.Descriptor(
  name='StaticInfo',
  full_name='apollo.data.StaticInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vehicle', full_name='apollo.data.StaticInfo.vehicle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='environment', full_name='apollo.data.StaticInfo.environment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hardware', full_name='apollo.data.StaticInfo.hardware', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='software', full_name='apollo.data.StaticInfo.software', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='apollo.data.StaticInfo.user', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1165,
  serialized_end=1398,
)


_STATICINFOCONF = _descriptor.Descriptor(
  name='StaticInfoConf',
  full_name='apollo.data.StaticInfoConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hardware_configs', full_name='apollo.data.StaticInfoConf.hardware_configs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='software_configs', full_name='apollo.data.StaticInfoConf.software_configs', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1400,
  serialized_end=1468,
)

_VEHICLEINFO.fields_by_name['brand'].enum_type = _VEHICLEINFO_BRAND
_VEHICLEINFO.fields_by_name['model'].enum_type = _VEHICLEINFO_MODEL
_VEHICLEINFO.fields_by_name['license'].message_type = modules_dot_canbus_dot_proto_dot_chassis__pb2._LICENSE
_VEHICLEINFO.fields_by_name['canbus_conf'].message_type = modules_dot_canbus_dot_proto_dot_canbus__conf__pb2._CANBUSCONF
_VEHICLEINFO.fields_by_name['vehicle_config'].message_type = modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2._VEHICLECONFIG
_VEHICLEINFO.fields_by_name['control_config'].message_type = modules_dot_control_dot_proto_dot_control__conf__pb2._CONTROLCONF
_VEHICLEINFO_BRAND.containing_type = _VEHICLEINFO
_VEHICLEINFO_MODEL.containing_type = _VEHICLEINFO
_HARDWAREINFO_CONFIGSENTRY.containing_type = _HARDWAREINFO
_HARDWAREINFO.fields_by_name['configs'].message_type = _HARDWAREINFO_CONFIGSENTRY
_SOFTWAREINFO_CONFIGSENTRY.containing_type = _SOFTWAREINFO
_SOFTWAREINFO.fields_by_name['configs'].message_type = _SOFTWAREINFO_CONFIGSENTRY
_SOFTWAREINFO.fields_by_name['latest_routing_request'].message_type = modules_dot_routing_dot_proto_dot_routing__pb2._ROUTINGREQUEST
_STATICINFO.fields_by_name['vehicle'].message_type = _VEHICLEINFO
_STATICINFO.fields_by_name['environment'].message_type = _ENVIRONMENTINFO
_STATICINFO.fields_by_name['hardware'].message_type = _HARDWAREINFO
_STATICINFO.fields_by_name['software'].message_type = _SOFTWAREINFO
_STATICINFO.fields_by_name['user'].message_type = _USERINFO
DESCRIPTOR.message_types_by_name['VehicleInfo'] = _VEHICLEINFO
DESCRIPTOR.message_types_by_name['EnvironmentInfo'] = _ENVIRONMENTINFO
DESCRIPTOR.message_types_by_name['HardwareInfo'] = _HARDWAREINFO
DESCRIPTOR.message_types_by_name['SoftwareInfo'] = _SOFTWAREINFO
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['StaticInfo'] = _STATICINFO
DESCRIPTOR.message_types_by_name['StaticInfoConf'] = _STATICINFOCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VehicleInfo = _reflection.GeneratedProtocolMessageType('VehicleInfo', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLEINFO,
  __module__ = 'modules.data.proto.static_info_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.VehicleInfo)
  ))
_sym_db.RegisterMessage(VehicleInfo)

EnvironmentInfo = _reflection.GeneratedProtocolMessageType('EnvironmentInfo', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTINFO,
  __module__ = 'modules.data.proto.static_info_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.EnvironmentInfo)
  ))
_sym_db.RegisterMessage(EnvironmentInfo)

HardwareInfo = _reflection.GeneratedProtocolMessageType('HardwareInfo', (_message.Message,), dict(

  ConfigsEntry = _reflection.GeneratedProtocolMessageType('ConfigsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HARDWAREINFO_CONFIGSENTRY,
    __module__ = 'modules.data.proto.static_info_pb2'
    # @@protoc_insertion_point(class_scope:apollo.data.HardwareInfo.ConfigsEntry)
    ))
  ,
  DESCRIPTOR = _HARDWAREINFO,
  __module__ = 'modules.data.proto.static_info_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.HardwareInfo)
  ))
_sym_db.RegisterMessage(HardwareInfo)
_sym_db.RegisterMessage(HardwareInfo.ConfigsEntry)

SoftwareInfo = _reflection.GeneratedProtocolMessageType('SoftwareInfo', (_message.Message,), dict(

  ConfigsEntry = _reflection.GeneratedProtocolMessageType('ConfigsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SOFTWAREINFO_CONFIGSENTRY,
    __module__ = 'modules.data.proto.static_info_pb2'
    # @@protoc_insertion_point(class_scope:apollo.data.SoftwareInfo.ConfigsEntry)
    ))
  ,
  DESCRIPTOR = _SOFTWAREINFO,
  __module__ = 'modules.data.proto.static_info_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.SoftwareInfo)
  ))
_sym_db.RegisterMessage(SoftwareInfo)
_sym_db.RegisterMessage(SoftwareInfo.ConfigsEntry)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'modules.data.proto.static_info_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)

StaticInfo = _reflection.GeneratedProtocolMessageType('StaticInfo', (_message.Message,), dict(
  DESCRIPTOR = _STATICINFO,
  __module__ = 'modules.data.proto.static_info_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.StaticInfo)
  ))
_sym_db.RegisterMessage(StaticInfo)

StaticInfoConf = _reflection.GeneratedProtocolMessageType('StaticInfoConf', (_message.Message,), dict(
  DESCRIPTOR = _STATICINFOCONF,
  __module__ = 'modules.data.proto.static_info_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.StaticInfoConf)
  ))
_sym_db.RegisterMessage(StaticInfoConf)


_VEHICLEINFO.fields_by_name['license'].has_options = True
_VEHICLEINFO.fields_by_name['license']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_ENVIRONMENTINFO.fields_by_name['map_name'].has_options = True
_ENVIRONMENTINFO.fields_by_name['map_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_HARDWAREINFO_CONFIGSENTRY.has_options = True
_HARDWAREINFO_CONFIGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SOFTWAREINFO_CONFIGSENTRY.has_options = True
_SOFTWAREINFO_CONFIGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SOFTWAREINFO.fields_by_name['docker_image'].has_options = True
_SOFTWAREINFO.fields_by_name['docker_image']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_SOFTWAREINFO.fields_by_name['mode'].has_options = True
_SOFTWAREINFO.fields_by_name['mode']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)