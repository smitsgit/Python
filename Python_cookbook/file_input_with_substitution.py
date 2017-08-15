import fileinput
import re


def modify_fastfile(full_path, version):
    print(full_path)
    mod_ver = r'  version_number = "{}"'.format(version)
    print(mod_ver)
    pattern = r'\s\sversion_number = \"\d.*\"'
    with fileinput.FileInput(full_path, inplace=True, backup='.bak') as file:
        for line in file:
            line = re.sub(pattern, mod_ver, line.rstrip())
            print(line)
    pass
