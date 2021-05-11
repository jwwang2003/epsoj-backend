import mmap
import time

def fileHandler(id, codes):
  for fileName, code in codes.items():
    binary = code.encode('utf-8')
    open(f'temp/{id}/{fileName}', "wb")
    with open(f'temp/{id}/{fileName}', mode='r+', encoding='utf8') as file_obj:
      with mmap.mmap(file_obj.fileno(), length=len(binary), access=mmap.ACCESS_WRITE) as mmap_obj:
            mmap_obj.write(binary)
            mmap_obj.flush()