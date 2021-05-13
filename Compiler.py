# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# Compiler.py
# May 10, 2021

import re
import os, glob, importlib.machinery

class Compiler:
  compilers = {}

  def __init__(self):
    for path in glob.glob('compilers/[!_]*.py'):
      name, ext = os.path.splitext(os.path.basename(path))
      loader = importlib.machinery.SourceFileLoader(name, path)
      self.compilers[name] = loader.load_module()

  def getCompiler(self, lang):
    # Simple regex equation to get the language and version
    m = re.match('([\D]+)(\d+)?', lang)
    language, version = m.groups()
    # Return appropriate compiler for the specified language
    return self.compilers[language].compile