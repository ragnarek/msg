import storage
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def add(channel, message):
	data = {"time": current_milli_time(), "message": message}
	return storage.add(channel, data)

def get(channel, fromDate, toDate):
	messages = storage.get(channel)
	if messages == None:
		return None
	ret = []
	for message in messages:
		if fromDate <= message["time"] <= toDate:
			ret.append(message)
	return ret
