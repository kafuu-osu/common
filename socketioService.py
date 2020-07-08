import uuid
import socketio
import time
from common.log import logUtils as log



class Client:
	def __init__(self, serverUrl=None):
		self.sio = socketio.Client()
		self.sioServer = serverUrl
		if self.sioServer: self.connect()

	def send(self, event, data, userData={}):
		sendTime = time.time()
		if not self.sio.sid: self.connect()
		
		eventId = str(uuid.uuid1())
		baseData = {'eventId': eventId,'time': sendTime}
		
		# Send event
		self.sio.emit(
			'adapter.emitToBus', { **baseData, 'event': event, 'args': data })
		# Update user data
		if userData: self.sio.emit(
			'adapter.emitToBus', { **baseData, 'event': 'user.updateStateFromPep', 'userData': userData })

		log.info('socketio sended event: {}, user: {}({}), time spent: {}s'.format(
			event, userData.get('username'), userData.get('userID'), time.time()-sendTime))

	def connect(self):
		try:
			self.sio.connect(self.sioServer)
			log.info('socketio server connected: {}'.format(self.sio.sid))
		except Exception as err:
			log.warning('socketio connect failed, err: {}'.format(err))


