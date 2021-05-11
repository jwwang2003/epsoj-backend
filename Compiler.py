# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# Compiler.py
# May 10, 2021

import re
import os, glob, importlib.machinery
import debug.logger as logger

compilers = {}

for path in glob.glob('compilers/[!_]*.py'):
  name, ext = os.path.splitext(os.path.basename(path))
  loader = importlib.machinery.SourceFileLoader(name, path)
  compilers[name] = loader.load_module()

logger.info(f'Compilers Available: {compilers.keys()}')

def getCompiler(lang):
  # Simple regex equation to get the language and version
  m = re.match('([\D]+)(\d+)?', lang)
  language, version = m.groups()
  # Return appropriate compiler for the specified language
  return compilers[language].MAIN