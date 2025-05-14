#!/usr/bin/env python
import os
import sys

def convert_font_to_header(font_path, output_path, array_name):
    # Read the font file as binary
    with open(font_path, 'rb') as f:
        font_data = f.read()
    
    # Create the header file
    with open(output_path, 'w') as f:
        # Write header guard
        header_guard = os.path.basename(output_path).replace('.', '_').upper()
        f.write(f'#ifndef {header_guard}\n')
        f.write(f'#define {header_guard}\n\n')
        
        # Write array size
        f.write(f'const unsigned int {array_name}_size = {len(font_data)};\n\n')
        
        # Write array data
        f.write(f'const unsigned char {array_name}[] = {{\n    ')
        
        # Format the binary data as a C array
        bytes_per_line = 12
        for i, byte in enumerate(font_data):
            f.write(f'0x{byte:02x}')
            if i < len(font_data) - 1:
                f.write(', ')
                if (i + 1) % bytes_per_line == 0:
                    f.write('\n    ')
        
        f.write('\n};\n\n')
        
        # Close header guard
        f.write(f'#endif // {header_guard}\n')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <font_file> <output_header> <array_name>")
        sys.exit(1)
    
    font_path = sys.argv[1]
    output_path = sys.argv[2]
    array_name = sys.argv[3]
    
    convert_font_to_header(font_path, output_path, array_name)
    print(f"Successfully converted {font_path} to {output_path}")
