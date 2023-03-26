from typing import List, Tuple
import genmsg
from genpy.base import PY_TYPE_STRINGS



def generate_fields(spec_names: List[str], spec_types: List[str] ) -> List[Tuple[str, str, str]]:
    field_definitions: List[str] = []
    for spec_name, spec_type in zip(spec_names, spec_types):

        base_type, is_array, array_length = genmsg.msgs.parse_type(spec_type)
        if len(base_type.split('/')) > 1:
            base_type = '.'.join(base_type.split('/')[:-1]) + '_msg.' +  base_type.split('/')[-1]
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
