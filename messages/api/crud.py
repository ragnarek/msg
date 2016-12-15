import storage
import time
from uuid import uuid4

current_milli_time = lambda: int(round(time.time() * 1000))

def add(channel, message):
	data = {"id": uuid4().hex, "time": current_milli_time(), "message": message}
	return storage.add(channel, data)

def get(channel, fromDate, toDate, id=None):
	messages = storage.get(channel)
	if messages == None:
		return None
	ret = []
	for message in messages:
		if fromDate <= message["time"] <= toDate and id == None or message["id"] == id:
			ret.append(message)
	return ret
