from typing import List, Tuple
import genmsg


# REF https://docs.python.org/3/library/struct.html#format-characters
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
    'string': 'bytes',
    'bool': 'bool',
    'char': 'bytes',
    'time': 'Tuple[int, int]', # See: https://github.com/Pickle-Robot/genmsg/blob/b3c24ea4a75ac494e4f94bf88e8838c71f4280a5/src/genmsg/msgs.py#L326
    'duration': 'Tuple[int, int]' 
}

def generate_fields(spec_names: List[str], spec_types: List[str] ) -> List[Tuple[str, str, str]]:
    field_definitions: List[str] = []
    for spec_name, spec_type in zip(spec_names, spec_types):

        base_type, is_array, array_length = genmsg.msgs.parse_type(spec_type)
        if len(base_type.split('/')) > 1:
            # base_type = base_type.translate(str.maketrans({'/': '.'}))
            base_type = '.'.join(base_type.split('/')[:-1]) + '.msg.' +  base_type.split('/')[-1]
        
        if base_type in PY_TYPE_STRINGS:
            base_type = PY_TYPE_STRINGS[base_type]
    
        if is_array and array_length:
            format_spec_type_hint = f'Tuple[{", ".join([base_type]*array_length)}]'
        elif is_array:
            format_spec_type_hint = f'List[{base_type}]'
        else:
            format_spec_type_hint = base_type
        field_definitions.append((spec_name, spec_type, format_spec_type_hint))
        
    return field_definitions
