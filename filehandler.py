# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# filehandler.py
# May 10, 2021
import mmap
import os

# Optimized (I hope) IO, much faster than just using open()
# Using UTF8 encoding
def fileHandler(id, codes):
  for fileName, code in codes.items():
    # startT = time.perf_counter()
    path = f'temp/{id}/{fileName}'
    binary = code.encode('utf-8')
    lenBinary = len(binary)
    # print(binary, len(binary))
    fd = os.open(path, os.O_RDWR|os.O_CREAT)
    os.ftruncate(fd, lenBinary)
    with open(path, mode='r+', encoding='utf8') as file_obj:
      with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_DEFAULT) as mmap_obj:
            mmap_obj.write(binary)
            mmap_obj.flush()
    # print('Finished in', time.perf_counter()-startT)