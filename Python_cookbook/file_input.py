#! /usr/bin/env python3
import fileinput

with fileinput.input() as f:
    for line in f:
        print(line, end='')

# ls | ./file_input.py
# __pycache__
# file_input.py
# file_input_multi_files.py

'''
The two following opening hooks are provided by this module:

fileinput.hook_compressed(filename, mode)
Transparently opens files compressed with gzip and bzip2 (recognized by the extensions '.gz' and '.bz2') using the gzip and bz2 modules. If the filename extension is not '.gz' or '.bz2', the file is opened normally (ie, using open() without any decompression).

Usage example: fi = fileinput.FileInput(openhook=fileinput.hook_compressed)

fileinput.hook_encoded(encoding, errors=None)
Returns a hook which opens each file with open(), using the given encoding and errors to read the file.

Usage example: fi = fileinput.FileInput(openhook=fileinput.hook_encoded("utf-8", "surrogateescape"))

Changed in version 3.6: Added the optional errors parameter.
'''