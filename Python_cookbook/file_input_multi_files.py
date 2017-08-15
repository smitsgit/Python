#! /usr/bin/env python3
import fileinput

with fileinput.input(files=('file_input.py', 'file_input_multi_files.py')) as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')


# ./file_input_multi_files.py

# file_input.py 1 #! /usr/bin/env python3
# file_input.py 2 import fileinput
# file_input.py 3
# file_input.py 4 with fileinput.input() as f:
# file_input.py 5     print()
# file_input.py 6     for line in f:
# file_input.py 7         print(line, end='\n')file_input_multi_files.py 8 #! /usr/bin/env python3
# file_input_multi_files.py 9 import fileinput
# file_input_multi_files.py 10
# file_input_multi_files.py 11 with fileinput.input(files=('file_input.py', 'file_input_multi_files.py')) as f:
# file_input_multi_files.py 12     for line in f:
# file_input_multi_files.py 13         print(f.filename(), f.lineno(), line, end='')%