

from typing import List, Tuple

import genmsg

# TODO pull this out into seperate function
# TODO verify these are sensible and msg_type->py_type never loses information 
# ... what makes sense for unsigned ints?
# Consult https://docs.python.org/3/library/struct.html#format-characters
PY_TYPE_STRINGS = {
    'int8': 'int',
    'uint8': 'int',
    'uint16': 'int',
    'int32': 'int',
    'uint32': 'int', 
    'int64': 'int',
    'uint64': 'int',
    'float32': 'float',
    'float64': 'float',
    'string': 'bytes', # ??? TODO char[]
    'bool': 'bool',
    'char': 'bytes', # ?
    'time': 'Tuple[int, int]'       , # See: https://github.com/Pickle-Robot/genmsg/blob/b3c24ea4a75ac494e4f94bf88e8838c71f4280a5/src/genmsg/msgs.py#L326
    'duration': 'Tuple[int, int]' 
}


def generate_fields(spec_names: List[str], spec_types: List[str] ) -> Tuple[List[str], List[str]]:
    feild_definitions: List[str] = []
    optional_feild_definitions: List[str] = []
    for spec_name, spec_type in zip(spec_names, spec_types):

        base_type, is_array, array_length, is_optional = genmsg.msgs.parse_type(spec_type)
        if len(base_type.split('/')) > 1:
            # base_type = base_type.translate(str.maketrans({'/': '.'}))
            base_type = '.'.join(base_type.split('/')[:-1]) + '.msg.' +  base_type.split('/')[-1]
        
        if base_type in PY_TYPE_STRINGS:
            base_type = PY_TYPE_STRINGS[base_type]

        # TODO verify this handles header types            
            
        if is_array and array_length:
            format_spec_type_hint = f'Tuple[{", ".join([base_type]*array_length)}]'
        elif is_array:
            format_spec_type_hint = f'List[{base_type}]'
        else:
            format_spec_type_hint = base_type
        
        if is_optional:
            optional_feild_definitions.append(f'{spec_name}: Optional[{format_spec_type_hint}]')
        else:
            feild_definitions.append(f'{spec_name}: {format_spec_type_hint}')

    return (feild_definitions, optional_feild_definitions)
