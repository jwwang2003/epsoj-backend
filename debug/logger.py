# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# logger.py
# May 6, 2021

import logging

# Initialize logger
logger = logging.getLogger('EPSOJ')
logger.setLevel(logging.DEBUG)

# Output
fh = logging.FileHandler('debug/EPSOJ.log')
fh.setLevel(logging.DEBUG)

# Log formatting
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# Add the handler to logger
logger.addHandler(fh)

def info(msg):
  print(f'<INFO> {msg}')
  logger.info(msg)

def debug(msg):
  print(f'<DEBUG> {msg}')
  logger.debug(msg)

def error(msg):
  print(f'<ERROR> {msg}')
  logger.error(msg)