# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# main.py ENTRY
# May 6, 2021

from server import Server
import sys
import debugging.logger as logger

if __name__ == '__main__':
  PORT = 5000   # Pre-defined port

  try:
    logger.info('[STARTUP] Starting EPSOJ Backend')
    server = Server(PORT)
  except:
    logger.error('[ERROR] Uh oh! Something went wrong :/')
    logger.error(sys.exc_info()[0])
  finally:
    logger.info('[SHUTDOWN] Stopping all processes')