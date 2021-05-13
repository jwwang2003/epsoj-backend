# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# main.py ENTRY
# May 6, 2021

from client import Client
import sys
import os
import debug.logger as logger

if __name__ == '__main__':
  PORT = os.getenv('PORT') or 1314   # Pre-defined port

  try:
    logger.info('[STARTUP] Starting EPSOJ Backend')
    logger.info(f'Using port: {PORT}')
    Client(PORT)
  except:
    logger.error('[ERROR] Uh oh! Something went wrong :/')
    logger.error(sys.exc_info())
  finally:
    logger.info('[SHUTDOWN] Stopping all processes')