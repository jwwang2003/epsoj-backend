# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# server.py
# May 7, 2021

import socketio
from aiohttp import web
import multiprocessing
import debug.logger as logger
from submission import Submission

class Server:
  # Instantiating SocketIO Server
  __sio = socketio.AsyncServer(async_mode='aiohttp')
  __app = web.Application()
  __sio.attach(__app)
  _numUser = 0

  def __init__(self, PORT):
    # Starting web app
    web.run_app(self.__app, port=PORT)

  # SocketIO events
  # --------------------------------------------------------------
  @__sio.event
  def connect(sid, environ):
    # No need to handle auth since the only connection being made
    # are from the NodeJS backend that already authenticated users
    if(environ['REMOTE_ADDR'] == '127.0.0.1'):
      logger.info(f'[CONNECT EVENT] {sid}')
    else:
      raise socketio.exceptions.ConnectionRefusedError('IP Authentication Failed')

  @__sio.event
  def disconnect(sid, environ):
    logger.info(f'[DISCONNECT EVENT] {sid}')

  @__sio.event
  def submission(sid, data):
    id, lang, code = data.values()
    s = Submission(id, lang, code)
    

  @__sio.event
  async def getPoolSize():
    await Server.__sio.emit('getPoolSize', len(multiprocessing.active_children()))