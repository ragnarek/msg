import storage
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def add(channel, message):
	data = {"time": current_milli_time(), "message": message}
	return storage.add(channel, data)

def get(channel, fromDate=None, toDate=None):
	return storage.get(channel)