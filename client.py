# Elgin Park Secondary Online Judge (EPSOJ) - Backend
# client.py
# May 7, 2021

"""
['Server' NodeJS]<--------->['Client' Python Backend]
Connect & disconnect events <->
New Submission -> ~
  - New submission ticket ~
Submission acknowledge <- ~
Current progress (compilation info, etc.) <-
Final results <-
Acknowledge final results ->
  - Close submission ticket
QueueSize <- ~
"""

import socketio
import asyncio
import multiprocessing
import debug.logger as logger
from compiler import Compiler
from submission import Submission
from timeout import TimeoutException, tlim

class Client:
    # Instantiating SocketIO Client
    __sio = socketio.AsyncClient()
    __compiler = Compiler()

    def __init__(self, PORT):
        self.PORT = PORT
        asyncio.run(self.start())

    async def start(self):
        await self.__sio.connect(f'http://localhost:{self.PORT}')
        await self.__sio.wait()

    # SocketIO events
    # --------------------------------------------------------------
    @__sio.event
    def connect():
        logger.info(
            f'Connection to NodeJS established UID: {Client.__sio.sid}')

    @__sio.event
    def disconnect():
        logger.info(f'Backend disconnected from NodeJS')

    @__sio.event
    async def submission(data):
		# Deconstructing data
        id, lang, code = data.values()

		# Send an acknowledge packet
        await Client.__sio.emit('submissionAck', {'id': id})

        p = multiprocessing.Process(
            name=f'Submission-{id}', target=Client.handleSubmission, args=(id, lang, code))
        p.daemon = True
        p.start()

    @__sio.event
    async def getPoolSize():
        await Client.__sio.emit('getPoolSize', len(multiprocessing.active_children()))

    def handleSubmission(id, lang, code):
        # Maximum time 
        try:
            with tlim(5):
                logger.info(f'[PROCESSING] {multiprocessing.current_process().name}')

                # Get compiler
                c = Client.__compiler.getCompiler(lang)
                s = Submission(id, lang, code, c)
                s.start()

        except TimeoutException:
            return
        finally:
            pass
        