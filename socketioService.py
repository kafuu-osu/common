import uuid
import socketio
import time
from common.log import logUtils as log



class Client:
    def __init__(self, serverUrl=None):
        self.sio = socketio.Client()
        self.sioServer = serverUrl

        if self.sioServer: self.connect()
        self.sio.on('disconnect', self.handleDisconnect)

    def send(self, event, data, userData={}, namespace=None):
        sendTime = time.time()
        if not self.sio.sid: self.connect()
        
        eventId = str(uuid.uuid1())
        
        # Send event
        self.sio.emit(
            'adapter.emitToBus', (event, eventId, data, sendTime ), namespace=namespace)
        # Update user data
        if userData: self.sio.emit(
            'adapter.emitToBus', ('user.updateStateFromPep', eventId, userData, sendTime ))

        log.info('socketio sended event: {}, user: {}({}), time spent: {}s'.format(
            event, userData.get('username'), userData.get('userID'), time.time()-sendTime))

    def connect(self):
        try:
            self.sio.connect(self.sioServer)
            log.info('socketio server connected: {}'.format(self.sio.sid))
        except Exception as err:
            log.warning('socketio connect failed, err: {}'.format(err))

    def handleDisconnect(self):
        self.sio.disconnect()
        log.info('socketio server disconnect!')
        log.info('try to reconnecting...')
        self.connect()
        log.info('socketio server reconnected!')


