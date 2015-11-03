import compileall
import os

compileall.compile_dir('./')
files = os.walk('./')

for d, fd, fl in files:
    for f in fl:
        if f == 'remove_py.pyc':
            continue
        if f.split('.')[-1] == 'pyc':
            os.remove('/'.join([d, f]))
            
raw_input()