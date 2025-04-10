import os
import sys

def addModules(file, dir):
    print('__file__ | ', file)
    print('dir      | ', dir)
    script_dir = os.path.dirname(os.path.abspath(file))
    print(script_dir)
    # if(dir.start)
    modules_path = os.path.join(os.path.dirname(script_dir), dir)
    print(modules_path)
    return sys.path.append(modules_path)