import os
dir_path='/path/to/file'
extension='.extension_name'

files=os.listdir(dir_path)
ext_files=[f for f in files if f.endswith(extension)]

for f in ext_files:
    file_path=os.path.join(dir_path,f)
    os.remove(file_path)
