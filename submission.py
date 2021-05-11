import os, shutil, mmap
from filehandler import fileHandler
import Compiler

class Submission:

  def __init__(self, id, lang, codes):
    self.id = id
    self.lang = lang
    self.codes = codes
    
  def start(self):
    self.initFile()
    c = Compiler.getCompiler(self.lang)

    shutil.rmtree(f'temp/{self.id}')
  
  def initFile(self):
    try:
      os.mkdir(f'temp/{self.id}')
    except:
      # Bad cleanup?
      # User's files from previous compilation
      # should not presist in temp directory
      shutil.rmtree(f'temp/{self.id}')
      os.mkdir(f'temp/{self.id}')
    
    fileHandler(self.id, self.codes)

    

Submission('632294', 'cpp14', {'main.cpp': '#include<iostream> \nusing namespace std; \nint main() { return 1; }'}).initFile()